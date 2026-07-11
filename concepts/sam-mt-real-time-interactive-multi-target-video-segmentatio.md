---
title: SAM-MT: Real-Time Interactive Multi-Target Video Segmentation
created: 2026-07-12
updated: 2026-07-12
type: concept
tags: [research, multimodal]
sources: [raw/papers/sam-mt-real-time-interactive-multi-target-video-segmentatio-2026-07-12.md]
confidence: medium
---

# SAM-MT: Real-Time Interactive Multi-Target Video Segmentation

> 📄 원문: [SAM-MT: Real-Time Interactive Multi-Target Video Segmentation](https://arxiv.org/abs/2607.08688v1)
> ✍️ 저자: Ruiqi Shen, Chang Liu, Henghui Ding
> 📅 발행: 2026-07-09
> 🏷️ 카테고리: cs.CV

## 요약

Modern Video Object Segmentation (VOS) involves tracking and segmenting user-specified targets. While recent approaches have achieved remarkable performance in single-target scenarios, extending them to multi-target settings typically involves replicating the single-target processing for each individual object, resulting in reduced frame rates (FPS) with unbounded latency as target count increases. Built upon Segment Anything 2 (SAM2), we propose SAM-MT, which addresses this by transforming the model into an interactive framework for real-time Multi-Target video segmentation. SAM-MT uses explicit queries to represent different individual targets, in parallel with a shared representation for global context. It employs decoupled masked attention to keep individual identities distinct from cross-target interference, and sparse memory for stable temporal evolution, along with specialized strategies for occlusion handling and overlap prevention. SAM-MT successfully decouples latency from the number of targets, achieving real-time speed on par with single-target baselines (&gt;36 FPS for 10 targets) while maintaining SAM2's robust video segmentation performance.

## 원문 영어

<details>
<summary>원문 보기</summary>

Modern Video Object Segmentation (VOS) involves tracking and segmenting user-specified targets. While recent approaches have achieved remarkable performance in single-target scenarios, extending them to multi-target settings typically involves replicating the single-target processing for each individual object, resulting in reduced frame rates (FPS) with unbounded latency as target count increases. Built upon Segment Anything 2 (SAM2), we propose SAM-MT, which addresses this by transforming the 

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2607.08688v1)
