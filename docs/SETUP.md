# Development Setup

## Environment

Conda environment:

`foresight_mjlab`

Python stack:

- Python 3.11.15
- PyTorch 2.13.0+cu130
- MuJoCo 3.6.0
- MuJoCo-Warp 3.5.0
- mjlab 1.2.0
- Warp 1.12.1
- SciPy 1.16.3
- Unitree RL mjlab 0.0.1

## Upstream Unitree Baseline

External repository:

`~/foresight_external/unitree_rl_mjlab`

Pinned upstream commit:

`1425b15f73bd4095f0df53709d7c389c3eb9e790`

The upstream Unitree repository is intentionally kept outside the ForesightG1 repository.

## Environment Isolation

ROS 2 and other workspaces may be sourced globally on the host.

Before running ForesightG1 / mjlab commands:

```bash
conda activate foresight_mjlab
unset PYTHONPATH
export PYTHONNOUSERSITE=1
