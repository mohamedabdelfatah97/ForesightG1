"""ForesightG1 dynamic playground environment."""

import mujoco

from mjlab.entity import EntityCfg
from mjlab.envs import ManagerBasedRlEnvCfg
from mjlab.managers.event_manager import EventTermCfg
from mjlab.managers.scene_entity_config import SceneEntityCfg

from src.tasks.velocity.config.g1.env_cfgs import unitree_g1_flat_env_cfg

from .events import move_platform_sinusoidal


def get_platform_spec() -> mujoco.MjSpec:
    """Create the ForesightG1 moving platform."""

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
    """Create ForesightG1 Dynamic Playground."""

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

    # Move the platform sinusoidally along the world Y axis.
    #
    # Center:    (2.0, 0.0, 0.05)
    # Amplitude: +/- 0.75 m
    # Period:    4 seconds
    cfg.events["move_platform"] = EventTermCfg(
        func=move_platform_sinusoidal,
        mode="step",
        params={
            "asset_cfg": SceneEntityCfg("moving_platform"),
            "center": (2.0, 0.0, 0.05),
            "amplitude_m": 0.75,
            "period_s": 4.0,
        },
    )

    return cfg