---
title: NewtPhys: 파운데이션 모델(Foundation Models)은 뉴턴 역학(Newtonian Physics)을 이해하는가?
created: 2026-06-04
updated: 2026-06-04
type: concept
tags: [research, programming, multimodal, agent]
sources: [raw/papers/newtphys-do-foundation-models-understand-newtonian-physics-2026-06-04.md]
confidence: medium
links: [functional-attention-from-pairwise-affinities-to-functional, imaginative-perception-tokens-enhance-spatial-reasoning-in-m, robodream-compositional-world-models-for-scalable-robot-dat, tempovla-learning-speed-controllable-vision-language-action]
---

# NewtPhys: 파운데이션 모델(Foundation Models)은 뉴턴 역학(Newtonian Physics)을 이해하는가?

> 관련: [[functional-attention-from-pairwise-affinities-to-functional|기능적 어텐션]], [[robodream-compositional-world-models-for-scalable-robot-dat|RoboDream]], [[imaginative-perception-tokens-enhance-spatial-reasoning-in-m|상상력 기반 인지 토큰]]도 참고하세요.

> 📄 원문: [NewtPhys: Do Foundation Models Understand Newtonian Physics?](https://arxiv.org/abs/2606.03986v1)
> ✍️ 저자: Sebastian Cavada, Soumava Paul, Tuan-Hung Vu
> 📅 발행: 2026-06-02
> 🏷️ 카테고리: cs.CV

## 요약

이전 연구들은 합성 또는 반합성 장면과 시각 질의응답(visual question-answering) 과제를 활용하여 파운데이션 모델(foundation model)의 물리적 추론 능력을 평가해 왔다. 그러나 이러한 벤치마크들은 고수준 이벤트에 치중하며, 진정한 저수준 뉴턴역학적 이해를 평가하는 데 필요한 시충실도(visual fidelity)가 부족하다. 우리는 실제 장면의 다시점(multiview) 이미지와 물리 기반 시뮬레이션으로 구축된 4D 물리 주석 데이터셋인 NewtPhys를 소개한다. 이 데이터셋은 시간 단계(timestep)에 걸쳐 밀도 높고 세밀한 주석을 제공하며, 3D 힘(3D forces)과 물리, 추적(tracking), 의미론(semantics), 기하학(geometry)을 포함하는 아모달(amodal) 픽셀 단위 수치를 포함하여 단순한 합성 환경과 현실적인 시각적 복잡성 사이의 간극을 메운다. NewtPhys를 활용하여, 우리는 54개의 오픈 가중치(open-weight) 모델과 2개의 폐쇄형 최첨단(closed-source frontier) 모델을 포함한 총 56개의 시각-언어 모델(VLM)과 10개의 비디오 파운데이션 모델(VFM)을 체계적으로 평가하고, 저수준 물리적 추론에서의 한계를 밝혀냈다. 벤치마크를 넘어, 우리의 데이터셋은 물리 기반 비전(physics-grounded vision) 분야의 향후 연구와 차세대 물리 인식 평가(physics-aware evaluation) 개발을 가능하게 한다. 코드와 데이터셋은 https://astra-vision.github.io/NewtPhys에서 이용할 수 있다.

## 원문 영어

<details>
<summary>원문 보기</summary>

Previous work has evaluated physics reasoning in foundation models using synthetic or semi-synthetic scenes and visual question-answering tasks. However, these benchmarks emphasize high-level events and lack the visual fidelity required to assess true low-level Newtonian understanding. We introduce NewtPhys, a 4D physically annotated dataset built from multiview images of real-world scenes with physics-grounded simulations. The dataset provides dense, fine-grained annotations across timesteps --

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2606.03986v1)
