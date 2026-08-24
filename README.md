# ForesightG1

Predictive whole-body control for Unitree G1 on dynamic, time-varying terrain.

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

The zero-action smoke test successfully loads and simulates the G1 on GPU.
The robot falls and resets continuously under the zero-action agent, which is expected because no locomotion/stabilization policy is active yet.

## Project Direction

ForesightG1 will investigate predictive whole-body control for humanoid traversal of dynamic terrain, including moving and time-varying platforms.

The long-term objective is to compare reactive control against predictive control that reasons about future terrain states and action feasibility before execution.
