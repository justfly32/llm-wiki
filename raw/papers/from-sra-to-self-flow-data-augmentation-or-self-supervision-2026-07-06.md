---
source_url: https://arxiv.org/abs/2607.02508v1
ingested: 2026-07-06
type: paper
arxiv_id: 2607.02508v1
authors: Dengyang Jiang, Mengmeng Wang, Harry Yang
published: 2026-07-02
categories: cs.CV
---

# From SRA to Self-Flow: Data Augmentation or Self-Supervision?

**Authors:** Dengyang Jiang, Mengmeng Wang, Harry Yang
**Published:** 2026-07-02
**arXiv:** https://arxiv.org/abs/2607.02508v1
**Categories:** cs.CV

## Abstract

Representation alignment has become an effective way to accelerate diffusion transformer training and improve generation quality. Recent self-alignment methods, such as SRA and Self-Flow, further remove the dependency on external pretrained encoders by constructing alignment within the diffusion model itself. However, the mechanism behind the improvement from SRA to Self-Flow, dual-time scheduling, remains under-examined: Self-Flow attributes its gain to interactions between tokens at different noise levels, where cleaner tokens help infer noisier ones. In this work, we revisit this explanation and ask whether the gain instead comes from data augmentation along the noise dimension. To disentangle these factors, we introduce Attention Separation, which preserves the same dual-timestep input as Self-Flow while blocking attention between tokens assigned to different noise levels. Surprisingly, removing such interaction does not degrade performance and can even improve it, suggesting that the improvement from SRA to Self-Flow mainly comes from data augmentation. Furthermore,We show that Attention Separation itself provides an augmentation effect by splitting a single image into multiple effective training parts to expand the training data. Based on these observations, we combine self-representation alignment with dual-timestep and attention-separation augmentation, and demonstrate the effectiveness of this design on ImageNet.
