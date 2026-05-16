# AGENTS.md

Repository-level operating instructions for AI coding agents (Claude Code, Codex, Cursor, Aider, OpenCode, and others).

These rules are agent-neutral. Runtime-specific workflow patterns are at the bottom under "Recommended workflows."

For the skill catalog and shared engineering standards, see `agent-skills/README.md`. Trigger descriptions in each `agent-skills/*.md` frontmatter are authoritative. If this file and a skill file disagree, the skill file wins.

---

## Output format (required for every task)

At the end of every task, the agent returns:

1. **Files changed** — exact paths
2. **Why** — one line per file
3. **Tests / checks run** — list with results
4. **Tests / checks not run** — list with reason
5. **Risks or follow-up** — explicit, not implied
6. **Review needed?** — yes / no, with what to look at

No marketing language. No "production-ready" claims unless validation in (3) supports it.

### Worked example

```text
Files changed:
- src/telemetry/exporter.py
- tests/telemetry/test_exporter.py

Why:
- exporter.py: added retry on transient HTTP 5xx
- test_exporter.py: covered new retry path

Tests / checks run:
- pytest tests/telemetry — 14 passed
- ruff check src/telemetry — clean

Tests / checks not run:
- end-to-end against staging exporter (no staging access from this session)

Risks / follow-up:
- retry budget hardcoded at 3 attempts; consider making configurable

Review needed? Yes — verify retry budget choice and the exception filter on retry.
```

---

## Agent role and scope

Use the agent for:

- focused implementation patches
- writing tests
- scaffolding within an existing pattern
- migrations and mechanical refactors
- dependency cleanup
- formatting and lint fixes
- applying plans the user has already approved

Do **not** use the agent as primary driver for:

- broad architecture redesigns
- unclear product direction
- safety-critical judgment without explicit human review
- speculative rewrites
- large autonomous refactors across unrelated modules
- production deployment decisions
- adding MCP servers, connectors, or external tools without explicit instruction

### Stop conditions

When the agent detects it has been pulled into a "do not" task, it must:

1. Stop before writing code or files.
2. State in plain text which "do not" condition triggered.
3. Propose the smallest scoped task that would unblock progress.
4. Wait for explicit user confirmation before continuing.

The agent does not silently proceed with a reduced version of the request.

---

## Execution discipline

Before editing, the agent identifies in writing:

1. The exact task in one sentence.
2. The files likely affected (list, not "the codebase").
3. The smallest safe change.
4. The tests or checks that validate the change.
5. Any risk of bloat, duplication, or unnecessary abstraction.

Prefer small, reviewable patches over broad rewrites.

### Hard budgets

These are constraints, not guidelines. Exceeding them requires explicit user authorization in the same turn:

- **Patch size:** ≤ 200 lines changed per task
- **Files touched:** ≤ 5 files per task
- **New files created:** ≤ 2 per task
- **New dependencies:** 0 without approval
- **New top-level modules or packages:** 0 without approval

When a task genuinely requires more, the agent splits it and asks which slice to do first.

---

## Anti-bloat rules

Do not create:

- wrapper classes that add no behavior
- placeholder modules
- speculative future architecture
- duplicate helper functions
- oversized READMEs
- generic enterprise scaffolding
- unused abstractions
- fake observability (log lines that nothing reads, metrics never plotted)
- fake production readiness (Dockerfiles for services that don't deploy, CI for code that doesn't run)
- files that only restate existing docs

Every new file must justify at least one of:

- operational necessity (something breaks without it)
- reliability improvement (measurable)
- maintainability improvement (concrete)
- observability improvement (with a named consumer)
- deployment-readiness improvement (with a named target)

If it does not justify one, do not create it.

---

## Token and context efficiency

Prefer:

- patches over full rewrites
- exact file references over "the codebase"
- checklists over long prose
- tests over explanations
- task-specific context over project-wide context

Avoid:

- dumping full files unless required
- repeating unchanged code
- architecture essays
- verbose comments
- duplicate documentation
- generic best-practice filler
- redundant tool calls (read once, edit precisely)

When in doubt, read less and ask.

---

## Skill usage

The skill catalog lives in `agent-skills/README.md` and each `agent-skills/*.md` file.

Skill selection rules:

- Use the skill that most narrowly matches the task. If two skills could fire, pick the one with the more specific trigger.
- If no skill applies, keep the patch minimal and state in the output format why no skill was needed.
- Skills compose with these AGENTS.md rules; they do not override the hard budgets or anti-bloat rules.

---

## Public vs private boundaries

This is a public repository. It contains methodology, standards, generic checklists, and non-sensitive engineering patterns only.

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

If a task requires those details, stop and recommend moving the work to a private repository. Do not redact and partially commit.

---

## Testing and validation

For code changes, run or propose the narrowest relevant validation:

- unit tests for logic changes
- lint and type checks for structural changes
- smoke tests for service changes
- config validation for deployment changes
- doc link and path checks for docs changes

Do not claim production readiness unless the validation listed above was actually performed. If it was skipped, list it under "Tests / checks not run" with a reason.

---

## Recommended workflows (optional)

These are conventions, not requirements. Pick the one that matches the agents available in the session.

### Single-agent

A capable agent (Claude Code, Codex, Cursor) handles design and implementation in one session. Apply the execution discipline checklist on every task; the agent's own review pass replaces a second agent.

### Two-agent (design / implement)

When two agents are used, a common split is:

- **Design agent:** produces a plan, identifies affected files, drafts tests, calls out risks.
- **Implementation agent:** applies the plan as a minimal patch, runs tests, returns the output format above.

The design agent performs the final review before changes land.

---

## Version

AGENTS.md — last reviewed against the Agent Skills spec on 2026-05-16. Update this date when this file changes.
