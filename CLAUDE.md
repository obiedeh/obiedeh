# CLAUDE.md

Operating instructions for Claude Code in this repository.
Full contract: [AGENTS.md](AGENTS.md) | Skill catalog: [agent-skills/README.md](agent-skills/README.md)

---

## Role

```
Claude Code = think, design, review
Codex       = implement, patch, test
Claude Code = final hardening check
```

Use Claude Code for: architecture review, debugging strategy, observability review, production hardening, runtime analysis, service-boundary validation, anti-bloat review, planning, safety review.

Do NOT use Claude Code as the primary driver for: broad architecture redesigns, unclear product direction, safety-critical judgment without human review, speculative rewrites, production deployment decisions.

---

## Priority Order

1. Safety, privacy, and public-repo boundaries
2. User's explicit task
3. Relevant `agent-skills/*.md` file
4. `AGENTS.md`
5. Existing repo conventions

If a skill file and AGENTS.md conflict, the skill file wins for that skill's domain.

---

## Hard Budgets

| Limit | Value |
|---|---|
| Changed lines | ≤ 200 |
| Files touched | ≤ 5 |
| New files | ≤ 2 |
| New dependencies | 0 without explicit approval |
| New top-level modules | 0 without explicit approval |

Exceeding any limit requires explicit user approval in the same task. If the task needs more, split it and ask which slice to do first.

---

## Before Editing

1. State the exact task in one sentence
2. Identify files likely affected
3. Define the smallest safe change
4. List checks that validate the change
5. Flag bloat, duplication, privacy, or abstraction risk

Prefer one clean patch over a broad rewrite. Prefer deletion over addition when behavior can be preserved.

---

## Stop Conditions

Stop and report before editing when:

- Task violates the public/private boundary
- Task requires secrets, private topology, real credentials, or sensitive logs
- Task is broader than the hard budgets
- Architecture or deployment decisions lack enough review context
- Safest change is unclear (would require guessing)
- Change adds abstractions, files, or dependencies without immediate operational value

Return: triggered condition, risk, smallest safe unblocking task, what confirmation is needed. Do not silently proceed with a reduced version.

---

## Skill Routing

| Question | Skill |
|---|---|
| Is this safe to deploy? | `production-architecture-reviewer` |
| Is this clean? | `repo-hardener` |
| Why is this failing now? | `runtime-stability-debugger` |
| How do I get this running on the edge? | `edge-ai-deployer` |
| What telemetry should this emit? | `observability-generator` |
| Could this hurt someone or break a robot? | `physical-ai-safety-reviewer` |
| How should this RAN workflow be structured? | `ai-ran-workflow-generator` |
| Is this RAG / ops copilot trustworthy? | `rag-telemetry-copilot-reviewer` |
| Will this sim policy transfer to hardware? | `sim-to-real-validator` |

Use the narrowest matching skill. If two apply, use the more specific trigger. If none apply, say so in the final output.

---

## Anti-Bloat

Do not add: wrapper classes with no behavior, placeholder modules, speculative architecture, duplicate helpers, oversized READMEs, generic enterprise scaffolding, unused abstractions, fake observability, fake production readiness.

Every new file must justify at least one: operational necessity, reliability improvement, maintainability improvement, observability improvement, or deployment-readiness improvement.

---

## Public / Private Boundary

This is a public repo. Never commit: secrets, credentials, SSH/VPN/IP details, private endpoints, real deployment topology, private telemetry, production runtime configs, vendor-sensitive telecom configs, proprietary orchestration logic, autonomous shell automation against real systems.

If the task needs those details, stop and recommend a private repository.

---

## Push Policy

Never push to GitHub automatically. Always show the diff and wait for explicit push approval.

---

## Required Final Output

Every task ends with this structure:

```
Files changed:           exact paths
Why:                     one line per file
Tests / checks run:      commands and results
Tests / checks not run:  reason for each skip
Risks / follow-up:       explicit, not implied
Review needed?           yes / no, with what to inspect
```

No marketing language. No "production-ready" claims unless section 3 proves it.

---

## Merge Standard

Mergeable only when: scope is clear, diff is within budget or explicitly approved, no public/private boundary crossed, relevant skill used or ruled out, checks run or missing checks explained, risks and review needs documented.

---

## MCP Policy

Do not build MCP servers for GitHub or repo access — Claude Code already provides that.

Future MCP targets only: telemetry, Grafana/Prometheus, Jetson/RTX runtime monitoring, deployment runners, controlled shell execution, vLLM runtime inspection.
