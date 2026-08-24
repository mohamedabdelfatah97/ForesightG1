"""Dynamic Playground event functions."""

import math
from typing import TYPE_CHECKING

import torch

from mjlab.managers.scene_entity_config import SceneEntityCfg

if TYPE_CHECKING:
    from mjlab.envs import ManagerBasedRlEnv


def move_platform_sinusoidal(
    env: "ManagerBasedRlEnv",
    env_ids: torch.Tensor | None,
    asset_cfg: SceneEntityCfg,
    center: tuple[float, float, float],
    amplitude_m: float,
    period_s: float,
) -> None:
    """Move a mocap platform sinusoidally along the world Y axis."""

    del env_ids

    platform = env.scene[asset_cfg.name]

    # Simulation time in seconds.
    t = env.common_step_counter * env.step_dt

    # y(t) = center_y + A * sin(2*pi*t/T)
    y_offset = amplitude_m * math.sin(
        2.0 * math.pi * t / period_s
    )

    # Mocap pose format:
    # [x, y, z, qw, qx, qy, qz]
    pose = torch.zeros(
        (env.num_envs, 7),
        device=env.device,
        dtype=torch.float32,
    )

    # Start from each vectorized environment's world origin.
    pose[:, :3] = env.scene.env_origins

    pose[:, 0] += center[0]
    pose[:, 1] += center[1] + y_offset
    pose[:, 2] += center[2]

    # Identity quaternion.
    pose[:, 3] = 1.0

    platform.write_mocap_pose_to_sim(pose)
