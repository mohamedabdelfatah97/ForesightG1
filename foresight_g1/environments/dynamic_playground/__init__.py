"""ForesightG1 Dynamic Playground task registration."""

from mjlab.tasks.registry import register_mjlab_task

from src.tasks.velocity.config.g1.rl_cfg import unitree_g1_ppo_runner_cfg
from src.tasks.velocity.rl import VelocityOnPolicyRunner

from .env_cfg import foresight_g1_dynamic_env_cfg


register_mjlab_task(
    task_id="ForesightG1-Dynamic-v1",
    env_cfg=foresight_g1_dynamic_env_cfg(),
    play_env_cfg=foresight_g1_dynamic_env_cfg(play=True),
    rl_cfg=unitree_g1_ppo_runner_cfg(),
    runner_cls=VelocityOnPolicyRunner,
)
