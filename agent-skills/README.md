# Agent Skills

Portable engineering skills for Claude Code and Codex workflows across AI infrastructure, edge AI, telecom, AI-RAN, robotics, observability, and production-hardening systems.

These are not generic AI agents.

They are compact operational SOPs that encode engineering judgment while minimizing token waste, architecture drift, and AI-generated repo bloat.

---

# Operating Model

```text
Claude Code = think, design, review
Codex = implement, patch, test
Claude Code = final production-readiness check
```

## Use Claude Code For

- architecture review
- repo understanding
- debugging strategy
- observability review
- production hardening
- runtime analysis
- service-boundary validation
- anti-bloat review
- planning and decomposition
- safety review

## Use Codex For

- implementation
- patches
- scaffolding
- migrations
- repetitive edits
- test generation
- mechanical refactors
- executing clearly-defined plans

---

# Skill Routing

| If the question is... | Use |
| --- | --- |
| Is this safe to deploy? | `production-architecture-reviewer` |
| Is this clean? | `repo-hardener` |
| Why is this failing now? | `runtime-stability-debugger` |
| How do I get this running on the edge? | `edge-ai-deployer` |
| What telemetry should this emit? | `observability-generator` |
| Could this hurt someone or break a robot? | `physical-ai-safety-reviewer` |
| How should this RAN workflow be structured? | `ai-ran-workflow-generator` |
| Is this RAG / ops copilot trustworthy? | `rag-telemetry-copilot-reviewer` |
| Will this sim policy transfer to hardware? | `sim-to-real-validator` |

---

# Public vs Private Skill Strategy

## Public Skills

Public skills should contain:

- engineering philosophy
- operational methodology
- architecture standards
- anti-bloat rules
- deployment checklists
- observability expectations
- runtime review checklists
- generic AI infrastructure guidance
- generic telecom workflows
- generic robotics safety review patterns

Public skills should NOT contain:

- secrets
- infrastructure topology
- deployment credentials
- SSH/IP details
- internal endpoints
- private telemetry
- vendor-sensitive configs
- production runtime tuning
- proprietary orchestration logic
- autonomous shell automation
- private SOPs

---

# Current Public Skills

| Skill | Purpose |
|---|---|
| [`production-architecture-reviewer`](production-architecture-reviewer.md) | Detect fake scalability, abstraction creep, weak service boundaries, poor deployment realism, and missing observability |
| [`repo-hardener`](repo-hardener.md) | Remove dead code, reduce duplication, simplify modules, prevent AI-generated repo sprawl |
| [`runtime-stability-debugger`](runtime-stability-debugger.md) | Review GPU pressure, KV cache growth, queue depth, streaming degradation, repeated-run instability |
| [`edge-ai-deployer`](edge-ai-deployer.md) | Validate Jetson, RTX, CUDA, Docker, TensorRT, vLLM, runtime health, deployment readiness |
| [`observability-generator`](observability-generator.md) | Enforce metrics, traces, structured logging, health checks, queue telemetry, runtime visibility |
| [`physical-ai-safety-reviewer`](physical-ai-safety-reviewer.md) | Review robotics safety, unsafe actions, sensor confidence, fail-safe logic, escalation paths |
| [`ai-ran-workflow-generator`](ai-ran-workflow-generator.md) | Generate telecom commissioning flows, KPI workflows, rollback logic, operational SOP structure |
| [`rag-telemetry-copilot-reviewer`](rag-telemetry-copilot-reviewer.md) | Review RAG pipelines, telemetry copilots, retrieval quality, and hallucination risk |
| [`sim-to-real-validator`](sim-to-real-validator.md) | Validate sim-to-real transfer assumptions, latency realism, and robotics deployment readiness |

---

# Recommended Private Skill Areas

These should eventually live in a separate PRIVATE repo.

```text
obi-private-agent-skills/
├── deployment/
├── runtime-ops/
├── robotics-runtime/
├── telemetry/
├── shell-automation/
├── ai-ran-internal/
├── production-workflows/
├── secret-integrations/
└── internal-mcp/
```

## Keep Private

- deployment automation
- real runtime configs
- production topology
- Jetson/RTX internal infrastructure
- Grafana/Prometheus internals
- live telemetry routing
- vendor-specific telecom workflows
- real commissioning procedures
- production rollback systems
- robotics runtime tuning
- sensor thresholds
- experimental orchestration systems
- autonomous execution logic
- hidden routing prompts
- internal shell automation

---

# Global Engineering Rules

Every skill must enforce:

- production realism
- minimal abstractions
- observability by default
- runtime stability
- testability
- clear service boundaries
- no placeholder modules
- no unnecessary wrappers
- no speculative future architecture
- no bloated documentation
- no duplicated instructions

Every new module or file must justify at least one of:

- operational necessity
- reliability improvement
- maintainability improvement
- observability improvement
- deployment-readiness improvement

If it does not justify one of those, do not create it.

---

# Token Efficiency Rules

Prefer:

- concise markdown
- short checklists
- patch-focused guidance
- small task-specific context
- structured operational summaries
- references instead of repeated content

Avoid:

- giant READMEs
- repeated architecture explanations
- dumping full files unnecessarily
- verbose comments
- generic best-practice filler
- unnecessary MCP/tool sprawl
- speculative abstractions

Treat tokens like infrastructure resources:

- VRAM
- cache
- bandwidth
- latency budget

Not free memory.

---

# MCP Policy

Do NOT build MCP servers for GitHub or repo access.

Claude Code and Codex already provide repository access.

Future MCP usage should only target:

- telemetry
- Grafana/Prometheus
- Jetson/RTX runtime monitoring
- deployment runners
- controlled shell execution
- vLLM runtime inspection
- observability systems

Avoid unnecessary MCP complexity.

---

# Recommended Workflow

1. Claude Code selects the correct skill and produces the architecture/review plan.
2. Codex executes patches, scaffolding, migrations, and tests.
3. Claude Code performs final hardening, observability review, and production-readiness validation.
4. Merge only after the relevant acceptance checks pass.
