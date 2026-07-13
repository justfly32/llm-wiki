---
title: OpenLongTail: Generative Scaling of Long-Tail Driving Data
created: 2026-07-14
updated: 2026-07-14
type: concept
tags: [research, alignment, multimodal, diffusion]
sources: [raw/papers/openlongtail-generative-scaling-of-long-tail-driving-data-2026-07-14.md]
confidence: medium
---

# OpenLongTail: Generative Scaling of Long-Tail Driving Data

> 📄 원문: [OpenLongTail: Generative Scaling of Long-Tail Driving Data](https://arxiv.org/abs/2607.09655v1)
> ✍️ 저자: Lulin Liu, Nuo Chen, Yan Wang
> 📅 발행: 2026-07-10
> 🏷️ 카테고리: cs.CV

## 요약

Scaling robust driving policies is fundamentally bottlenecked by the scarcity of edge cases in curated datasets. While the real world continuously captures these critical events, such long-tail events remain underutilized when collected from heterogeneous sources. Specifically, diverse but valuable in-the-wild long-tail videos lack the full view coverage required for training policy models, often missing multi-view poses or originating solely from monocular dash cameras. This modality gap prevents these ubiquitous observations from being converted into scalable training data for long-tail generalization. We introduce OpenLongTail, an open-source generative data engine for scaling autonomous driving policies under long-tail events. To transform heterogeneous data sources into view-aligned and temporally coherent multi-view assets that are useful for policy learning, we develop a pose-informed extrapolative view synthesis pipeline that generates the missing views. We further enhance cross-view consistency and the temporal alignment for the newly generated views by injecting Plücker ray geometry into the scalable generation engine. By synthesizing heterogeneous long-tail data, we observe a significant improvement in closed-loop driving robustness in handling long-tail events. By measuring the extrapolative view synthesis and pose metrics, we validate the effectiveness of OpenLongTail in visual fidelity, cross-view consistency, and ego-trajectory recovery.

## 원문 영어

<details>
<summary>원문 보기</summary>

Scaling robust driving policies is fundamentally bottlenecked by the scarcity of edge cases in curated datasets. While the real world continuously captures these critical events, such long-tail events remain underutilized when collected from heterogeneous sources. Specifically, diverse but valuable in-the-wild long-tail videos lack the full view coverage required for training policy models, often missing multi-view poses or originating solely from monocular dash cameras. This modality gap preven

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2607.09655v1)
