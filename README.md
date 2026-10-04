# Obinna Edeh

**I take Physical AI and edge systems from the bench to the field, and I build them myself.**

My career has been getting new hardware to perform at scale: leading engineering teams, field crews and equipment vendors through deployments where the spec sheet promised one thing and the site delivered another. Closing that gap before the build is how I work, and it is the same gap Physical AI faces now. A model that passes a benchmark or a simulation still has to hold up on the robot, at the camera's real frame rate, inside real power and thermal limits.

At [EmbodiedEdge Labs](https://embodiededge.ai), my Physical AI lab, I work that gap on my own hardware: a Jetson AGX Thor, a Jetson Orin NX on a ROS 2 rover, a 6-DoF arm and an RTX 5090 bench. Every result below names its date, the hardware it was measured on and the committed file it comes from.

Open to senior engineering leadership roles in Physical AI, robotics and edge AI, where getting systems field-ready is the job.

---

## Flagship Systems

| System | The field question | What the evidence shows | Status |
|---|---|---|---|
| **Bench2Field** · [repository](https://github.com/obiedeh/bench2field) · [case study](https://obiedeh.github.io/bench2field.html) · [report](https://obiedeh.github.io/bench2field/case_studies/01_perception_detector/report/index.html) | How much of a model optimization survives contact with the robot? | On the rover's Jetson Orin NX at the camera's real 26 Hz, YOLOX-s alone answers in **26.9 ms**, inside the 33.3 ms deadline. The full frame takes **47.8 ms**, so the robot would drop about one frame in eight. A model-only benchmark says GO. (2026-10-02, `case_studies/01_perception_detector/PHASE1_FINDINGS.md`) | v1.0.1 released: measure and diagnose. v2 (optimize and close the gap) in progress. |
| **Physical AI on Jetson** · [repository](https://github.com/obiedeh/physical-ai-jetson-robotics) · [case study](https://obiedeh.github.io/physical-ai-jetson-robotics.html) | Can a learned policy run on the robot's own compute, and what does the robot cost to run? | GR00T through TensorRT at **101.6 ms median (9.8 Hz)** on Jetson AGX Thor. Isaac Sim Ludo executor **35/36 turns**. A GR00T evaluation corrected from 1/20 to **0/20** and kept on record. Rover SLAM stack measured on the Orin at **11.1 W** board input. (2026-08-20 to 2026-09-16, `reports/`) | Active. Autonomous real-arm pick and place not yet established ([NOT_CLAIMED](https://github.com/obiedeh/physical-ai-jetson-robotics/blob/main/reports/NOT_CLAIMED.md)). |
| **Physical AI Safety Observability** · [repository](https://github.com/obiedeh/physical-ai-safety-observability) · [case study](https://obiedeh.github.io/physical-ai-safety-observability.html) · [showcase](https://obiedeh.github.io/physical-ai-safety-observability/docs/showcase/) | What does it cost to put a vision-language model in the safety loop on the edge device? | Pipeline sustains **28.6 frames/s** with rule evaluation under 1 ms p95 (mock model). Cosmos-Reason2-2B on device: **4.35 s p50 per frame at 66.6 W**. Constrained-decoding guard proven against the live model server. (Jetson AGX Thor, 2026-09-09 and 2026-10-02, `reports/thor/`) | Functional. Live-camera validation in progress; detection quality not yet measured. |
| **Urban Edge Vision Analytics** · [repository](https://github.com/obiedeh/urban-edge-vision-analytics) · [showcase](https://obiedeh.github.io/urban-edge-vision-analytics/docs/showcase/) | Can one edge box watch several street cameras and turn what it sees into events an operator can review? | Runs end to end on live cameras: stop-sign, two-gate speed and moving-object packs per camera, video decoupled from inference, model chosen per host (Cosmos-Reason2-2B on Thor, Gemma 4 on the RTX 5090). | Functional. Latency, power and pack accuracy measurements pending. |

## How I Lead the Work

- **Validate against the site, not the spec sheet.** Every result is measured on the hardware it will run on, at the rate it will run at.
- **Set the budget before the test.** Deadlines, power and accuracy limits are written down first, never fitted to the result.
- **No claim without its evidence.** A run counts once its artifact is committed with device, date and inputs.
- **Corrections stay in the record.** The GR00T retraction and the Bench2Field v1.0.1 correction are documented, not overwritten.
- **Humans stay in the loop.** Every alert, safety event and recommendation is advisory and operator-reviewed.

## Credibility Boundary

Each project labels what is measured, implemented but unmeasured, scaffolded or planned. Simulation, synthetic fixtures and mock adapters are labelled wherever they appear, and none of them is presented as deployment proof.

## Technical Stack

**Physical AI and robotics:** ROS 2, MoveIt 2, Isaac Sim, Isaac Lab, OpenUSD, GR00T, LeRobot, SLAM
**Edge inference:** NVIDIA Jetson AGX Thor and Orin NX, TensorRT, ONNX Runtime, CUDA, vLLM, Nsight
**Runtime observability:** telemetry pipelines, safety events, tegrastats power and thermal capture, evidence artifacts with hashes
**ML:** Python, PyTorch, scikit-learn, ONNX export with parity checks, vision-language models (Cosmos-Reason2, Gemma)
**Operational AI:** retrieval-grounded copilots, guardrails, evaluation harnesses, human review
**Infrastructure:** Docker, Kubernetes, CI/CD, AWS (Bedrock, App Runner), Azure, GCP, Terraform, SQL, Spark, Airflow

## Supporting Systems

| System | What it proves | Status |
|---|---|---|
| [Jetson Edge AI Security](https://github.com/obiedeh/jetson-edge-ai-security) · [case study](https://obiedeh.github.io/jetson-edge-ai-security.html) · [evidence](https://obiedeh.github.io/jetson-edge-ai-security/reports/index.html) | Defensive edge telemetry with operator-reviewed alerts. Traced a 54.1 W runtime power draw on Jetson AGX Thor to the default inference thread pool; running one thread with spinning disabled brought it to 24.3 W, equal to idle, with zero missed deadlines. | Measured for inference and power. Detection quality on a synthetic fixture. |
| [Field Commissioning Copilot](https://github.com/obiedeh/field-commissioning-das-copilot) · [evidence](https://obiedeh.github.io/field-commissioning-das-copilot/docs/showcase/) | Field commissioning for distributed antenna system (DAS) networks: a retrieval-grounded copilot that answers from OEM documentation, says when its sources don't cover a question, and flags any unverified number before field use. Zero unsourced numbers shown as fact and 0.906 faithfulness in a 65-case evaluation. | Measured locally. Cloud deployment planned. |
| Wireless signal AI: neural receiver ([repo](https://github.com/obiedeh/ai-phy-neural-receiver-benchmark) · [evidence](https://obiedeh.github.io/ai-phy-neural-receiver-benchmark/reports/index.html)) · KPI forecasting ([repo](https://github.com/obiedeh/ai-ran-kpi-forecasting) · [evidence](https://obiedeh.github.io/ai-ran-kpi-forecasting/reports/index.html)) · link intelligence ([repo](https://github.com/obiedeh/wireless-link-intelligence-system) · [evidence](https://obiedeh.github.io/wireless-link-intelligence-system/reports/dashboard.html)) · edge telemetry ([repo](https://github.com/obiedeh/private-5g-edge-telemetry) · [evidence](https://obiedeh.github.io/private-5g-edge-telemetry/reports/index.html)) | Learned models measured against classical baselines, with the limits of the advantage reported. The KPI forecaster beats a naive baseline in ordinary weeks and loses to it over holidays, and says so. | Simulation and public-data evidence. |

## Contact

- Email: [obiedeh@gmail.com](mailto:obiedeh@gmail.com)
- LinkedIn: [linkedin.com/in/obinna-edeh-206306137](https://linkedin.com/in/obinna-edeh-206306137)
- Lab: [embodiededge.ai](https://embodiededge.ai)
- Site: [obiedeh.github.io](https://obiedeh.github.io/)
