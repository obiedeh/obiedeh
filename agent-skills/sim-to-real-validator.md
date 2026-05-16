---
name: sim-to-real-validator
description: Validate sim-to-real transfer for robotics and physical AI systems built on Isaac Sim, Isaac Lab, OpenUSD, MuJoCo, or Gazebo. Use when a policy or model trained in simulation is being moved to a physical robot, when a sim-to-real gap is suspected as the cause of a regression, when domain randomization is being designed, when a new simulation asset is being added, or when the user asks whether a sim result will hold on hardware. Use this skill before any first run on real hardware.
---

# Sim-to-Real Validator

Simulation results don't transfer for free. This skill exists to catch the predictable failures before a policy or perception model meets physical hardware, and to structure the first hardware run so failures are recoverable and informative.

The default failure mode is "it worked in sim, then it didn't on the robot, and we don't know why." This skill structures the validation so the answer is recoverable.

## When to invoke

- A policy trained in Isaac Lab, Isaac Sim, MuJoCo, or Gazebo is being prepared for hardware.
- A perception model trained on synthetic or rendered data is being moved to real sensors.
- A sim-to-real regression has appeared and the cause is unclear.
- Domain randomization is being scoped or extended.
- New simulation assets, lighting, or physics are being added.
- The user asks whether sim results will hold on real hardware.

## Pre-deployment checklist

Each item produces one of: **OK**, **needs work**, or **blocker**, with a one-line piece of evidence.

### 1. Distribution match

- Real sensor specs (resolution, FOV, frame rate, noise model) are documented and matched in sim.
- Real actuator limits (torque, velocity, latency) are documented and matched in sim.
- Real environment ranges (lighting, surface friction, object mass) are bounded and represented.
- Items outside the simulated range are explicitly listed as out-of-distribution.

### 2. Domain randomization

- Randomization parameters are listed with min, max, and distribution.
- Each parameter is justified — what real-world variation it covers.
- Randomization ranges include the real-world target *and* a buffer beyond it.
- A "no randomization" baseline policy exists for comparison.

### 3. Latency and control rate

- Sim control rate matches hardware control rate, or the gap is documented and tested.
- Sensor-to-action latency in sim approximates the hardware path (driver, transport, inference, actuation).
- Policy is tested in sim with realistic latency injected, not zero latency.

### 4. Observation alignment

- Real sensor pipeline (cameras, IMU, lidar) is reproduced in sim, not approximated.
- Coordinate frames match between sim and hardware, with a written check.
- Sensor noise, dropout, and calibration error are modeled in sim.

### 5. Safety envelope

- A bounded test region exists for first hardware runs.
- A kill switch is wired, tested, and reachable by a human in less than one second.
- Failure modes are enumerated with the expected hardware response.
- A rollback procedure exists if the policy needs to be reverted mid-run.

### 6. Evidence

- The sim-side results being claimed for transfer are reproducible (seed pinned, version tagged).
- The simulation scene, randomization config, and policy weights are versioned together.
- A held-out sim eval exists that the policy has not been tuned against.

## First hardware run protocol

When the checklist passes, structure the first real run as four stages. Do not skip stages. If stage N fails, return to sim with the observation — do not move to stage N+1 with a tweak.

1. **Static check** — robot powered, sensors streaming, no actuation. Confirm the observation pipeline matches sim in shape and units.
2. **Open-loop replay** — replay a known-good trajectory from sim with the policy disabled. Confirm hardware tracks command.
3. **Constrained closed-loop** — policy enabled, bounded workspace, low speed, human override armed.
4. **Nominal closed-loop** — policy at intended operating envelope, with logging at full rate.

## Output format

Return a structured readiness report:

```text
Sim-to-Real Readiness: <system or policy name>

Checklist results:
- Distribution match: <OK | needs work | blocker> + evidence
- Domain randomization: <...>
- Latency and control rate: <...>
- Observation alignment: <...>
- Safety envelope: <...>
- Evidence: <...>

Go / No-Go for first hardware run: <Go | No-Go>

If No-Go, smallest unblocking change:
- <one item>

Pre-run protocol stage where issues are most likely:
- <stage number and reason>
```

## Anti-patterns this skill flags

- "We added domain randomization" with no listed ranges.
- "It works in sim" as the only evidence for a hardware run.
- Sim-side latency of zero.
- Camera FOV mismatch between sim and hardware.
- Kill switch not tested on the actual hardware setup.
- Policy weights versioned separately from the sim scene that trained them.
- Tuning randomization until the policy passes, rather than fixing the policy.

## What this skill does not do

- It does not run the simulation or the hardware test for you.
- It does not generate domain randomization configs — it reviews them.
- It does not replace `physical-ai-safety-reviewer` for the surrounding safety case. That skill covers autonomy-level safety review; this one covers transfer-validity review.
