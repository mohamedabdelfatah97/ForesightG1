"""Play the ForesightG1 Dynamic Playground with a trained locomotion policy."""

from dataclasses import asdict
from pathlib import Path

import torch

from mjlab.envs import ManagerBasedRlEnv
from mjlab.rl import MjlabOnPolicyRunner, RslRlVecEnvWrapper
from mjlab.tasks.registry import load_env_cfg, load_rl_cfg, load_runner_cls
from mjlab.utils.torch import configure_torch_backends
from mjlab.viewer import NativeMujocoViewer

# Importing this module registers ForesightG1-Dynamic-v1.
import foresight_g1.environments.dynamic_playground  # noqa: F401


TASK_ID = "ForesightG1-Dynamic-v1"

PROJECT_ROOT = Path(__file__).resolve().parents[2]
CHECKPOINT = (
    PROJECT_ROOT
    / "checkpoints"
    / "g1_flat_10k_20260824"
    / "model_9999.pt"
)


def main() -> None:
    configure_torch_backends()

    device = "cuda:0" if torch.cuda.is_available() else "cpu"

    if not CHECKPOINT.exists():
        raise FileNotFoundError(f"Checkpoint not found: {CHECKPOINT}")

    env_cfg = load_env_cfg(TASK_ID, play=True)
    agent_cfg = load_rl_cfg(TASK_ID)

    env_cfg.scene.num_envs = 1

    print(f"[INFO] Task: {TASK_ID}")
    print(f"[INFO] Device: {device}")
    print(f"[INFO] Checkpoint: {CHECKPOINT}")

    env = ManagerBasedRlEnv(
        cfg=env_cfg,
        device=device,
        render_mode=None,
    )

    env = RslRlVecEnvWrapper(
        env,
        clip_actions=agent_cfg.clip_actions,
    )

    runner_cls = load_runner_cls(TASK_ID) or MjlabOnPolicyRunner
    runner = runner_cls(env, asdict(agent_cfg), device=device)

    runner.load(
        str(CHECKPOINT),
        load_cfg={"actor": True},
        strict=True,
        map_location=device,
    )

    policy = runner.get_inference_policy(device=device)

    NativeMujocoViewer(env, policy).run()

    env.close()


if __name__ == "__main__":
    main()
