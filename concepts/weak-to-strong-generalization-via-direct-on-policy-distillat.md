---
title: Weak-to-Strong Generalization via Direct On-Policy Distillation
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [research, multimodal, agent]
sources: [raw/papers/weak-to-strong-generalization-via-direct-on-policy-distillat-2026-07-08.md]
confidence: medium
---

# Weak-to-Strong Generalization via Direct On-Policy Distillation

> 📄 원문: [Weak-to-Strong Generalization via Direct On-Policy Distillation](https://arxiv.org/abs/2607.05394v1)
> ✍️ 저자: Shiyuan Feng, Huan-ang Gao, Haohan Chi
> 📅 발행: 2026-07-06
> 🏷️ 카테고리: cs.LG, cs.AI, cs.CL

## 요약

Reinforcement learning with verifiable rewards (RLVR) is a powerful recipe for improving language-model reasoning, but it is expensive to repeat on every new strong model because the target model must generate many rollouts during training. As models scale, post-training itself becomes a bottleneck. We study a weak-to-strong alternative: run RL on a smaller model where rollouts are cheaper, then reuse what that RL run learned to improve a stronger target model. Directly distilling the post-RL weak teacher is not enough, because the teacher's final policy mixes useful RL gains with the limitations of the smaller model. We propose Direct On-Policy Distillation (Direct-OPD), which transfers the teacher's RL-induced policy shift instead. Direct-OPD compares the post-RL teacher with its own pre-RL reference and treats their log-ratio as a dense implicit reward for the student. In plain terms, the checkpoint pair tells us which actions RL made the weak model more or less likely to take, and Direct-OPD applies that signal on the stronger student's own on-policy states. This directly reuses the weak model's RL supervision signal without training an explicit reward model or running sparse-reward RL on the target model. Empirically, Direct-OPD consistently leverages weaker teachers to improve stronger target models; notably, it boosts Qwen3-1.7B from 48.3% to 62.4% on AIME 2024 in just 4 hours on 8 A100 GPUs. It outperforms step-matched direct RL and enables the sequential composition of multiple policy shifts. Our results show that RL outcomes can be reused across model scales as implicit reward signals, not merely as final models to imitate.

## 원문 영어

<details>
<summary>원문 보기</summary>

Reinforcement learning with verifiable rewards (RLVR) is a powerful recipe for improving language-model reasoning, but it is expensive to repeat on every new strong model because the target model must generate many rollouts during training. As models scale, post-training itself becomes a bottleneck. We study a weak-to-strong alternative: run RL on a smaller model where rollouts are cheaper, then reuse what that RL run learned to improve a stronger target model. Directly distilling the post-RL we

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2607.05394v1)
