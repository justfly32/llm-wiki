---
title: The Key to Going Linear: Analysis-Driven Transformer Linearization
created: 2026-07-10
updated: 2026-07-10
type: concept
tags: [research, optimization]
sources: [raw/papers/the-key-to-going-linear-analysis-driven-transformer-lineari-2026-07-10.md]
confidence: medium
---

# The Key to Going Linear: Analysis-Driven Transformer Linearization

> 📄 원문: [The Key to Going Linear: Analysis-Driven Transformer Linearization](https://arxiv.org/abs/2607.07706v1)
> ✍️ 저자: Anna Kuzina, Paul N. Whatmough, Babak Ehteshami Bejnordi
> 📅 발행: 2026-07-08
> 🏷️ 카테고리: cs.LG

## 요약

The quadratic cost of causal self-attention severely bottlenecks long-context transformer inference. While numerous post hoc linearization pipelines exist, it is difficult to identify which components preserve model quality. This work isolates the effect of state update design in a strict frozen-backbone regime. We show that softmax relies on key-dependent, rank-1 orthogonal projections, elucidating why delta-style networks outperform purely gated accumulation. We identify a potential source of approximation errors and introduce structural interventions, specifically sink tokens, short convolutions, and fixed-budget cache routing, which reduces the remaining gap. We scale this linearization approach across LLaMA and Qwen models up to 32B parameters, outperforming prior post hoc baselines on MMLU and matching the long-context retrieval of complex adaptive-caching frameworks.

## 원문 영어

<details>
<summary>원문 보기</summary>

The quadratic cost of causal self-attention severely bottlenecks long-context transformer inference. While numerous post hoc linearization pipelines exist, it is difficult to identify which components preserve model quality. This work isolates the effect of state update design in a strict frozen-backbone regime. We show that softmax relies on key-dependent, rank-1 orthogonal projections, elucidating why delta-style networks outperform purely gated accumulation. We identify a potential source of 

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2607.07706v1)
