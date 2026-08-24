"""ForesightG1 dynamic playground environment."""

import mujoco

from mjlab.entity import EntityCfg
from mjlab.envs import ManagerBasedRlEnvCfg

from src.tasks.velocity.config.g1.env_cfgs import unitree_g1_flat_env_cfg


def get_platform_spec() -> mujoco.MjSpec:
    """Create the first ForesightG1 platform."""

    spec = mujoco.MjSpec()

    body = spec.worldbody.add_body(
        name="moving_platform",
        mocap=True,
    )

    body.add_geom(
        name="moving_platform_geom",
        type=mujoco.mjtGeom.mjGEOM_BOX,

        # MuJoCo box sizes are HALF-extents:
        # 1.5 m x 1.5 m x 0.10 m platform.
        size=(0.75, 0.75, 0.05),

        rgba=(0.20, 0.45, 0.85, 1.0),
    )

    return spec


def foresight_g1_dynamic_env_cfg(
    play: bool = False,
) -> ManagerBasedRlEnvCfg:
    """Create ForesightG1 Dynamic Playground v1."""

    # Reuse the already validated Unitree G1 flat locomotion environment.
    cfg = unitree_g1_flat_env_cfg(play=play)

    platform_cfg = EntityCfg(
        init_state=EntityCfg.InitialStateCfg(
            # Center of platform.
            # Top surface is therefore z = 0.10 m.
            pos=(2.0, 0.0, 0.05),
        ),
        spec_fn=get_platform_spec,
    )

    # Preserve the existing G1 entity and add our platform.
    assert cfg.scene.entities is not None
    cfg.scene.entities = {
        **cfg.scene.entities,
        "moving_platform": platform_cfg,
    }

    return cfg
