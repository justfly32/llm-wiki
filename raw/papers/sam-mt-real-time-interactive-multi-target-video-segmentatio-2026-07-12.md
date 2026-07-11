---
source_url: https://arxiv.org/abs/2607.08688v1
ingested: 2026-07-12
type: paper
arxiv_id: 2607.08688v1
authors: Ruiqi Shen, Chang Liu, Henghui Ding
published: 2026-07-09
categories: cs.CV
---

# SAM-MT: Real-Time Interactive Multi-Target Video Segmentation

**Authors:** Ruiqi Shen, Chang Liu, Henghui Ding
**Published:** 2026-07-09
**arXiv:** https://arxiv.org/abs/2607.08688v1
**Categories:** cs.CV

## Abstract

Modern Video Object Segmentation (VOS) involves tracking and segmenting user-specified targets. While recent approaches have achieved remarkable performance in single-target scenarios, extending them to multi-target settings typically involves replicating the single-target processing for each individual object, resulting in reduced frame rates (FPS) with unbounded latency as target count increases. Built upon Segment Anything 2 (SAM2), we propose SAM-MT, which addresses this by transforming the model into an interactive framework for real-time Multi-Target video segmentation. SAM-MT uses explicit queries to represent different individual targets, in parallel with a shared representation for global context. It employs decoupled masked attention to keep individual identities distinct from cross-target interference, and sparse memory for stable temporal evolution, along with specialized strategies for occlusion handling and overlap prevention. SAM-MT successfully decouples latency from the number of targets, achieving real-time speed on par with single-target baselines (&gt;36 FPS for 10 targets) while maintaining SAM2's robust video segmentation performance.
