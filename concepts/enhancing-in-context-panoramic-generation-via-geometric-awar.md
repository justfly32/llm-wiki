---
title: Enhancing In-context Panoramic Generation via Geometric-aware Pretraining
created: 2026-07-13
updated: 2026-07-13
type: concept
tags: [research, multimodal]
sources: [raw/papers/enhancing-in-context-panoramic-generation-via-geometric-awar-2026-07-13.md]
confidence: medium
---

# Enhancing In-context Panoramic Generation via Geometric-aware Pretraining

> 📄 원문: [Enhancing In-context Panoramic Generation via Geometric-aware Pretraining](https://arxiv.org/abs/2607.08765v1)
> ✍️ 저자: Haoran Feng, Ruiyang Zhang, Longyi Zhang
> 📅 발행: 2026-07-09
> 🏷️ 카테고리: cs.CV

## 요약

In this work, we present Canvas360, a two-stage framework for in-context panoramic generation that combines geometry-aware pretraining with downstream task-specific fine-tuning. To address the lack of large-scale, high-quality training data tailored to in-context panoramic tasks, we propose Canvas360Dataset, a collection of 1M high-quality paired panoramic samples for style transfer, inpainting, outpainting, and editing, enabling effective supervision across diverse in-context generation scenarios. On the modeling side, Canvas360 enhances text-to-panorama generation through parallel depth generation, velocity circular padding, and similarity loss regularization, enabling the model to learn geometry-aware representations, capture object distortion details, and improve geometric consistency and global coherence. Furthermore, empowered by strong panoramic priors, Canvas360 enables a unified in-context panoramic generation framework that supports diverse downstream tasks via token-level concatenation, surpassing prior methods in both task coverage and modeling flexibility. Extensive experiments show that Canvas360 improves panoramic image fidelity, achieving particularly strong performance on the panorama-specific FAED metric and competitive or leading results across the reported quantitative evaluations. More information can be found on our project page: https://zry000.github.io/Canvas360/

## 원문 영어

<details>
<summary>원문 보기</summary>

In this work, we present Canvas360, a two-stage framework for in-context panoramic generation that combines geometry-aware pretraining with downstream task-specific fine-tuning. To address the lack of large-scale, high-quality training data tailored to in-context panoramic tasks, we propose Canvas360Dataset, a collection of 1M high-quality paired panoramic samples for style transfer, inpainting, outpainting, and editing, enabling effective supervision across diverse in-context generation scenari

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2607.08765v1)
