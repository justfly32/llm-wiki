---
source_url: https://arxiv.org/abs/2606.02577v1
ingested: 2026-06-03
type: paper
arxiv_id: 2606.02577v1
authors: Junjie Ye, Rong Xue, Basile Van Hoorick
published: 2026-06-01
categories: cs.RO, cs.CV
---

# RoboDream: Compositional World Models for Scalable Robot Data Synthesis

**Authors:** Junjie Ye, Rong Xue, Basile Van Hoorick
**Published:** 2026-06-01
**arXiv:** https://arxiv.org/abs/2606.02577v1
**Categories:** cs.RO, cs.CV

## Abstract

Scaling robot learning requires large-scale, diverse demonstrations, yet real-world data collection via teleoperation remains prohibitively expensive and time-consuming. While video diffusion models offer a promising avenue for data scaling, existing generative approaches are often limited to superficial visual augmentation, or suffer from embodiment hallucinations that yield physically infeasible motions. We present a generalizable embodiment-centric world model that achieves scalable data generation by synthesizing photorealistic demonstrations with novel objects, in novel scenes, and from novel viewpoints. Our approach anchors generation to rendered robot motion while conditioning on explicit scene and object priors, effectively decoupling trajectory execution from environment synthesis. This formulation has the potential to unlock two powerful data scaling capabilities: (1) retrieval and rebirth, which repurposes existing trajectories into entirely new contexts without new motion data; and (2) prop-free teleoperation, where operators manipulate empty air and the model hallucinates the target objects and scene afterwards, eliminating reset time. We demonstrate with real-world experiments that our generated data consistently improves downstream policy performance and significantly reduces real-world data requirements across diverse manipulation tasks.
