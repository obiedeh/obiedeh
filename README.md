# Obinna Edeh

**AI Architect and Systems Engineer focused on Physical AI, Edge Inference, Runtime Observability, and AI Infrastructure.**

I build AI systems where models meet physical infrastructure: robots, Jetson-class edge devices, runtime telemetry, safety-aware observability, and operator-assist intelligence workflows.

> Production AI is moving from isolated models to deployed systems that reason over physical infrastructure, edge compute, telemetry, and real-world operations.

I am currently pursuing an **M.S. in Applied Artificial Intelligence** at the University of San Diego, with a portfolio focused on Physical AI, edge runtime systems, operational observability, and infrastructure-aware AI deployment.

---

## Portfolio Thesis

My work is converging around one systems problem:

```text
physical infrastructure
+ edge inference
+ runtime telemetry
+ operational observability
+ retrieval-grounded intelligence
+ human-in-the-loop review
= deployable AI systems for real-world environments
```

The focus is not generic AI demos.

The focus is building AI systems that can be:
- benchmarked
- observed
- validated
- deployed
- audited
- operated safely under real runtime constraints

---

## Hiring-Manager Signal

This portfolio is built to prove:
- edge inference under real runtime constraints
- telemetry-driven validation and observability
- safety-aware Physical AI workflows
- reproducible engineering artifacts
- human-in-the-loop operational review
- infrastructure-aware AI deployment

---

## Portfolio Architecture

These projects define the core architecture of my portfolio: Physical AI systems, edge inference, runtime telemetry, safety observability, and Jetson/ROS 2 deployment workflows.

| Project | Focus | Signal |
|---|---|---|
| [physical-ai-jetson-robotics](https://github.com/obiedeh/physical-ai-jetson-robotics) | Jetson, ROS 2, robotics, sim-to-real | Flagship Physical AI system |
| [physical-ai-safety-observability](https://github.com/obiedeh/physical-ai-safety-observability) | Safety events, runtime telemetry, observability | Operational AI and safety layer |
| [jetson-edge-ai-security](https://github.com/obiedeh/jetson-edge-ai-security) | Edge telemetry, anomaly detection, Jetson constraints | Security and reliability at the edge |

## Applied Systems

These projects translate edge AI, telemetry, and analytics into operator-facing systems with reports, dashboards, and decision support.

| Project | Focus | Signal |
|---|---|---|
| [urban-edge-vision-analytics](https://github.com/obiedeh/urban-edge-vision-analytics) | Edge vision, traffic events, incident reporting | Applied computer vision system |
| [private-5g-data-pipeline](https://github.com/obiedeh/private-5g-data-pipeline) | Private 5G telemetry, data quality, reporting | Network operations data pipeline |
| [wireless-link-intelligence-system](https://github.com/obiedeh/wireless-link-intelligence-system) | RF link metrics, SINR/RSSI interpretation, dashboarding | Wireless engineering decision support |

## AI-RAN

These projects focus on AI-native wireless systems, 5G/6G link intelligence, neural receivers, and RAN operational analytics.

| Project | Focus | Signal |
|---|---|---|
| [neural-receiver-5g-nr](https://github.com/obiedeh/neural-receiver-5g-nr) | ML-assisted 5G NR receiver concepts | AI for physical-layer wireless systems |
| [ai-ran-kpi-forecasting](https://github.com/obiedeh/ai-ran-kpi-forecasting) | RAN KPI forecasting and operational intelligence | AI-RAN operations analytics |
| [private-5g-data-pipeline](https://github.com/obiedeh/private-5g-data-pipeline) | Private 5G telemetry foundation | Data layer for AI-native network operations |

## Pinned Repository Guidance

Recommended pin order:

1. [physical-ai-jetson-robotics](https://github.com/obiedeh/physical-ai-jetson-robotics)
2. [physical-ai-safety-observability](https://github.com/obiedeh/physical-ai-safety-observability)
3. [jetson-edge-ai-security](https://github.com/obiedeh/jetson-edge-ai-security)
4. [urban-edge-vision-analytics](https://github.com/obiedeh/urban-edge-vision-analytics)
5. [neural-receiver-5g-nr](https://github.com/obiedeh/neural-receiver-5g-nr)
6. [private-5g-data-pipeline](https://github.com/obiedeh/private-5g-data-pipeline)

Some projects live as standalone repositories; the [`projects/`](projects/) folder contains selected profile-linked notes and mirrors.

---

# Flagship Direction

## Physical AI Jetson Robotics

**Repository:** [physical-ai-jetson-robotics](https://github.com/obiedeh/physical-ai-jetson-robotics)

A Physical AI engineering platform connecting:

- ROS 2 robotics workflows
- Jetson edge inference
- OpenUSD / Isaac simulation
- robot telemetry and diagnostics
- sim-to-real validation
- safety-aware operations tooling
- retrieval-grounded diagnostics over logs, documentation, and runtime state
- AI-RAN / private 5G readiness concepts for robotics workloads

This repository is the center of gravity for the portfolio.

---

# Systems Relationship

```text
Physical infrastructure
  -> edge inference
  -> runtime telemetry
  -> operational observability
  -> retrieval-grounded intelligence
  -> operator-assist workflows
  -> telecom / wireless infrastructure support
```

The repositories are intentionally connected.

The broader thesis is that AI systems become operationally valuable only when connected to:
- telemetry
- runtime constraints
- evidence
- observability
- human review
- deployment workflows

---

# Current Evidence Focus

The current portfolio focus is strengthening the flagship proof stack:

1. [`physical-ai-jetson-robotics`](https://github.com/obiedeh/physical-ai-jetson-robotics) — Jetson/runtime evidence, telemetry artifacts, sim-to-real validation
2. [`physical-ai-safety-observability`](https://github.com/obiedeh/physical-ai-safety-observability) — safety event evidence, operator review flow, runtime metrics
3. [`jetson-edge-ai-security`](https://github.com/obiedeh/jetson-edge-ai-security) — defensive telemetry replay, alert artifacts, runtime reporting

Detailed maturity tracking is maintained in [`PORTFOLIO_EVIDENCE.md`](PORTFOLIO_EVIDENCE.md).

Hiring-manager mapping: [`HIRING_MANAGER_BRIEF.md`](HIRING_MANAGER_BRIEF.md).

---

# Evidence Standard

Each flagship project should include:
- reproducible run command
- tests / CI validation
- runtime metrics artifact
- architecture diagram
- sample input/output
- limitations
- next validation step

---

# Credibility Boundary

This portfolio separates:
- implemented workflows
- runnable scaffolds
- mock validation paths
- planned hardware benchmarks
- future deployment targets

Project READMEs should state limitations clearly. Mock adapters, synthetic inputs, and planned Jetson paths are useful engineering scaffolds, but they are not claimed as real-world deployment proof until committed evidence artifacts exist.

---

# Engineering Standards

This profile repository also includes agent operating standards for AI-assisted development:

- [`AGENTS.md`](AGENTS.md) — repository-level operating contract for Claude Code, Codex, Cursor, Aider, and similar coding agents
- [`agent-skills/`](agent-skills) — review skills for architecture, runtime stability, observability, edge deployment, AI-RAN workflows, RAG/telemetry copilots, and sim-to-real validation

The goal is to keep AI-assisted development disciplined:
- small patches
- explicit scope
- measurable validation
- operational realism
- evidence-backed claims
- strict public/private boundaries

---

# Technical Stack

**Edge AI:** NVIDIA Jetson, TensorRT, vLLM, ONNX, CUDA, VLM/LLM deployment  
**Robotics / Physical AI:** ROS 2, MoveIt 2, Isaac Sim, Isaac Lab, OpenUSD  
**AI / ML:** Python, PyTorch, scikit-learn, XGBoost, SHAP, MLflow  
**Operational AI / RAG:** retrieval-grounded copilots, local inference workflows, guardrails, human review  
**Data / Infrastructure:** SQL, Spark, Airflow, dbt, Docker, Kubernetes, CI/CD  
**Telecom / AI-RAN:** RAN telemetry, KPI forecasting, private 5G, wireless link analysis  
**Cloud / Distributed Systems:** AWS, Azure, GCP, Terraform

---

# Contact

- Email: [obiedeh@gmail.com](mailto:obiedeh@gmail.com)
- LinkedIn: [linkedin.com/in/obinna-edeh-206306137](https://linkedin.com/in/obinna-edeh-206306137)
- GitHub: [github.com/obiedeh](https://github.com/obiedeh)
