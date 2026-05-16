# physical-ai-safety-reviewer

Use when touching robotics, perception, sensors, unsafe actions, human override, incident review,
evidence chains, or fail-safe logic.

## Safety Rules

- Do not treat model output as ground truth.
- Preserve evidence, timestamps, source identity, runtime state, model version, and rule version.
- Degraded runtime should lower confidence or require human review.
- Human override and incident review paths must be explicit before production claims.

## Checks

- Validate rule behavior with deterministic tests.
- Confirm false positives and uncertainty are represented.
- Document missing sensor, camera, or real-world validation.

## Output

Report safety assumptions, evidence coverage, missing validation, and escalation gaps.

