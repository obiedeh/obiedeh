import argparse
import logging
import os
from typing import Any

import httpx

from edge.adapters.base import VLMAdapter
from edge.adapters.mock_vlm import MockVLMAdapter
from edge.adapters.openai_compatible import CosmosReason2Adapter, OpenAICompatibleAdapter
from edge.frame_sampler import sample_frames
from edge.source_loader import VideoSource, load_source
from rules.engine import SafetyPolicyEngine
from telemetry.logging import configure_logging, log_event
from telemetry.metrics import metrics
from telemetry.runtime import RuntimeMonitor, Timer

logger = logging.getLogger("edge.worker")


def build_adapter(args: argparse.Namespace) -> VLMAdapter:
    if args.adapter == "mock":
        return MockVLMAdapter()
    if args.adapter == "openai-compatible":
        api_key = os.getenv(args.api_key_env) if args.api_key_env else None
        return OpenAICompatibleAdapter(
            endpoint=args.adapter_endpoint,
            model=args.model,
            api_key=api_key,
        )
    if args.adapter == "cosmos-reason2":
        api_key = os.getenv(args.api_key_env) if args.api_key_env else None
        return CosmosReason2Adapter(
            endpoint=args.adapter_endpoint,
            model=args.model,
            api_key=api_key,
        )
    raise ValueError(f"unsupported adapter: {args.adapter}")


def post_event(backend: str, event_payload: dict[str, Any]) -> None:
    response = httpx.post(f"{backend.rstrip('/')}/events", json=event_payload, timeout=10)
    response.raise_for_status()


def run_worker(
    *,
    source: VideoSource,
    backend: str,
    adapter: VLMAdapter | None = None,
    post_events: bool = True,
) -> list[dict[str, Any]]:
    adapter = adapter or MockVLMAdapter()
    engine = SafetyPolicyEngine(zones=source.zones)
    runtime = RuntimeMonitor()
    emitted: list[dict[str, Any]] = []

    for frame_context in sample_frames(source):
        runtime.frames_processed += 1
        metrics.increment("frames_processed_total")
        with Timer() as inference_timer:
            analysis = adapter.analyze_frame(frame_context)
        runtime.inference_latency_ms = inference_timer.elapsed_ms

        with Timer() as rule_timer:
            events = engine.evaluate(
                frame_context=frame_context,
                analysis=analysis,
                runtime_context=runtime.snapshot(),
            )
        runtime.rule_eval_latency_ms = rule_timer.elapsed_ms
        metrics.set_gauge("rule_eval_latency_ms", rule_timer.elapsed_ms)

        for event in events:
            payload = event.model_dump(mode="json")
            if post_events:
                with Timer() as post_timer:
                    post_event(backend, payload)
                runtime.backend_post_latency_ms = post_timer.elapsed_ms
                metrics.set_gauge("backend_post_latency_ms", post_timer.elapsed_ms)
            emitted.append(payload)
            log_event(
                logger,
                "safety_event_emitted",
                event_id=event.event_id,
                rule_id=event.rule_id,
                severity=event.severity,
                confidence=event.confidence,
            )
    return emitted


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run edge safety observability worker.")
    parser.add_argument("--source", required=True, help="Path to source JSON")
    parser.add_argument("--backend", required=True, help="Backend base URL")
    parser.add_argument(
        "--adapter",
        choices=["mock", "openai-compatible", "cosmos-reason2"],
        default="mock",
        help="Inference adapter to use",
    )
    parser.add_argument(
        "--adapter-endpoint",
        default="http://127.0.0.1:8000/v1",
        help="OpenAI-compatible base URL for real VLM/reasoning adapters",
    )
    parser.add_argument(
        "--model",
        default="nvidia/cosmos-reason2-2b",
        help="Model name passed to the OpenAI-compatible endpoint",
    )
    parser.add_argument(
        "--api-key-env",
        default="COSMOS_API_KEY",
        help="Environment variable containing adapter API key, if required",
    )
    parser.add_argument("--no-post", action="store_true", help="Generate events without posting")
    return parser


def main() -> None:
    configure_logging()
    args = build_parser().parse_args()
    source = load_source(args.source)
    adapter = build_adapter(args)
    events = run_worker(
        source=source,
        backend=args.backend,
        adapter=adapter,
        post_events=not args.no_post,
    )
    log_event(logger, "worker_complete", events=len(events), camera_id=source.camera_id)


if __name__ == "__main__":
    main()
