---
title: 센서에 목소리를 부여하다: 시맨틱 시계열 임베딩을 위한 멀티모달 JEPA
created: 2026-06-02
updated: 2026-06-02
type: concept
tags: [research, programming, multimodal]
sources: [raw/papers/giving-sensors-a-voice-multimodal-jepa-for-semantic-time-se-2026-06-02.md]
confidence: medium
---

# 센서에 목소리를 부여하다: 시맨틱 시계열 임베딩을 위한 멀티모달 JEPA

> 📄 원문: [Giving Sensors a Voice: Multimodal JEPA for Semantic Time-Series Embeddings](https://arxiv.org/abs/2605.31580v1)
> ✍️ 저자: Utsav Dutta, Gerardo Pastrana, Sina Khoshfetrat Pakazad
> 📅 발행: 2026-05-29
> 🏷️ 카테고리: cs.LG

## 요약

트랜스포머 기반 아키텍처는 언어 및 비전 분야에서 시퀀스 모델링을 크게 발전시켰지만, 이기적 다변량 시계열 데이터에 대한 범용 표현 학습은 아직 충분히 탐구되지 않았다. 우리는 채널 수준의 텍스트 설명을 채널 순서에 동등한(equivariant) 트랜스포머 인코더에 통합하는 CHARM(Channel-Aware Representation Model)을 제안한다. CHARM은 Joint Embedding Predictive Architecture(JEPA)와 정보가 풍부하고 시간적으로 안정적인 임베딩을 유도하는 새로운 손실 함수로 학습된다. 잠재 공간 예측은 센서 노이즈에 대한 강건성을 장려하며, 설명 인식 게이팅(description-aware gating)은 학습된 채널 간 관계를 통해 해석 가능성을 제공한다. 이상 탐지(anomaly detection), 분류(classification), 단기 및 장기 예측(short- and long-term forecasting) 전반에 걸쳐, 학습된 임베딩은 선형 프로브(linear probe)만으로도 강력한 성능을 달성한다. 성능은 주로 JEPA 목적 함수와 조건부 아키텍처에 의해 주도되며, 텍스트 설명은 데이터셋 간 일반화를 위한 채널 식별자 역할을 한다.

## 원문 영어

<details>
<summary>원문 보기</summary>

Transformer-based architectures have advanced sequence modeling in language and vision, yet general-purpose representation learning for heterogeneous multivariate time series remains underexplored. We introduce CHARM (Channel-Aware Representation Model), which incorporates channel-level textual descriptions into a Transformer encoder equivariant to channel order. CHARM is trained with a Joint Embedding Predictive Architecture (JEPA) and a novel loss promoting informative, temporally stable embed

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2605.31580v1)
