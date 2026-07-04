---
title: PointDiT: Pixel-Space Diffusion for Monocular Geometry Estimation
created: 2026-07-05
updated: 2026-07-05
type: concept
tags: [research, multimodal, diffusion]
sources: [raw/papers/pointdit-pixel-space-diffusion-for-monocular-geometry-estim-2026-07-05.md]
confidence: medium
---

# PointDiT: Pixel-Space Diffusion for Monocular Geometry Estimation

> 📄 원문: [PointDiT: Pixel-Space Diffusion for Monocular Geometry Estimation](https://arxiv.org/abs/2607.02515v1)
> ✍️ 저자: Haofei Xu, Rundi Wu, Philipp Henzler
> 📅 발행: 2026-07-02
> 🏷️ 카테고리: cs.CV

## 요약

State-of-the-art single-image 3D reconstruction methods often rely on complex hybrid architectures and loss functions, or compress geometry into latent spaces in order to leverage pre-trained latent diffusion models. In this work, we show that such architectural overhead and intricate loss formulations are unnecessary. We introduce a minimalist pixel-space Diffusion Transformer, built on a plain ViT, that operates directly on raw 3D point map patches and is conditioned on image tokens from a pre-trained DINOv3. Unlike existing latent diffusion approaches, we train our diffusion backbone entirely from scratch, eliminating the need for point map tokenizers. Despite its simplicity, our approach surpasses complex latent-based diffusion models while remaining significantly simpler than hybrid alternatives. Notably, it produces sharper geometric structure and is more robust in highly ambiguous regions, such as transparent objects.

## 원문 영어

<details>
<summary>원문 보기</summary>

State-of-the-art single-image 3D reconstruction methods often rely on complex hybrid architectures and loss functions, or compress geometry into latent spaces in order to leverage pre-trained latent diffusion models. In this work, we show that such architectural overhead and intricate loss formulations are unnecessary. We introduce a minimalist pixel-space Diffusion Transformer, built on a plain ViT, that operates directly on raw 3D point map patches and is conditioned on image tokens from a pre

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2607.02515v1)
