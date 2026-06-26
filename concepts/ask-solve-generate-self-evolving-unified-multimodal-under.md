---
title: 질문하고, 풀고, 생성하라: Self-Consistency Rewards를 통한 자기 진화형 통합 다중 모달 이해 및 생성
created: 2026-06-27
updated: 2026-06-27
type: concept
tags: [research, programming, multimodal, diffusion]
sources: [raw/papers/ask-solve-generate-self-evolving-unified-multimodal-under-2026-06-27.md]
confidence: medium
---

# 질문하고, 풀고, 생성하라: Self-Consistency Rewards를 통한 자기 진화형 통합 다중 모달 이해 및 생성

> 📄 원문: [Ask, Solve, Generate: Self-Evolving Unified Multimodal Understanding and Generation via Self-Consistency Rewards](https://arxiv.org/abs/2606.27376v1)
> ✍️ 저자: Ritesh Thawkar, Shravan Venkatraman, Omkar Thawakar
> 📅 발행: 2026-06-25
> 🏷️ 카테고리: cs.CV

## 요약

시각적 이해와 이미지 생성을 모두 지원하는 대부분의 통합 대규모 다중모달 모델(LMM)은 여전히 큐레이션된 포스트트레이닝 감독, 즉 인간 어노테이션, 선호도 레이블, 또는 외부 보상 모델에 의존합니다. 우리는 레이블이 지정되지 않은 이미지만을 사용하여 통합 LMM이 두 능력을 모두 자율적으로 향상시킬 수 있는지 탐구합니다. 우리는 세 가지 내부 역할을 갖는 자기 진화형 훈련 프레임워크를 제안합니다: 시각적 질문을 생성하는 Proposer, 질문에 답하고 평가하는 Solver, 그리고 이미지를 합성하는 Generator. 훈련은 인간 어노테이션, 선호도 레이블, 또는 과정 훈련된 외부 보상/심사 모델 없이 오직 자기 파생 일관성 신호만을 사용합니다. 학습을 안정화하기 위해, 토큰 수준 예측 불확실성에 기반한 연속적인 난이도 신호인 Solver Token Entropy(STE)를 도입하며, 이는 샘플 수준 일관성이 신뢰할 수 없게 된 경우에도 유용하게 작동합니다. 이미지 생성을 위해, 질문-응답 충실도 평가와 순환 일관적 캡셔닝(cycle-consistent captioning)을 결합한 다중 스케일 내부 평가 체계를 설계합니다. 이는 더 나은 시각적 이해가 더 신뢰할 수 있는 생성 평가와 더 강력한 내부 훈련 신호를 가능하게 하는 Solver 매개 결합(solver-mediated coupling)을 만들어냅니다. 이 프레임워크는 diffusion 기반 BLIP3o, rectified-flow 기반 BAGEL, autoregressive 기반 VARGPT-v1.1 아키텍처 전체에 동일한 역할 분해, 보상 로직, 훈련 스케줄을 유지하며, 각 백본의 네이티브 프롬프팅 및 생성 인터페이스만을 요구합니다. 여덟 가지 이해 지표에 걸쳐, 우리의 me

(이하 생략...)

## 원문 영어

<details>
<summary>원문 보기</summary>

Most unified large multimodal models (LMMs) that support both visual understanding and image generation still rely on curated post-training supervision, such as human annotations, preference labels, or external reward models. We ask whether a unified LMM can improve both abilities autonomously using only unlabeled images. We propose a self-evolving training framework with three internal roles: a Proposer that generates visual questions, a Solver that answers and evaluates them, and a Generator t

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2606.27376v1)
