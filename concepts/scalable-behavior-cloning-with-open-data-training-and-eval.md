---
title: 공개 데이터, 련  평가를 활용한 확장 가능한 행동 복제(Scalable Behavior Cloning)
created: 2026-06-29
updated: 2026-06-29
type: concept
tags: [research, multimodal, diffusion]
sources: [raw/papers/scalable-behavior-cloning-with-open-data-training-and-eval-2026-06-29.md]
confidence: medium
---

# 공개 데이터, 련  평가를 활용한 확장 가능한 행동 복제(Scalable Behavior Cloning)

> 📄 원문: [Scalable Behavior Cloning with Open Data, Training, and Evaluation](https://arxiv.org/abs/2606.27375v1)
> ✍️ 저자: Arthur Allshire, Himanshu Gaurav Singh, Ritvik Singh
> 📅 발행: 2026-06-25
> 🏷️ 카테고리: cs.RO

## 요약

우리는 행동 클로닝(behavior cloning)을 위한 완전한 오픈소스 스택인 ABC를 소개합니다. ABC의 핵심은 ABC-130K로, 이는 현재까지 가장 큰 오픈소스 원격조작(teleoperation) 데이터셋으로, 195가지 다양한 작업에 걸쳐 130K 이상의 에피소드에 걸친 3,500시간의 데이터를 포함하고 있습니다. 또한 접근 가능한 하드웨어 셋업, 훈련 인프라, 시뮬레이션 파이프라인을 오픈소스로 공개합니다. 400시간의 시뮬레이션 원격조작(sim-teleop) 데이터도 공개하며, 시뮬레이션과 실제 환경 평가 간에 상관관계를 갖는 공동 훈련(co-training) 레시피를 제공하여 비용이 많이 드는 실제 환경 평가에 앞서 모델 설계 및 훈련 결정을 검증(ablating)할 수 있는 신뢰할 수 있는 대안을 제시합니다. 우리는 다양한 훈련 레시피를 탐구하고 디퓨전 트랜스포머(Diffusion Transformers, DiT) 및 비전-언어-행동(Vision-Language-Action, VLA) 모델에 대한 일반적인 아키텍처 선택을 비교하며, 실제 환경 평가를 바탕으로 연구 결과를 입증합니다. 이를 통해 얻은 정책(policies)은 상자 접기나 지갑에서 신용카드 꺼내기 같은 정교한 작업을 성공적으로 수행합니다. 재현 가능한 툴킷을 제공함으로써, 연구자들이 동등한 위치에서 연구할 수 있도록 하여 공동체가 함께 행동 클로닝(Behavior Cloning)의 ABC를 배울 수 있는 필수적인 기반을 마련하고자 합니다.

## 원문 영어

<details>
<summary>원문 보기</summary>

We introduce ABC, a fully open-source stack for manipulation with behavior cloning. At its core is ABC-130K: the largest open-source teleoperation dataset to date, featuring 3,500 hours of data spanning over 130K episodes across 195 diverse tasks. Furthermore, we open-source our accessible hardware setup, training infrastructure, and simulation pipeline. We also release 400 hours of sim-teleop data and provide a co-training recipe that produces correlated simulation and real-world evaluation, of

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2606.27375v1)
