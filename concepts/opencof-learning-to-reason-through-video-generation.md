---
title: OpenCoF: Learning to Reason Through Video Generation
created: 2026-07-13
updated: 2026-07-13
type: concept
tags: [research, programming, multimodal, agent]
sources: [raw/papers/opencof-learning-to-reason-through-video-generation-2026-07-13.md]
confidence: medium
---

# OpenCoF: Learning to Reason Through Video Generation

> 📄 원문: [OpenCoF: Learning to Reason Through Video Generation](https://arxiv.org/abs/2607.08763v1)
> ✍️ 저자: Xinyan Chen, Ziyu Guo, Renrui Zhang
> 📅 발행: 2026-07-09
> 🏷️ 카테고리: cs.CV, cs.AI

## 요약

Reasoning has become a core capability for large models, especially when reliable decisions require understanding logical consequences. Recent video generation models offer a reasoning path distinct from previous Chain-of-Thought (CoT): reasoning can unfold through temporally connected frames, known as Chain-of-Frame (CoF) reasoning. However, existing video generators are primarily trained on general video corpora, still lacking diverse supervision and dedicated designs for CoF reasoning. To address this gap, we introduce OpenCoF, a framework comprising the OpenCoF-17K dataset, a reasoning video dataset spanning 11 task families, and Wan-CoF, a fine-tuned video model for studying whether diverse temporal supervision improves CoF behavior. Across four video reasoning benchmarks, Wan-CoF achieves considerable gains over the Wan2.2-I2V-A14B baseline. Building on this, we empirically explore more advanced designs for CoF capabilities, i.e., equipping the model with visual and textual reasoning tokens. This mechanism respectively captures low-level visual cues and high-level semantic priors for spatial and temporal reasoning. Through performance comparisons and attention analysis, we examine how these tokens contribute across model depth, denoising steps, space, and time. Our results suggest that stronger video reasoning requires both broad temporal supervision and explicit mechanisms for organizing intermediate reasoning state. We open-source the dataset, model, and code to facilitate future research on reasoning-oriented video generation.

## 원문 영어

<details>
<summary>원문 보기</summary>

Reasoning has become a core capability for large models, especially when reliable decisions require understanding logical consequences. Recent video generation models offer a reasoning path distinct from previous Chain-of-Thought (CoT): reasoning can unfold through temporally connected frames, known as Chain-of-Frame (CoF) reasoning. However, existing video generators are primarily trained on general video corpora, still lacking diverse supervision and dedicated designs for CoF reasoning. To add

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2607.08763v1)
