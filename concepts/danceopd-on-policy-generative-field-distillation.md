---
title: DanceOPD: 온-정책 생성 필드 증류
created: 2026-06-29
updated: 2026-06-29
type: concept
tags: [research, multimodal, diffusion]
sources: [raw/papers/danceopd-on-policy-generative-field-distillation-2026-06-29.md]
confidence: medium
---

# DanceOPD: 온-정책 생성 필드 증류

> 📄 원문: [DanceOPD: On-Policy Generative Field Distillation](https://arxiv.org/abs/2606.27377v1)
> ✍️ 저자: Wei Zhou, Xiongwei Zhu, Zelin Xu
> 📅 발행: 2026-06-25
> 🏷️ 카테고리: cs.CV, cs.CL, cs.LG

## 요약

현대적 이미지 생성은 텍스트-이미지(T2I), 로컬 편집, 글로벌 편집 등 다양한 기능을 통합하는 단일 모델을 요구한다. 그러나 이러한 기능들은 자연스럽게 정렬되지 않는 경우가 많고 종종 충돌한다. 예를 들어, 편집은 T2I 성능을 저하시키는 경향이 있으며, 글로벌 편집과 로컬 편집은 서로 간섭한다. 결과적으로 이러한 기능들을 효과적으로 조합하는 것은 이미지 생성 모델 훈련의 핵심 과제가 되었다. 이를 해결하기 위해, 우리는 DanceOPD를 소개한다. DanceOPD는 플로우 매칭(flow-matching) 모델을 위한 온폴리시(on-policy) 생성 필드 증류 프레임워크로, 각 샘플을 하나의 기능 필드로 라우팅하고, 하나의 저노이즈 학생 유도 상태를 쿼리하며, 단순한 속도 MSE 목적함수로 훈련한다. 각 기능 소스를 공유 플로우 상태 공간 위의 속도 필드로 정의함으로써, 학생은 자체 롤아웃(rollout) 상태에서 쿼리된 필드로부터 학습하여 전문가 기능들을 조합한다. 이 공식은 또한 분류자 없는 가이던스(classifier-free guidance)와 같은 연산자 정의 필드도 흡수할 수 있다. T2I, 편집, 리얼리즘 필드 흡수, CFG 흡수에 대한 종합적인 실험 결과, 우리의 접근법이 다중 기능 조합을 개선하여 앵커 생성 품질을 유지하면서 대상 기능을 강화하는 것을 보여준다. 우리는 이 연구가 플로우 매칭 모델에서 생성 필드 증류를 위한 실용적인 경로를 확립한다고 믿는다.

## 원문 영어

<details>
<summary>원문 보기</summary>

Modern image generation demands a single model that unifies diverse capabilities, including text-to-image (T2I), local editing, and global editing. However, these capabilities are rarely naturally aligned and often conflict. For instance, editing tends to degrade T2I performance, while global and local editing interfere with each other. Consequently, effectively composing these capabilities has become a central challenge for image generation model training. To tackle this, we introduce DanceOPD,

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2606.27377v1)
