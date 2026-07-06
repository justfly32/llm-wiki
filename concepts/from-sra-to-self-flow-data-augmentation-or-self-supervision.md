---
title: From SRA to Self-Flow: Data Augmentation or Self-Supervision?
created: 2026-07-06
updated: 2026-07-06
type: concept
tags: [research, programming, alignment, multimodal, diffusion]
sources: [raw/papers/from-sra-to-self-flow-data-augmentation-or-self-supervision-2026-07-06.md]
confidence: medium
---

# From SRA to Self-Flow: Data Augmentation or Self-Supervision?

> 📄 원문: [From SRA to Self-Flow: Data Augmentation or Self-Supervision?](https://arxiv.org/abs/2607.02508v1)
> ✍️ 저자: Dengyang Jiang, Mengmeng Wang, Harry Yang
> 📅 발행: 2026-07-02
> 🏷️ 카테고리: cs.CV

## 요약

Representation alignment has become an effective way to accelerate diffusion transformer training and improve generation quality. Recent self-alignment methods, such as SRA and Self-Flow, further remove the dependency on external pretrained encoders by constructing alignment within the diffusion model itself. However, the mechanism behind the improvement from SRA to Self-Flow, dual-time scheduling, remains under-examined: Self-Flow attributes its gain to interactions between tokens at different noise levels, where cleaner tokens help infer noisier ones. In this work, we revisit this explanation and ask whether the gain instead comes from data augmentation along the noise dimension. To disentangle these factors, we introduce Attention Separation, which preserves the same dual-timestep input as Self-Flow while blocking attention between tokens assigned to different noise levels. Surprisingly, removing such interaction does not degrade performance and can even improve it, suggesting that the improvement from SRA to Self-Flow mainly comes from data augmentation. Furthermore,We show that Attention Separation itself provides an augmentation effect by splitting a single image into multiple effective training parts to expand the training data. Based on these observations, we combine self-representation alignment with dual-timestep and attention-separation augmentation, and demonstrate the effectiveness of this design on ImageNet.

## 원문 영어

<details>
<summary>원문 보기</summary>

Representation alignment has become an effective way to accelerate diffusion transformer training and improve generation quality. Recent self-alignment methods, such as SRA and Self-Flow, further remove the dependency on external pretrained encoders by constructing alignment within the diffusion model itself. However, the mechanism behind the improvement from SRA to Self-Flow, dual-time scheduling, remains under-examined: Self-Flow attributes its gain to interactions between tokens at different 

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2607.02508v1)
