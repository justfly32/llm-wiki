---
title: 질문하고, 고, 생성하기: 자기 일관성 보상을 통한 자기 진화적 통합 다중 모달 이해 및 생성
created: 2026-06-29
updated: 2026-06-29
type: concept
tags: [research, programming, multimodal, diffusion]
sources: [raw/papers/ask-solve-generate-self-evolving-unified-multimodal-under-2026-06-29.md]
confidence: medium
---

# 질문하고, 고, 생성하기: 자기 일관성 보상을 통한 자기 진화적 통합 다중 모달 이해 및 생성

> 📄 원문: [Ask, Solve, Generate: Self-Evolving Unified Multimodal Understanding and Generation via Self-Consistency Rewards](https://arxiv.org/abs/2606.27376v1)
> ✍️ 저자: Ritesh Thawkar, Shravan Venkatraman, Omkar Thawakar
> 📅 발행: 2026-06-25
> 🏷️ 카테고리: cs.CV

## 요약

시각적 이해와 이미지 생성을 모두 지원하는 대부분의 통합 대규 다중 모달 모델(LMMs)은 여전히 큐레이션된 사후 훈련 감독(curated post-training supervision), 즉 인간 주석(human annotations), 선호도 레이블(preference labels), 또는 외부 보상 모델(external reward models)에 의존합니다. 우리는 통합 LMM이 레이블이 없는 이미지만을 사용하여 두 능력을 모두 자율적으로 향상시킬 수 있는지 질문합니다. 우리는 세 가지 내부 역할을 갖는 자가 진화 훈련 프레임워크를 제안합니다: 시각적 질문을 생성하는 제안자(Proposer), 질문에 답하고 평가하는 해결자(Solver), 그리고 이미지를 합성하는 생성자(Generator). 훈련은 인간 주석, 선호도 레이블, 또는 작업별 훈련된 외부 보상/심사 모델(task-trained external reward/judge models) 없이 오직 자기 유도 일관성 신호(self-derived consistency signals)만을 사용합니다. 학습을 안정화하기 위해, 샘플 수준 일관성이(sample-level consistency) 신뢰할 수 없게 될 때에도 유용하게 남는 토큰 수준 예측 불확실성(token-level prediction uncertainty) 기반의 연속적 난이도 신호인 솔버 토큰 엔트로피(Solver Token Entropy, STE)를 도입합니다. 이미지 생성을 위해, 질문-답변 충실도 점수(question-answer fidelity scoring)와 순환 일관적 캡셔닝(cycle-consistent captioning)을 결합한 다중 스케일 내부 평가 방안을 설계합니다. 이는 더 나은 시각적 이해가 더 신뢰할 수 있는 생성 평가와 더 강력한 내부 훈련 신호를 가능하게 하는 솔버 매개 결합(solver-mediated coupling)을 만듭니다. 이 프레임워크는 확산 기반 BLIP3o, 정류 흐름(rectified-flow) BAGEL, 자기회귀 VARGPT-v1.1 아키텍처 모두에서 동일한 역할 분해, 보상 로직, 훈련 스케줄을 유지하며, 각 백본의 네이티브 프롬프팅 및 생성 인터페이스만을 요구합니다. 여덟 가지 이해 지표에서, 우리의 me

(이하 생략...)

## 원문 영어

<details>
<summary>원문 보기</summary>

Most unified large multimodal models (LMMs) that support both visual understanding and image generation still rely on curated post-training supervision, such as human annotations, preference labels, or external reward models. We ask whether a unified LMM can improve both abilities autonomously using only unlabeled images. We propose a self-evolving training framework with three internal roles: a Proposer that generates visual questions, a Solver that answers and evaluates them, and a Generator t

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2606.27376v1)
