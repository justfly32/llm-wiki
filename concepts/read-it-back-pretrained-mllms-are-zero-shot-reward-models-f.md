---
title: Read It Back: Pretrained MLLMs Are Zero-Shot Reward Models for Text-to-Image Generation
created: 2026-07-15
updated: 2026-07-15
type: concept
tags: [research, ai-ml, alignment, multimodal, diffusion]
sources: [raw/papers/read-it-back-pretrained-mllms-are-zero-shot-reward-models-f-2026-07-15.md]
confidence: medium
---

# Read It Back: Pretrained MLLMs Are Zero-Shot Reward Models for Text-to-Image Generation

> 📄 원문: [Read It Back: Pretrained MLLMs Are Zero-Shot Reward Models for Text-to-Image Generation](https://arxiv.org/abs/2607.11886v1)
> ✍️ 저자: Runhui Huang, Qihui Zhang, Zhe Liu
> 📅 발행: 2026-07-13
> 🏷️ 카테고리: cs.CV

## 요약

In this paper, we propose SpectraReward, a training-free reward function that turns pretrained MLLMs into off-the-shelf reward models for image-generation reinforcement learning. Instead of asking the MLLM to judge a generated image or answer decomposed verification questions, SpectraReward measures how well the original prompt can be recovered from the generated image through a single image-conditioned, teacher-forced forward pass. We use the average image-conditioned prompt log-likelihood as the reward, directly reusing the MLLM's pretrained image-text alignment ability without preference labels, reward-model fine-tuning. We further introduce Self-SpectraReward, a special case for unified multimodal models where the policy's own understanding branch serves as the reward model for its generation branch, forming a closed-loop self-improving framework without external reward models or external knowledge. Extensive experiments validate SpectraReward through a broad image-generation RL study covering two diffusion models, three RL algorithms, nine reward MLLM backbones from four MLLM families spanning 4B to 235B parameters, and five out-of-distribution text-to-image benchmarks. Results show that both SpectraReward and Self-SpectraReward significantly and consistently improve generation performance and outperform prior MLLM-derived reward training methods. Further analysis reveals that larger reward MLLMs are not always better, while Self-SpectraReward can match or surpass much larger external reward models, suggesting that reward-policy alignment is a key factor for effective image-generation RL. Project Page: https://huangrh99.github.io/SpectraReward/

## 원문 영어

<details>
<summary>원문 보기</summary>

In this paper, we propose SpectraReward, a training-free reward function that turns pretrained MLLMs into off-the-shelf reward models for image-generation reinforcement learning. Instead of asking the MLLM to judge a generated image or answer decomposed verification questions, SpectraReward measures how well the original prompt can be recovered from the generated image through a single image-conditioned, teacher-forced forward pass. We use the average image-conditioned prompt log-likelihood as t

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2607.11886v1)
