---
source_url: https://arxiv.org/abs/2607.13033v1
ingested: 2026-07-16
type: paper
arxiv_id: 2607.13033v1
authors: Yu Fang, Wanxi Dong, Jiaqi Liu
published: 2026-07-14
categories: cs.RO
---

# DenseReward: Dense Reward Learning via Failure Synthesis for Robotic Manipulation

**Authors:** Yu Fang, Wanxi Dong, Jiaqi Liu
**Published:** 2026-07-14
**arXiv:** https://arxiv.org/abs/2607.13033v1
**Categories:** cs.RO

## Abstract

Reinforcement learning holds great promise for improving robot policies beyond the limits of imitation learning. However, its practical adoption remains bottlenecked by the lack of reliable vision-language reward models that provide dense and informative feedback. Two key challenges remain: acquiring diverse failure data at scale and obtaining fine-grained reward signals beyond sparse trajectory-level success labels. Collecting failure trajectories typically requires laborious human effort, while pseudo-failures constructed by relabeling successful demonstrations fail to capture the diverse physical failure modes that arise during robot execution. Meanwhile, existing reward models often predict sparse binary or trajectory-level rewards, which provide limited guidance for efficient policy optimization. We introduce DenseReward, a dense robotic reward model that addresses both challenges. To train DenseReward, we develop an automated failure data generation pipeline that synthesizes physically realistic failure trajectories in simulation without human labeling, covering diverse failure modes such as collisions, missed grasps, object drops, and recovery behaviors. DenseReward predicts dense frame-level reward scores from visual observations and language instructions, enabling fine-grained estimation of task progress throughout an episode. Experiments show that DenseReward outperforms general-purpose VLMs and existing robotic reward models in dense reward prediction across both simulated and real-world manipulation. We further demonstrate that DenseReward provides effective reward guidance for downstream model predictive control and reinforcement learning. We release the dataset, trained reward models, and evaluation suite to support the development of failure-aware dense reward modeling for robot learning.
