---
title: Visually Grounded Self-Reflection for Vision-Language Models via Reinforcement Learning
created: 2026-07-07
updated: 2026-07-07
type: concept
tags: [research, ai-ml, multimodal, agent]
sources: [raw/papers/visually-grounded-self-reflection-for-vision-language-models-2026-07-07.md]
confidence: medium
---

# Visually Grounded Self-Reflection for Vision-Language Models via Reinforcement Learning

> 📄 원문: [Visually Grounded Self-Reflection for Vision-Language Models via Reinforcement Learning](https://arxiv.org/abs/2607.02490v1)
> ✍️ 저자: Liyan Tang, Fangcong Yin, Greg Durrett
> 📅 발행: 2026-07-02
> 🏷️ 카테고리: cs.CL, cs.CV

## 요약

Large vision-language models can reason over multimodal inputs by generating textual chains of thought (CoT). A key capability exhibited in CoT reasoning is self-reflection: revisiting earlier decisions and correcting previous errors. However, existing LVLMs often fail to properly attend to visual inputs during reflection, limiting their ability to translate feedback into grounded corrections, especially for out-of-distribution images. To address this issue, we propose a novel reinforcement learning training framework VRRL, with two components explicitly designed to elicit visually grounded self-reflection. First, we randomly mask trajectory prefixes during training to emphasize recovery from incorrect intermediate predictions rather than making early mistakes. Second, we introduce buffered roll-ins from an experience replay buffer to expose the model to diverse failure states that it must learn to correct. We evaluate our approach on visual grounding tasks involving tables and charts, as well as spatial navigation benchmarks. While off-the-shelf and conventionally fine-tuned models degrade substantially under distribution shift, our method substantially improves average out-of-distribution accuracy over standard RL and reflection-oriented fine-tuning baselines by using self-reflection effectively.

## 원문 영어

<details>
<summary>원문 보기</summary>

Large vision-language models can reason over multimodal inputs by generating textual chains of thought (CoT). A key capability exhibited in CoT reasoning is self-reflection: revisiting earlier decisions and correcting previous errors. However, existing LVLMs often fail to properly attend to visual inputs during reflection, limiting their ability to translate feedback into grounded corrections, especially for out-of-distribution images. To address this issue, we propose a novel reinforcement lear

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2607.02490v1)
