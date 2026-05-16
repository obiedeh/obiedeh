from collections import defaultdict
from threading import Lock

from events.schemas import SafetyEvent, Severity


class MetricsRegistry:
    def __init__(self) -> None:
        self._lock = Lock()
        self.counters: defaultdict[str, float] = defaultdict(float)
        self.gauges: defaultdict[str, float] = defaultdict(float)

    def increment(self, name: str, value: float = 1.0) -> None:
        with self._lock:
            self.counters[name] += value

    def set_gauge(self, name: str, value: float) -> None:
        with self._lock:
            self.gauges[name] = value

    def observe_event(self, event: SafetyEvent) -> None:
        self.increment("events_total")
        if event.severity == Severity.CRITICAL:
            self.increment("critical_events_total")
        self.set_gauge("frames_processed_total", event.runtime_context.frames_processed)
        self.set_gauge("inference_latency_ms", event.runtime_context.latency_ms)
        self.set_gauge("frames_dropped_total", event.runtime_context.dropped_frames)

    def render_prometheus(self) -> str:
        required = {
            "events_total": self.counters.get("events_total", 0.0),
            "critical_events_total": self.counters.get("critical_events_total", 0.0),
            "frames_processed_total": self.gauges.get("frames_processed_total", 0.0),
            "frames_dropped_total": self.gauges.get("frames_dropped_total", 0.0),
            "inference_latency_ms": self.gauges.get("inference_latency_ms", 0.0),
            "rule_eval_latency_ms": self.gauges.get("rule_eval_latency_ms", 0.0),
            "backend_post_latency_ms": self.gauges.get("backend_post_latency_ms", 0.0),
        }
        lines = [f"{name} {value}" for name, value in sorted(required.items())]
        return "\n".join(lines) + "\n"


metrics = MetricsRegistry()
