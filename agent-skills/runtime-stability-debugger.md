# runtime-stability-debugger

Use when touching inference runtime, GPU behavior, queues, streaming, latency, memory pressure,
repeated-run instability, or long-lived workers.

## Review Focus

- Queue depth, dropped work, latency p95/p99, and memory pressure are observable.
- Backpressure, timeout, retry, and shutdown behavior are explicit.
- Runtime degradation changes confidence or operator review state when safety matters.
- GPU/accelerator assumptions are configurable and not hidden in code.

## Checks

- Run narrow smoke tests for repeated execution.
- Inspect logs and metrics for failure-path visibility.
- Document missing hardware validation when no GPU/edge target was tested.

## Output

Summarize runtime risk, measured behavior, and the next smallest stability fix.

