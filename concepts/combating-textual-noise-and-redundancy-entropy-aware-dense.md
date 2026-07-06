---
title: Combating Textual Noise and Redundancy: Entropy-Aware Dense Visual Token Pruning
created: 2026-07-07
updated: 2026-07-07
type: concept
tags: [research, optimization, multimodal]
sources: [raw/papers/combating-textual-noise-and-redundancy-entropy-aware-dense-2026-07-07.md]
confidence: medium
---

# Combating Textual Noise and Redundancy: Entropy-Aware Dense Visual Token Pruning

> 📄 원문: [Combating Textual Noise and Redundancy: Entropy-Aware Dense Visual Token Pruning](https://arxiv.org/abs/2607.02484v1)
> ✍️ 저자: Xuehui Wang, Xuankun Yang, Wei Shen
> 📅 발행: 2026-07-02
> 🏷️ 카테고리: cs.CV, cs.AI

## 요약

Visual token pruning is a crucial strategy for accelerating VLMs by compressing redundant image patches, yet existing methods often fail to preserve critical cues under dense instructions and fine-grained queries. In this paper, we investigate this failure and identify two underlying bottlenecks: the widespread dispersion of textual noise that corrupts dense cross-modal scoring, and the feature fragmentation inherent to standard token selection. To address these issues, we propose Entropy-Aware Dense Pruning (EADP), a framework that reformulates pruning as a structured compression problem. EADP first leverages statistical entropy to quantify and filter out textual noise, yielding a robust, fine-grained instruction relevance score. Subsequently, instead of naive Top-K selection, EADP casts token selection as a submodular maximization problem with a spatial prior, explicitly ensuring a holistic and non-redundant visual representation. Extensive experiments demonstrate that EADP improves the accuracy-efficiency trade-off of VLMs, robustly preserving fine-grained visual cues under strict token budgets while achieving SoTA performance on challenging multimodal benchmarks.

## 원문 영어

<details>
<summary>원문 보기</summary>

Visual token pruning is a crucial strategy for accelerating VLMs by compressing redundant image patches, yet existing methods often fail to preserve critical cues under dense instructions and fine-grained queries. In this paper, we investigate this failure and identify two underlying bottlenecks: the widespread dispersion of textual noise that corrupts dense cross-modal scoring, and the feature fragmentation inherent to standard token selection. To address these issues, we propose Entropy-Aware 

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2607.02484v1)
