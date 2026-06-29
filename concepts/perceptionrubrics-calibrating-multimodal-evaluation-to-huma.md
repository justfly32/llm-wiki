---
title: PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception
created: 2026-06-30
updated: 2026-06-30
type: concept
tags: [research, multimodal, agent]
sources: [raw/papers/perceptionrubrics-calibrating-multimodal-evaluation-to-huma-2026-06-30.md]
confidence: medium
---

# PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception

> 📄 원문: [PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception](https://arxiv.org/abs/2606.28322v1)
> ✍️ 저자: Yana Wei, Hongbo Peng, Yanlin Lai
> 📅 발행: 2026-06-26
> 🏷️ 카테고리: cs.CV

## 요약

우리는 포화된 벤치마크 점수와 실제 환경의 취약성(brittleness) 사이의 간극을 해결하기 위한 루브릭 기반 평가 프레임워크인 PerceptionRubrics를 소개합니다. 전체론적 의미 매칭(holistic semantic matching) 평가에서 엄밀한 원자적 감사(atomic auditing)로 평가 방식을 전환한 PerceptionRubrics는 1,038개의 정보 밀집 이미지를 12,000개 이상의 인스턴스별 루브릭과 짝지어 제공합니다. 이 기준들은 새로운 순환 동료 합의(Circular Peer-Review) 파이프라인을 통해 구성된 골든 캡션(golden captions)에서 도출된 후, 필수 사실(Must-Right)과 세부 오류(Easy-Wrong) 루브릭의 이중 스트림(dual-stream) 시스템으로 정제됩니다. 특히 중요한 점은, PerceptionRubrics이 게이티드 스코어링(Gated Scoring) 메커니즘을 구현한다는 것입니다: 선형 평균과 달리, 필수 시각적 사실에서의 실패는 날카로운 이진 페널티를 유발합니다. 광범위한 평가를 통해 다음과 같은 핵심 인사이트를 도출했습니다: (1) 신뢰성 격차(Reliability Gap): 모델이 파편화된 요소를 올바르게 검증하면서도 엄격한 논리곱 제약(conjunctive constraints)에서 실패하는 경우가 많아, 밀집 도메인에서의 취약성이 드러남; (2) 오픈-클로즈드 계층화(Open-Closed Stratification): 추세와 달리, 오픈소스와 독점 프론티어 모델 간에 지속적인 8% 인지 격차가 존재함을 밝힘; (3) 인간 정렬 엄밀성(Human-Aligned Rigor): 게이티드 메트릭이 기존 벤치마크와 실질적으로 더 높은 정렬도를 보여주며, 엄밀한 지각 충실도(perceptual fidelity)가 신뢰할 수 있는 생성의 전제 조건임을 입증함.

## 원문 영어

<details>
<summary>원문 보기</summary>

We introduce PerceptionRubrics, a rubric-based evaluation framework that addresses the gap between saturated benchmark scores and real-world brittleness. Shifting evaluation from holistic semantic matching to rigorous atomic auditing, PerceptionRubrics pairs 1,038 information-dense images with over 12,000 instance-specific rubrics. These criteria are derived from golden captions constructed via a novel Circular Peer-Review consensus pipeline and then distilled into a dual-stream system of Must-R

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2606.28322v1)
