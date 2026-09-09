# Obinna Edeh

**AI systems engineer for edge, robotics, and operational evidence.** I build systems that run on Jetson-class hardware and robots, then measure them and keep the measurement next to the claim.

Open to leading AI systems work where teams need measurable edge, robotics, and operational evidence. Case studies and dashboards: [obiedeh.github.io](https://obiedeh.github.io/).

Every number below names its date, the hardware it was measured on, and the committed file it comes from. Anything without a measurement is labelled a scaffold.

---

## Flagship Systems

| System | What it is | Measured evidence | Status |
|---|---|---|---|
| **Physical AI on Jetson** · [repository](https://github.com/obiedeh/physical-ai-jetson-robotics) · [case study](https://obiedeh.github.io/physical-ai-jetson-robotics.html) | Robot manipulation program: Isaac Sim training and evaluation, GR00T inference on Jetson AGX Thor, Orin NX host for a ROS 2 arm, correction ledger | GR00T TensorRT **101.6 ms median, 9.8 Hz**, Jetson AGX Thor 128GB at 120 W, 2026-08-20 (`reports/thor_trt_benchmark/thor_trt_benchmark.json`). Ludo executor **35/36 turns**, Isaac Sim on RTX 5090, runs 2026-08-19, aggregate 2026-08-20 (`reports/ludo_stats_frozen/`). Orin NX fp16 matmul **9.72 TFLOPS p50**, 2026-08-20 (`reports/jetson/yahboom_day_one/day_one_smoke.json`). GR00T eval01 corrected from an apparent 1/20 to **0/20** (`reports/ludo_groot17_eval01/session_summary_corrected.json`). | Measured. Public repository from a clean tree, 2026-09-09; vendor assets are staged locally, never committed. |
| **Physical AI Safety Observability** · [repository](https://github.com/obiedeh/physical-ai-safety-observability) · [case study](https://obiedeh.github.io/physical-ai-safety-observability.html) · [evidence page](https://obiedeh.github.io/physical-ai-safety-observability/reports/index.html) | Runtime safety layer: structured safety events, policy engine for PPE, zones and proximity, operator review API, telemetry hooks | Jetson AGX Thor, 2026-09-09: worker sustains **28.6 frames/s** at 30 fps pacing with rule evaluation under 1 ms p95 (mock model, `reports/thor/mock_30fps_no_post.json`). Cosmos-Reason2-2B via vLLM on device: **p50 4.35 s, p95 12.85 s per frame**, 66.6 W board power (`reports/thor/cosmos2b_video_60.json`). | Measured for runtime overhead and inference cost only. Detection quality unmeasured, no ground truth yet. |
| **Jetson Edge AI Security** · [repository](https://github.com/obiedeh/jetson-edge-ai-security) · [evidence pages](https://obiedeh.github.io/jetson-edge-ai-security/reports/index.html) | Defensive edge telemetry runtime: replayable events, anomaly alerts, operator review, ONNX detector and forecaster, Thor deployment package | Inference on Jetson AGX Thor, CPU provider, 2026-09-08: detector **p95 0.0237 ms at 1000 events/s**, **0.36 GB** peak RSS (`reports/thor_benchmark.json`). Default onnxruntime thread pool drew **54.1 W**; one thread with spinning disabled drew **24.3 W**, equal to idle, with zero pacing misses (`reports/thor_benchmark_threads.json`). | Measured for inference only. Detection quality is on a synthetic fixture; capture path unmeasured. |

The combined edge-security and telemetry case study is at [obiedeh.github.io/jetson-edge-ai-security.html](https://obiedeh.github.io/jetson-edge-ai-security.html).

## How I Work

- A run is not evidence until its artifact is committed with provenance: device, date, inputs, session options.
- Corrections stay in the record. The GR00T retraction and the Thor template fix are documented, not overwritten.
- Simulation, synthetic fixtures, and mock adapters are labelled as such everywhere they appear.
- Humans stay in the loop: every alert, safety event, and policy output is advisory and operator-reviewed.

## Credibility Boundary

This portfolio separates implemented workflows, runnable scaffolds, mock validation paths, planned hardware benchmarks, and future deployment targets.

Mock adapters, synthetic inputs, and planned Jetson paths are useful engineering scaffolds, but they are not claimed as real-world deployment proof until evidence artifacts exist.

## Technical Stack

**Physical AI and robotics:** ROS 2, MoveIt 2, Isaac Sim, Isaac Lab, OpenUSD, GR00T
**Edge inference:** NVIDIA Jetson AGX Thor and Orin NX, TensorRT, ONNX Runtime, CUDA
**Runtime observability:** telemetry pipelines, safety events, tegrastats power and thermal capture, evidence artifacts with hashes
**ML:** Python, PyTorch, scikit-learn, ONNX export with parity checks
**Operational AI:** retrieval-grounded copilots, guardrails, human review
**Data and infrastructure:** SQL, Spark, Airflow, dbt, Docker, Kubernetes, CI/CD, AWS, Azure, GCP, Terraform
**Infrastructure and operational reliability:** network and radio telemetry, KPI forecasting, link-level signal analysis, capacity planning

## Supporting Systems

Smaller systems that prove one discipline each. One line, no further investment planned unless a measurement is added.

| System | What it proves | Data source | Status |
|---|---|---|---|
| urban-edge-vision-analytics | Edge vision event pipeline with operator review | Synthetic frames and a mock detector | Scaffold. Repository private. |
| [private-5g-edge-telemetry](https://github.com/obiedeh/private-5g-edge-telemetry) · [dashboard](https://obiedeh.github.io/private-5g-edge-telemetry/reports/dashboard.html) | Capacity planning under an edge-inference latency budget, with deterministic reports | Simulated factory telemetry | Simulation evidence, no hardware |
| [wireless-link-intelligence-system](https://github.com/obiedeh/wireless-link-intelligence-system) · [dashboard](https://obiedeh.github.io/wireless-link-intelligence-system/reports/dashboard.html) | Signal-processing correctness and link estimation with a classical baseline first | Deterministic QPSK simulator and synthetic link conditions | Simulation evidence, no hardware |
| [ai-ran-kpi-forecasting](https://github.com/obiedeh/ai-ran-kpi-forecasting) · [portal](https://obiedeh.github.io/ai-ran-kpi-forecasting/reports/index.html) | KPI forecasting pattern with no-leakage temporal splits and advisory policy output | 48-row synthetic sample, plus the public Telecom Italia Milan grid (62 days, 3 squares) | Measured: inference cost on Jetson AGX Thor, CPU provider, 2026-09-09 (`reports/thor_benchmark/thor_benchmark.json`); forecast accuracy on public data, 2026-09-09, over two hold-out windows: all three models beat a naive last-value baseline in ordinary weeks, the baseline beats them over the holidays (`reports/forecast_examples/telecom_italia_mi/summary.json`, `..._preholiday/summary.json`) |
| [ai-phy-neural-receiver-benchmark](https://github.com/obiedeh/ai-phy-neural-receiver-benchmark) · [dashboard](https://obiedeh.github.io/ai-phy-neural-receiver-benchmark/reports/dashboard.html) | Neural versus classical receiver comparison with the boundary of the advantage reported | Sionna-modelled link simulation | Simulation evidence, no hardware |

Hiring-manager mapping: [HIRING_MANAGER_BRIEF.md](HIRING_MANAGER_BRIEF.md).

## Contact

- Email: [obiedeh@gmail.com](mailto:obiedeh@gmail.com)
- LinkedIn: [linkedin.com/in/obinna-edeh-206306137](https://linkedin.com/in/obinna-edeh-206306137)
- Site: [obiedeh.github.io](https://obiedeh.github.io/)
