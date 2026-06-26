---
source_url: https://arxiv.org/abs/2606.02576v1
ingested: 2026-06-03
type: paper
arxiv_id: 2606.02576v1
authors: Yu-Cheng Shi, Zhen-Hao Xie, Jun-Tao Tang
published: 2026-06-01
categories: cs.CV, cs.LG
---

# ProtoAda: Prototype-Guided Adaptive Adapter Expansion and Geometric Consolidation for Multimodal Continual Instruction Tuning

**Authors:** Yu-Cheng Shi, Zhen-Hao Xie, Jun-Tao Tang
**Published:** 2026-06-01
**arXiv:** https://arxiv.org/abs/2606.02576v1
**Categories:** cs.CV, cs.LG

## Abstract

Multimodal Large Language Models (MLLMs) achieve strong performance through instruction tuning, but real-world deployment requires them to continually acquire new vision-language capabilities, making Multimodal Continual Instruction Tuning (MCIT) essential. To reduce inter-task interference and promote collaboration, recent methods often employ sparse architectures like Mixture of LoRA Experts with image-text similarity routing. However, tasks with distinct response structures could share highly similar visual-linguistic semantics and thus be wrongly routed to the same expert; image-text similarity alone is insufficient for reliable task assignment. For example, an expert in a grounding task requiring coordinate prediction may be biased toward producing short textual answers after learning semantically similar VQA tasks. This format-blind task assignment integrates heterogeneous response types into shared parameters, inducing gradient interference and ineffective expert collaboration. To address this problem, we propose ProtoAda, a prototype-guided adaptive tuning framework. ProtoAda introduces format-aware task prototypes to align task assignment and routing with both task semantics and output structure, and further consolidates format-compatible updates in a geometry-aware manner to effectively reuse and progressively refine existing parameters. Extensive experiments on multiple benchmarks demonstrate that ProtoAda achieves superior performance, especially on tasks whose answer structures are easily corrupted by sequential tuning.
