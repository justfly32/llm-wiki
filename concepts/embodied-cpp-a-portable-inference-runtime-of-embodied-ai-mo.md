---
title: Embodied.cpp: A Portable Inference Runtime of Embodied AI Models on Heterogeneous Robots
created: 2026-07-06
updated: 2026-07-06
type: concept
tags: [research, programming, optimization, multimodal]
sources: [raw/papers/embodied-cpp-a-portable-inference-runtime-of-embodied-ai-mo-2026-07-06.md]
confidence: medium
---

# Embodied.cpp: A Portable Inference Runtime of Embodied AI Models on Heterogeneous Robots

> 📄 원문: [Embodied.cpp: A Portable Inference Runtime of Embodied AI Models on Heterogeneous Robots](https://arxiv.org/abs/2607.02501v1)
> ✍️ 저자: Ling Xu, Chuyu Han, Borui Li
> 📅 발행: 2026-07-02
> 🏷️ 카테고리: cs.RO, cs.CV, cs.OS

## 요약

Embodied AI models now span vision-language-action (VLA) models and world-action models (WAMs), but practical deployment remains fragmented across model-specific Python stacks, backend assumptions, and robot-side glue code, especially on heterogeneous edge devices. Existing inference runtimes are designed mainly for request-response serving and therefore do not satisfy the runtime contract of embodied deployment: multi-rate execution inside closed-loop control, latency-first batch-1 inference on heterogeneous hardware, and extensible embodied interfaces beyond fixed token I/O. We present Embodied.cpp, a portable C++ inference runtime for embodied models. Based on an architectural analysis of representative VLA models and WAMs, Embodied.cpp captures a shared execution path and organizes it into five layers: input adapters, sequence builders, backbone execution, head plugins, and deployment adapters. The runtime provides modular multi-rate execution, latency-first fused inference, and extensible operator and I/O support, enabling deployment across heterogeneous devices, robots, and simulators through one backend abstraction. We evaluate Embodied.cpp on two VLA models, HY-VLA and pi0.5, and on a preliminary WAM benchmark using a LingBot-VA Transformer block. The VLA deployments achieve successful closed-loop execution with 100.0% and 91.0% task success rates, respectively. The WAM benchmark reduces block memory from 312.2 MiB to 88.1 MiB. These results show that Embodied.cpp improves deployment efficiency while preserving high accuracy across diverse embodied model architectures.

## 원문 영어

<details>
<summary>원문 보기</summary>

Embodied AI models now span vision-language-action (VLA) models and world-action models (WAMs), but practical deployment remains fragmented across model-specific Python stacks, backend assumptions, and robot-side glue code, especially on heterogeneous edge devices. Existing inference runtimes are designed mainly for request-response serving and therefore do not satisfy the runtime contract of embodied deployment: multi-rate execution inside closed-loop control, latency-first batch-1 inference on

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2607.02501v1)
