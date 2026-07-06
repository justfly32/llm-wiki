---
source_url: https://arxiv.org/abs/2607.02484v1
ingested: 2026-07-07
type: paper
arxiv_id: 2607.02484v1
authors: Xuehui Wang, Xuankun Yang, Wei Shen
published: 2026-07-02
categories: cs.CV, cs.AI
---

# Combating Textual Noise and Redundancy: Entropy-Aware Dense Visual Token Pruning

**Authors:** Xuehui Wang, Xuankun Yang, Wei Shen
**Published:** 2026-07-02
**arXiv:** https://arxiv.org/abs/2607.02484v1
**Categories:** cs.CV, cs.AI

## Abstract

Visual token pruning is a crucial strategy for accelerating VLMs by compressing redundant image patches, yet existing methods often fail to preserve critical cues under dense instructions and fine-grained queries. In this paper, we investigate this failure and identify two underlying bottlenecks: the widespread dispersion of textual noise that corrupts dense cross-modal scoring, and the feature fragmentation inherent to standard token selection. To address these issues, we propose Entropy-Aware Dense Pruning (EADP), a framework that reformulates pruning as a structured compression problem. EADP first leverages statistical entropy to quantify and filter out textual noise, yielding a robust, fine-grained instruction relevance score. Subsequently, instead of naive Top-K selection, EADP casts token selection as a submodular maximization problem with a spatial prior, explicitly ensuring a holistic and non-redundant visual representation. Extensive experiments demonstrate that EADP improves the accuracy-efficiency trade-off of VLMs, robustly preserving fine-grained visual cues under strict token budgets while achieving SoTA performance on challenging multimodal benchmarks.
