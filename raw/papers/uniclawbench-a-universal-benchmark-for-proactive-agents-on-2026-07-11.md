---
source_url: https://arxiv.org/abs/2607.08768v1
ingested: 2026-07-11
type: paper
arxiv_id: 2607.08768v1
authors: Zhekai Chen, Chengqi Duan, Kaiyue Sun
published: 2026-07-09
categories: cs.CL
---

# UniClawBench: A Universal Benchmark for Proactive Agents on Real-World Tasks

**Authors:** Zhekai Chen, Chengqi Duan, Kaiyue Sun
**Published:** 2026-07-09
**arXiv:** https://arxiv.org/abs/2607.08768v1
**Categories:** cs.CL

## Abstract

The rapid development of large language models and multimodal large language models has accelerated the emergence of proactive agents capable of operating everyday tools and assisting users in real-world environments. However, existing benchmarks struggle to evaluate such agents effectively, as they often rely on sandboxed environments and single-turn evaluation paradigms. Moreover, their scenario-based task taxonomies mix multiple model capabilities within the same task category, making it difficult to identify the root causes of agent failures. To address these limitations, we introduce UniClawBench, the first capability-driven benchmark designed to evaluate proactive agents in dynamic, real-world settings. UniClawBench is built around five foundational model capabilities: Skill Usage, Exploration, Long-Context Reasoning, Multimodal Understanding, and Cross-Platform Coordination. Based on these capabilities, we design 400 bilingual real-world tasks. Unlike previous benchmarks that rely on static, pre-recorded answers, our benchmark evaluates agents in live Docker containers using fine-grained, step-by-step completion checkpoints. Furthermore, we design a closed-loop evaluation strategy comprising an executor agent, a hidden supervisor agent, and a user agent to simulate realistic multi-turn human feedback without leaking grading criteria. To disentangle base model capabilities from framework-level design choices, we evaluate state-of-the-art models under multiple agent frameworks. Through comprehensive comparisons across both models and frameworks, we show how base model capabilities and agent framework designs jointly shape performance in real-world environments. To facilitate future research, we make our benchmark and code publicly available at https://github.com/HKU-MMLab/UniClawBench.
