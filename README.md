# Obinna Edeh

**I lead Physical AI and edge systems from the bench to the field, and I stay hands-on.**

I've spent my career getting new hardware to perform at scale, leading engineering teams, field crews and vendors through nationwide deployments of hundreds of sites a year. One lesson held on every program: a spec sheet describes ideal conditions; the site shows what the hardware actually does.

Physical AI has the same gap. At [EmbodiedEdge Labs](https://embodiededge.ai), my Physical AI lab, I test robots and edge AI on my own hardware and measure what survives the move from benchmark to field.

Open to senior engineering leadership roles in Physical AI, robotics and edge AI.

---

## How I Lead the Work

- **Validate against the site, not the spec sheet.**
- **Set the budget before the test.**
- **No claim without its evidence.**
- **Corrections stay in the record.**
- **Humans stay in the loop.**

## Flagship Systems

Each project links its proof: the measured result, the hardware and the date.

| System | What the evidence shows | Status |
|---|---|---|
| **Bench2Field**<br>[Repository](https://github.com/obiedeh/bench2field)<br>**Proof:** [Case study](https://obiedeh.github.io/bench2field.html) · [Report](https://obiedeh.github.io/bench2field/case_studies/01_perception_detector/report/index.html) | **The benchmark said GO. The robot would drop frames.** On the rover's Jetson Orin NX the detector alone meets its 33.3 ms deadline (26.9 ms); the full frame takes 47.8 ms. | v1.0.1 released. v2 in progress. |
| **Physical AI on Jetson**<br>[Repository](https://github.com/obiedeh/physical-ai-jetson-robotics)<br>**Proof:** [Case study](https://obiedeh.github.io/physical-ai-jetson-robotics.html) | **A learned policy running on the robot's own compute.** GR00T through TensorRT at 9.8 Hz on Jetson AGX Thor, with a failed evaluation corrected and kept on the record. | Active. |
| **Physical AI Safety Observability**<br>[Repository](https://github.com/obiedeh/physical-ai-safety-observability)<br>**Proof:** [Case study](https://obiedeh.github.io/physical-ai-safety-observability.html) · [Showcase](https://obiedeh.github.io/physical-ai-safety-observability/docs/showcase/) | **Priced the safety loop before anyone depends on it.** A vision-language model on the device costs 4.35 s per frame at 66.6 W. | Functional. Live-camera validation in progress. |
| **Urban Edge Vision Analytics**<br>[Repository](https://github.com/obiedeh/urban-edge-vision-analytics)<br>**Proof:** [Showcase](https://obiedeh.github.io/urban-edge-vision-analytics/docs/showcase/) | **One edge box watching several street cameras.** Runs end to end on live cameras; measurement is next. | Functional. |

Simulation, synthetic data and mock adapters are labelled wherever they appear and never presented as deployment proof.

## Supporting Systems

| System | What the evidence shows | Status |
|---|---|---|
| **Jetson Edge AI Security**<br>[Repository](https://github.com/obiedeh/jetson-edge-ai-security)<br>**Proof:** [Case study](https://obiedeh.github.io/jetson-edge-ai-security.html) | **Found a power problem in a runtime setting, not the model.** Cut a 54.1 W draw on Jetson AGX Thor to idle, 24.3 W, with zero missed deadlines. | Measured. |
| **Field Commissioning Copilot**<br>Repository available on request<br>**Proof:** [Evidence page](https://obiedeh.github.io/field-commissioning-copilot/) | **Built so a technician never acts on an unsourced number.** Answers commissioning questions from manufacturer documentation and says when no source covers the question. | Measured locally. |
| **Wireless signal AI**<br>Four studies | Learned models measured against classical baselines, limits included:<br>▸ [Neural receiver](https://obiedeh.github.io/ai-phy-neural-receiver-benchmark/reports/index.html): wins at moderate SNR, falls behind above 15 dB<br>▸ [KPI forecasting](https://obiedeh.github.io/ai-ran-kpi-forecasting/reports/index.html): beats a naive baseline, except over holidays<br>▸ [Link intelligence](https://obiedeh.github.io/wireless-link-intelligence-system/reports/dashboard.html): neural channel estimation wins at low SNR<br>▸ [Edge telemetry](https://obiedeh.github.io/private-5g-edge-telemetry/reports/index.html): 100 AGVs fit a 20 ms control budget; 120 don't | Simulation and public data. |

## Technical Stack

- **Physical AI and robotics:** ROS 2, MoveIt 2, Isaac Sim, Isaac Lab, OpenUSD, GR00T, LeRobot, SLAM
- **Edge inference:** NVIDIA Jetson AGX Thor and Orin NX, TensorRT, ONNX Runtime, CUDA, vLLM
- **ML and operational AI:** Python, PyTorch, vision-language models, retrieval-grounded copilots, evaluation harnesses
- **Infrastructure:** Docker, Kubernetes, CI/CD, AWS, Azure, GCP

## Contact

[obiedeh@gmail.com](mailto:obiedeh@gmail.com) · [LinkedIn](https://linkedin.com/in/obinna-edeh-206306137) · [embodiededge.ai](https://embodiededge.ai) · [obiedeh.github.io](https://obiedeh.github.io/)
