---
title: WARP-RM: 데이터 큐레이션을 위한 Warp 증강 상대적 진행도 보상 모델
created: 2026-06-30
updated: 2026-06-30
type: concept
tags: [research]
sources: [raw/papers/warp-rm-a-warp-augmented-relative-progress-reward-model-for-2026-06-30.md]
confidence: medium
---

# WARP-RM: 데이터 큐레이션을 위한 Warp 증강 상대적 진행도 보상 모델

> 📄 원문: [WARP-RM: A Warp-Augmented Relative Progress Reward Model for Data Curation](https://arxiv.org/abs/2606.28320v1)
> ✍️ 저자: Justin Yu, Andrew Goldberg, Kavish Kondap
> 📅 발행: 2026-06-26
> 🏷️ 카테고리: cs.RO

## 요약

모방 학습의 스케일링에는 대규모 데이터셋이 필요하지만, 인원 원격 조작(teleoperation)은 필연적으로 망설임(hesitation)과 복구(recovery) 동작이 포함된 혼합 품질의 시연(demonstration)을 생성한다. 기존의 프레임 수준 진행 보상(progress reward) 모델은 절대적 시간 진행 프록시에 대해 감독 학습을 수행하는데, 이는 레이블 노이즈의 문제를 겪거나, 하위 작업(subtask) 경계를 정의하기 위해 비용이 많이 드는 수동 주석(human annotation)을 요구한다. 우리는 WARP(Warp-Augmented Relative Progress)를 제시한다. 이는 성공적인 시연으로부터 밀도 높은, 부호화된 상대적 진행 크기(signed relative progress magnitudes)를 완전한 자기 지도 방식(fully self-supervised)으로 학습하는 새로운 알고리즘이다. WARP는 시연의 시간 왜곡 증강(time-warp augmentation, 가변 재생 속도 및 역재생)을 통해 프레임별 진행 타겟을 생성하며, WARP-RM은 입력 프레임 간의 정규화된 경과 시간을 예측하도록 훈련된다. 이 예측을 겹치는 윈도우에 걸쳐 집계하면 밀도 높은 프레임 수준 진행 신호가 산출된다. 이어서 우리는 WARP-BC를 소개한다. 이는 이러한 스칼라 보상 추정치를 활용하여 행동 모방(behavior cloning) 과정에서 고이점(high-advantage) 동작 청크(action chunk)에 가중치를 부여하는 방식으로, 청크 수준의 이점(chunk-level advantage)은 프레임별 보상을 집계하여 얻는다. 우리는 긴 시간 범위(long-horizon)의 변형 가능한 객체(deformable object) 조작 작업인 무작위로 구겨진 상태에서 티셔츠를 개는 작업을 수행하는 물리적 양팔 로봇(bimanual robot) 시스템에서 우리의 접근법을 평가한다. 최적이 아닌 데이터에 대한 정책의 견고성(robustness)을 평가하기 위해, 에피소드 길이를 원격 조작의 비최적성(sub-optimality) 프록시로 사용하여 다양한 품질의 훈련 데이터셋을 구축한다. 데이터셋에 더 많은 비효율성이 포함되도록 확장될수록, WARP-BC는 19/20의 성공률을 유지하는 반면,

(이하 생략...)

## 원문 영어

<details>
<summary>원문 보기</summary>

Scaling imitation learning requires large datasets, yet human teleoperation inevitably produces mixed-quality demonstrations containing hesitations and recoveries. Prior frame-level progress reward models supervise on absolute temporal progress proxies that suffer from label noise, or require costly human annotations to define subtask boundaries. We present WARP (Warp-Augmented Relative Progress), a novel fully self-supervised algorithm for learning dense, signed relative progress magnitudes dir

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2606.28320v1)
