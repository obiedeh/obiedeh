# observability-generator

Use when adding logs, metrics, traces, health checks, queue telemetry, alerts, dashboards, or
runtime visibility.

## Observability Rules

- Metrics must map to operational questions.
- Logs should be structured JSON with stable fields.
- Health and readiness should test dependencies, not only process liveness.
- Avoid fake dashboards or metrics that are never updated.

## Required Signals

- Request or event count.
- Error count or failure reason.
- Latency distribution or p95/p99.
- Queue depth or backlog where work is asynchronous.
- Runtime resource pressure for edge workloads.

## Output

List added signals, where they are emitted, and what remains blind.

