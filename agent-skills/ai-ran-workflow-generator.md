# ai-ran-workflow-generator

Use when touching telecom workflows, commissioning, KPI analysis, rollback, CLI validation,
network observability, or AI-RAN logic.

## Workflow Rules

- Keep public workflows generic and non-sensitive.
- Separate recommendation from execution.
- Include validation, rollback, and operator approval points.
- Avoid vendor-sensitive configs, private topology, or live operational SOPs.

## Checks

- Inputs, outputs, and failure modes are explicit.
- KPI thresholds are examples unless validated for a deployment.
- Rollback paths are described without private automation details.

## Output

Return a compact workflow with prerequisites, checks, rollback, and missing private details.

