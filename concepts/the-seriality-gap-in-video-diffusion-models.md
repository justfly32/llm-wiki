---
title: The Seriality Gap in Video Diffusion Models
created: 2026-07-16
updated: 2026-07-16
type: concept
tags: [research, multimodal, agent, diffusion]
sources: [raw/papers/the-seriality-gap-in-video-diffusion-models-2026-07-16.md]
confidence: medium
---

# The Seriality Gap in Video Diffusion Models

> 📄 원문: [The Seriality Gap in Video Diffusion Models](https://arxiv.org/abs/2607.13031v1)
> ✍️ 저자: Jorge Diaz Chao, Konpat Preechakul, Yuxi Liu
> 📅 발행: 2026-07-14
> 🏷️ 카테고리: cs.LG, cs.CV

## 요약

When one ball strikes another, then another, video models should predict the consequences of each bounce. In controlled experiments on multi-ball hard-sphere dynamics, we find that the performance of standard bidirectional video diffusion degrades as the causal chain lengthens, even when provided more denoising steps. In a length-matched single-ball control, where ball-ball interactions are absent, the degradation largely disappears, isolating dependent-event structure rather than video length as the cause. Across intervention studies, methods that increase effective serial computation improve performance disproportionately, including autoregressive/blockwise generation and architectural depth. We identify this pattern as the seriality gap: a mismatch between tasks requiring growing serial computation and video diffusion models whose denoising loop does not provide scalable serial compute. We then prove that, for deterministic video prediction, denoising steps do not add serial computation beyond the backbone, indicating a structural obstacle for video diffusion on serial reasoning and simulation tasks.

## 원문 영어

<details>
<summary>원문 보기</summary>

When one ball strikes another, then another, video models should predict the consequences of each bounce. In controlled experiments on multi-ball hard-sphere dynamics, we find that the performance of standard bidirectional video diffusion degrades as the causal chain lengthens, even when provided more denoising steps. In a length-matched single-ball control, where ball-ball interactions are absent, the degradation largely disappears, isolating dependent-event structure rather than video length a

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2607.13031v1)
