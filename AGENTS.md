# AGENTS.md

Repository-level operating contract for AI coding agents: Claude Code, Codex, Cursor, Aider, OpenCode, and similar tools.

This file controls how agents work in this repository. It is intentionally strict. The goal is small, reviewable, validated changes, not impressive-looking repo growth.

For the skill catalog and shared engineering standards, see `agent-skills/README.md`. Trigger descriptions in `agent-skills/*.md` frontmatter are authoritative. If this file and a skill file conflict, the skill file wins for that skill's domain.

---

## Priority order

When instructions conflict, follow this order:

1. Safety, privacy, and public-repo boundaries
2. User's explicit task
3. Relevant `agent-skills/*.md` file
4. This `AGENTS.md`
5. Existing repo conventions

Never use lower-priority instructions to bypass higher-priority constraints.

---

## Required final output

Every task ends with this exact structure:

1. **Files changed** — exact paths
2. **Why** — one line per file
3. **Tests / checks run** — commands or checks with results
4. **Tests / checks not run** — reason for each skipped check
5. **Risks or follow-up** — explicit, not implied
6. **Review needed?** — yes / no, with what to inspect

No marketing language. No "production-ready" claims unless the checks in section 3 prove it.

### Example

```text
Files changed:
- src/telemetry/exporter.py
- tests/telemetry/test_exporter.py

Why:
- exporter.py: added retry on transient HTTP 5xx
- test_exporter.py: covered the retry path

Tests / checks run:
- pytest tests/telemetry — 14 passed
- ruff check src/telemetry — clean

Tests / checks not run:
- end-to-end against staging exporter — no staging access from this session

Risks / follow-up:
- retry budget is fixed at 3 attempts; consider making it configurable

Review needed? Yes — verify retry budget and retryable exception filter.
```

---

## Agent scope

Use agents for:

- focused implementation patches
- tests
- scaffolding inside an existing pattern
- migrations and mechanical refactors
- dependency cleanup
- formatting and lint fixes
- applying an approved plan

Do **not** use agents as the primary driver for:

- broad architecture redesigns
- unclear product direction
- safety-critical judgment without human review
- speculative rewrites
- large autonomous refactors across unrelated modules
- production deployment decisions
- MCP servers, connectors, or external tools without explicit instruction

---

## Stop conditions

Stop before editing when any condition below is true:

- The task violates the public/private boundary.
- The requested change requires secrets, private topology, real credentials, or sensitive logs.
- The task is broader than the hard budgets below.
- The task asks for architecture or deployment decisions without enough review context.
- The safest change is unclear and would require guessing.
- The change would add abstractions, files, or dependencies without immediate operational value.

When stopping, return:

1. The triggered stop condition
2. Why continuing would be risky
3. The smallest safe task that would unblock progress
4. What confirmation or missing input is needed

Do not silently proceed with a reduced version of the task.

---

## Before editing

Before changing files, identify:

1. The exact task in one sentence
2. The files likely affected
3. The smallest safe change
4. The checks that validate the change
5. Any bloat, duplication, privacy, or abstraction risk

Prefer one clean patch over a broad rewrite. Prefer deletion over addition when behavior can be preserved.

---

## Hard budgets

These are limits, not suggestions. Exceeding them requires explicit user approval in the same task.

- **Patch size:** ≤ 200 changed lines
- **Files touched:** ≤ 5 files
- **New files:** ≤ 2
- **New dependencies:** 0 without approval
- **New top-level modules/packages:** 0 without approval

If the task needs more, split it and ask which slice to do first.

---

## Anti-bloat rules

Do not add:

- wrapper classes that add no behavior
- placeholder modules
- speculative future architecture
- duplicate helper functions
- oversized READMEs
- generic enterprise scaffolding
- unused abstractions
- fake observability
- fake production readiness
- files that only restate existing docs

Every new file must justify at least one:

- **Operational necessity:** something breaks without it
- **Reliability improvement:** measurable failure reduction
- **Maintainability improvement:** concrete simplification
- **Observability improvement:** named consumer and signal
- **Deployment-readiness improvement:** named target and validation path

If none apply, do not create the file.

---

## Token and context discipline

Prefer:

- patches over full rewrites
- exact file paths over "the codebase"
- checklists over essays
- tests over explanations
- task-specific context over repo-wide context

Avoid:

- dumping full files unless necessary
- repeating unchanged code
- architecture essays
- verbose comments
- duplicate documentation
- generic best-practice filler
- redundant tool calls

Read only what is needed. Edit only what is necessary. Validate what changed.

---

## Skill usage

The skill catalog lives in `agent-skills/README.md`. Individual skills live in `agent-skills/*.md`.

Rules:

- Use the narrowest matching skill.
- If two skills apply, use the one with the more specific trigger.
- If no skill applies, say so in the final output and keep the patch minimal.
- Skill files add constraints; they do not override hard budgets, anti-bloat rules, or public/private boundaries.

---

## Public vs private boundary

This is a public repository. It may contain methodology, standards, generic checklists, and non-sensitive engineering patterns.

Never add:

- secrets or credentials
- SSH, VPN, or internal IP details
- private endpoints or hostnames
- real deployment topology
- private telemetry or logs
- production runtime configs
- vendor-sensitive telecom configs
- proprietary orchestration logic
- autonomous shell automation against real systems
- hidden routing prompts
- sensitive operational SOPs

If the task needs those details, stop and recommend a private repository. Do not partially redact and commit.

---

## Testing and validation

Run the narrowest relevant check:

- logic change → unit tests
- structural change → lint/type checks
- service change → smoke test
- deployment/config change → config validation
- docs change → link/path check

If a check cannot run, list it under **Tests / checks not run** with the reason. Missing validation must be visible, not buried.

---

## Recommended workflows

### Single-agent

A capable agent handles design, implementation, and self-review for small scoped tasks. It must still follow the before-editing checklist, hard budgets, and final output format.

### Two-agent: design / implement

Use this when architecture, safety, or production-readiness risk is meaningful.

- **Design agent:** plan, affected files, tests, risks, acceptance criteria
- **Implementation agent:** minimal patch, validation, final output
- **Design agent:** final review before merge

Default split when both are available:

```text
Claude Code = think, design, review
Codex = implement, patch, test
Claude Code = final hardening check
```

---

## Merge standard

A change is mergeable only when:

- scope is clear
- diff is within budget or explicitly approved
- no public/private boundary is crossed
- relevant skill was used or explicitly ruled out
- checks were run or missing checks are explained
- risks and review needs are documented

If these are not true, the work is not done.

---

## Version

AGENTS.md — last reviewed against the Agent Skills spec on 2026-05-16.
