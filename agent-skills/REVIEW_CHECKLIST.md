# Review Checklist

Use this checklist when reviewing work from another agent before merge.

The goal is to catch:

- scope drift
- repo bloat
- fake production readiness
- weak validation
- architectural decay
- public/private boundary violations

---

# Scope Review

- Was the original task completed?
- Did the implementation stay within approved files?
- Did the patch stay within budget?
- Were unrelated changes avoided?
- Were adjacent problems left as follow-up instead of silently fixed?

---

# Architecture Review

- Were service boundaries preserved?
- Were unnecessary abstractions avoided?
- Were wrapper classes avoided unless justified?
- Was speculative architecture avoided?
- Does the implementation match existing repo patterns?

---

# Validation Review

- Were the required checks run?
- Are skipped checks explained?
- Are validation claims supported by evidence?
- Are test results visible?
- Does the documentation match actual behavior?

---

# Anti-Bloat Review

Reject if the patch introduces:

- placeholder modules
- fake observability
- fake deployment readiness
- duplicated helpers
- oversized documentation
- dead code
- unused abstractions
- unnecessary dependencies

---

# Public / Private Boundary Review

Reject if the patch exposes:

- credentials
- internal IPs
- private endpoints
- sensitive logs
- production topology
- vendor-sensitive configs
- hidden prompts
- private operational SOPs

---

# Evidence Review

Strong claims require evidence.

Examples:

| Claim | Required evidence |
| --- | --- |
| Faster inference | latency or throughput measurement |
| Stable runtime | repeated-run validation |
| Production-ready | deployment validation + observability |
| Improved retrieval | eval result or benchmark |
| Better robotics transfer | sim-to-real evidence |

Reject vague claims without measurable support.

---

# Runtime and Operational Review

Review where applicable:

- p95/p99 latency
- queue depth
- retry behavior
- memory pressure
- GPU utilization
- KV cache growth
- degraded-runtime behavior
- health checks
- rollback paths

---

# Final Merge Decision

## Approve only if

- scope stayed controlled
- validation is visible
- evidence supports claims
- no unnecessary complexity was added
- public/private boundaries remain intact
- follow-up items are documented

## Request changes if

- the patch drifted beyond scope
- validation is weak or missing
- evidence is unsupported
- repo complexity increased without operational value
- the implementation would be difficult to maintain
