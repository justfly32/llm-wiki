---
title: Mixture of Frames Policy: Multi-Frame Action Denoising for Bimanual Mobile Manipulation
created: 2026-07-15
updated: 2026-07-15
type: concept
tags: [research, diffusion]
sources: [raw/papers/mixture-of-frames-policy-multi-frame-action-denoising-for-b-2026-07-15.md]
confidence: medium
---

# Mixture of Frames Policy: Multi-Frame Action Denoising for Bimanual Mobile Manipulation

> 📄 원문: [Mixture of Frames Policy: Multi-Frame Action Denoising for Bimanual Mobile Manipulation](https://arxiv.org/abs/2607.11884v1)
> ✍️ 저자: Dian Wang, Jisang Park, Xiaomeng Xu
> 📅 발행: 2026-07-13
> 🏷️ 카테고리: cs.RO

## 요약

Robotic manipulation is inherently multi-frame: local actions may be simple in an end-effector frame, while transport, upright-object handling, and whole-body coordination are better represented in a base-aligned frame. However, modern diffusion-based visuomotor policies typically commit to a single predefined action frame, forcing one denoiser to model action distributions that are often unnecessarily complex in that frame. We propose Mixture of Frames Policy (MoF), a diffusion policy that performs synchronized action denoising across multiple coordinate frames. MoF maintains a single canonical diffusion state, re-expresses it in several task-relevant frames, applies frame-specialized denoisers, and fuses their noise predictions back in the canonical frame. To make this possible for intermediate noisy diffusion states, we introduce a column-based 6D rotation representation within an SE(3) action parameterization that supports exact, differentiable frame transformations without requiring noisy rotations to lie on the SO(3) manifold. Across nine simulated bimanual manipulation tasks, we show that the best action frame is task-dependent and that MoF improves over oracle frame selection and standard Mixture-of-Experts (MoE) baselines. We further evaluate MoF on two real-world bimanual mobile manipulation tasks, demonstrating that it outperforms all constituent single-frame baselines. Project homepage: https://mofpo.github.io

## 원문 영어

<details>
<summary>원문 보기</summary>

Robotic manipulation is inherently multi-frame: local actions may be simple in an end-effector frame, while transport, upright-object handling, and whole-body coordination are better represented in a base-aligned frame. However, modern diffusion-based visuomotor policies typically commit to a single predefined action frame, forcing one denoiser to model action distributions that are often unnecessarily complex in that frame. We propose Mixture of Frames Policy (MoF), a diffusion policy that perf

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2607.11884v1)
