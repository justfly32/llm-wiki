---
title: UniClawBench: A Universal Benchmark for Proactive Agents on Real-World Tasks
created: 2026-07-11
updated: 2026-07-11
type: concept
tags: [research, ai-ml, programming, multimodal, agent]
sources: [raw/papers/uniclawbench-a-universal-benchmark-for-proactive-agents-on-2026-07-11.md]
confidence: medium
---

# UniClawBench: A Universal Benchmark for Proactive Agents on Real-World Tasks

> 📄 원문: [UniClawBench: A Universal Benchmark for Proactive Agents on Real-World Tasks](https://arxiv.org/abs/2607.08768v1)
> ✍️ 저자: Zhekai Chen, Chengqi Duan, Kaiyue Sun
> 📅 발행: 2026-07-09
> 🏷️ 카테고리: cs.CL

## 요약

The rapid development of large language models and multimodal large language models has accelerated the emergence of proactive agents capable of operating everyday tools and assisting users in real-world environments. However, existing benchmarks struggle to evaluate such agents effectively, as they often rely on sandboxed environments and single-turn evaluation paradigms. Moreover, their scenario-based task taxonomies mix multiple model capabilities within the same task category, making it difficult to identify the root causes of agent failures. To address these limitations, we introduce UniClawBench, the first capability-driven benchmark designed to evaluate proactive agents in dynamic, real-world settings. UniClawBench is built around five foundational model capabilities: Skill Usage, Exploration, Long-Context Reasoning, Multimodal Understanding, and Cross-Platform Coordination. Based on these capabilities, we design 400 bilingual real-world tasks. Unlike previous benchmarks that rely on static, pre-recorded answers, our benchmark evaluates agents in live Docker containers using fine-grained, step-by-step completion checkpoints. Furthermore, we design a closed-loop evaluation strategy comprising an executor agent, a hidden supervisor agent, and a user agent to simulate realistic multi-turn human feedback without leaking grading criteria. To disentangle base model capabilities from framework-level design choices, we evaluate state-of-the-art models under multiple agent frameworks. Through comprehensive comparisons across both models and frameworks, we show how base model capabilities and agent framework designs jointly shape performance in real-world environments. To facilitate future research, we make our benchmark and code publicly available at https://github.com/HKU-MMLab/UniClawBench.

## 원문 영어

<details>
<summary>원문 보기</summary>

The rapid development of large language models and multimodal large language models has accelerated the emergence of proactive agents capable of operating everyday tools and assisting users in real-world environments. However, existing benchmarks struggle to evaluate such agents effectively, as they often rely on sandboxed environments and single-turn evaluation paradigms. Moreover, their scenario-based task taxonomies mix multiple model capabilities within the same task category, making it diff

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2607.08768v1)
