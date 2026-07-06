---
source_url: https://arxiv.org/abs/2607.02490v1
ingested: 2026-07-07
type: paper
arxiv_id: 2607.02490v1
authors: Liyan Tang, Fangcong Yin, Greg Durrett
published: 2026-07-02
categories: cs.CL, cs.CV
---

# Visually Grounded Self-Reflection for Vision-Language Models via Reinforcement Learning

**Authors:** Liyan Tang, Fangcong Yin, Greg Durrett
**Published:** 2026-07-02
**arXiv:** https://arxiv.org/abs/2607.02490v1
**Categories:** cs.CL, cs.CV

## Abstract

Large vision-language models can reason over multimodal inputs by generating textual chains of thought (CoT). A key capability exhibited in CoT reasoning is self-reflection: revisiting earlier decisions and correcting previous errors. However, existing LVLMs often fail to properly attend to visual inputs during reflection, limiting their ability to translate feedback into grounded corrections, especially for out-of-distribution images. To address this issue, we propose a novel reinforcement learning training framework VRRL, with two components explicitly designed to elicit visually grounded self-reflection. First, we randomly mask trajectory prefixes during training to emphasize recovery from incorrect intermediate predictions rather than making early mistakes. Second, we introduce buffered roll-ins from an experience replay buffer to expose the model to diverse failure states that it must learn to correct. We evaluate our approach on visual grounding tasks involving tables and charts, as well as spatial navigation benchmarks. While off-the-shelf and conventionally fine-tuned models degrade substantially under distribution shift, our method substantially improves average out-of-distribution accuracy over standard RL and reflection-oriented fine-tuning baselines by using self-reflection effectively.
