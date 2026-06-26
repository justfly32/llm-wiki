---
title: DanceOPD: 온-정책 생성형 필드 증류 (On-Policy Generative Field Distillation)
created: 2026-06-27
updated: 2026-06-27
type: concept
tags: [research, multimodal, diffusion]
sources: [raw/papers/danceopd-on-policy-generative-field-distillation-2026-06-27.md]
confidence: medium
---

# DanceOPD: 온-정책 생성형 필드 증류 (On-Policy Generative Field Distillation)

> 📄 원문: [DanceOPD: On-Policy Generative Field Distillation](https://arxiv.org/abs/2606.27377v1)
> ✍️ 저자: Wei Zhou, Xiongwei Zhu, Zelin Xu
> 📅 발행: 2026-06-25
> 🏷️ 카테고리: cs.CV, cs.CL, cs.LG

## 요약

최신 이미지 생성에서는 텍스트-이미지 변환(text-to-image, T2I), 로컬 편집(local editing), 글로벌 편집(global editing) 등 다양한 기능을 통합하는 단일 모델이 요구된다. 그러나 이러한 기능들은 자연스럽게 정렬되는 경우가 드물며, 종 돌한다. 예를 들어, 편집 기능은 T2I 성능을 저하시키는 경향이 있고, 글로벌 편집과 로컬 편집은 서로 간섭한다. 결과적으로 이러한 기능들을 효과적으로 조합하는 것은 이미지 생성 모델 학습의 심 과제가 되었다. 이를 해결하기 위해, 우리는 flow-matching 모델을 위한 온리시 생성 필드 증류(on-policy generative field distillation) 프레임워크인 DanceOPD를 제안한다. 이 프레임워크는 각 샘플을 하나의 기능 필드로 라우팅하고, 하나의 저노이즈 학생 유도 상태(low-noise student-induced state)를 리하며, 단순한 속도 MSE(velocity MSE) 목적함수로 학습한다. 각 기능 소스를 공유 름 상태 공간(shared flow state space) 위의 속도 필드(velocity field)로 정의하면, 학생은 자체 롤아웃 상태(rollout states)에서 리된 필드로부터 학습하여 전문가 기능들을 조합한다. 이 공식화는 또한 classifier-free guidance(CFG)와 같은 연산자 정의 필드(operator-defined fields)도 흡수할 수 있다. T2I, 편집, 리리즘 필드 흡수, CFG 수에 대한 종합적인 실험 결과, 우리의 접근법이 다중 기능 조합을 개선하여 대상 기능을 강화하면서도 앵커 생성 질을 보존하는 것으로 나타다. 본 연구는 flow-matching 모델에서 생성 필드 증류를 위한 실질적인 경로를 확립한다고 믿는다.

## 원문 영어

<details>
<summary>원문 보기</summary>

Modern image generation demands a single model that unifies diverse capabilities, including text-to-image (T2I), local editing, and global editing. However, these capabilities are rarely naturally aligned and often conflict. For instance, editing tends to degrade T2I performance, while global and local editing interfere with each other. Consequently, effectively composing these capabilities has become a central challenge for image generation model training. To tackle this, we introduce DanceOPD,

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2606.27377v1)
