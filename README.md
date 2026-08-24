# ForesightG1

Predictive whole-body control for Unitree G1 on dynamic, time-varying terrain.

## Project Goal

ForesightG1 investigates whether a humanoid can use predictive reasoning about both its own future motion and the future state of the environment before committing to an action.

The long-term objective is to compare:

- reactive whole-body control
- predictive whole-body control
- failure-aware action selection and recovery

in dynamic environments containing moving, time-varying, and eventually partially unstable terrain.

The initial benchmark direction is humanoid traversal across dynamic platforms, where successful control may require timing, waiting, replanning, jumping, recovery, and eventually whole-body contact.

---

## Current Status

### Milestone 0 — Simulation Baseline

Validated the official Unitree G1 environment using MuJoCo / mjlab with GPU-accelerated MuJoCo-Warp.

Current baseline:

- Unitree G1 29-DoF
- mjlab 1.2.0
- MuJoCo 3.6.0
- MuJoCo-Warp 3.5.0
- Warp 1.12.1
- PyTorch 2.13.0 + CUDA 13.0

Verified:

- Unitree G1 model loads successfully
- MuJoCo-Warp initializes on GPU
- physics simulation runs successfully
- native MuJoCo viewer works
- environment managers initialize correctly
- command, action, observation, reward, and termination pipelines are functional

A zero-action smoke test was used for the initial validation.

The robot falls and resets continuously under the zero-action agent, which is expected because no locomotion or stabilization policy is active.

---

### Milestone 1 — PPO Training Pipeline

Validated the complete reinforcement-learning training pipeline for the official `Unitree-G1-Flat` task.

The smoke test used:

- 256 parallel G1 environments
- GPU-accelerated simulation
- PPO training
- 5 learning iterations
- 30,720 total simulation steps
- TensorBoard logging
- checkpoint saving
- automatic ONNX export
- checkpoint loading and replay

The test successfully produced:

```text
model_0.pt
model_1.pt
model_2.pt
model_3.pt
model_4.pt
policy.onnx