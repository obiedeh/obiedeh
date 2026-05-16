from dataclasses import dataclass, field
from time import perf_counter

from events.schemas import RuntimeContext, RuntimeStatus


@dataclass
class RuntimeMonitor:
    frames_processed: int = 0
    frames_dropped: int = 0
    queue_depth: int = 0
    inference_latency_ms: float = 0.0
    rule_eval_latency_ms: float = 0.0
    backend_post_latency_ms: float = 0.0
    gpu_memory_pressure: float = 0.0
    thermal_pressure: float = 0.0
    notes: list[str] = field(default_factory=list)

    def snapshot(self) -> RuntimeContext:
        status = RuntimeStatus.NOMINAL
        notes = list(self.notes)
        if (
            self.frames_dropped > 0
            or self.queue_depth > 5
            or self.gpu_memory_pressure >= 0.75
            or self.thermal_pressure >= 0.75
        ):
            status = RuntimeStatus.DEGRADED
        if self.gpu_memory_pressure >= 0.9 or self.thermal_pressure >= 0.9:
            status = RuntimeStatus.CRITICAL
        return RuntimeContext(
            frames_processed=self.frames_processed,
            latency_ms=self.inference_latency_ms + self.rule_eval_latency_ms,
            queue_depth=self.queue_depth,
            dropped_frames=self.frames_dropped,
            gpu_memory_pressure=self.gpu_memory_pressure,
            thermal_pressure=self.thermal_pressure,
            runtime_status=status,
            notes=notes,
        )


class Timer:
    def __enter__(self) -> "Timer":
        self._start = perf_counter()
        self.elapsed_ms = 0.0
        return self

    def __exit__(self, *_args: object) -> None:
        self.elapsed_ms = (perf_counter() - self._start) * 1000
