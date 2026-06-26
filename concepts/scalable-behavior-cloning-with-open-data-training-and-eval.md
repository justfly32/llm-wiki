---
title: 오픈 데이터, 훈련, 평가를 통한 확장 가능한 행동 클로닝
created: 2026-06-27
updated: 2026-06-27
type: concept
tags: [research, multimodal, diffusion]
sources: [raw/papers/scalable-behavior-cloning-with-open-data-training-and-eval-2026-06-27.md]
confidence: medium
---

# 오픈 데이터, 훈련, 평가를 통한 확장 가능한 행동 클로닝

> 📄 원문: [Scalable Behavior Cloning with Open Data, Training, and Evaluation](https://arxiv.org/abs/2606.27375v1)
> ✍️ 저자: Arthur Allshire, Himanshu Gaurav Singh, Ritvik Singh
> 📅 발행: 2026-06-25
> 🏷️ 카테고리: cs.RO

## 요약

우리는 behavior cloning을 활용한 조작을 위한 완전한 오픈소스 스택인 ABC를 소개합니다. 그 핵심은 195가지 다양한 작업에 걸쳐 130K 이상의 에피소드, 총 3,500시간의 데이터를 포함하는 현재까지 가장 규모가 큰 오픈소스 teleoperation 데이터셋인 ABC-130K입니다. 또한, 접근 가능한 하드웨어 설정, training infrastructure, 그리고 simulation pipeline도 오픈소스로 공개합니다. 나아가 400시간의 sim-teleop 데이터를 공개하고, 시뮬레이션과 실세계 평가 간의 상관성을 확보한 co-training recipe를 제공하여 비용이 많이 드는 실세계 평가 이전에 model-design 및 training decision을 ablating하기 위한 신뢰할 수 있는 proxy를 제공합니다. 우리는 다양한 training recipe를 탐구하고 Diffusion Transformers (DiT) 및 Vision-Language-Action (VLA) 모델에 대한 일반적인 architectural choice를 비교하며, 그 결과를 실세계 평가에 기반하여 도출합니다. 이를 통해 얻어진 policy는 상자 접기(box folding)나 지갑에서 신용카드 추출하기와 같은 정교한 작업을 성공적으로 수행합니다. 재현 가능한 toolkit을 제공함으로써, 연구자들이 동일한 출발선에 설 수 있도록 하여 공동체가 함께 Behavior Cloning의 ABC를 배울 수 있는 필수적인 기반을 마련하고자 합니다.

## 원문 영어

<details>
<summary>원문 보기</summary>

We introduce ABC, a fully open-source stack for manipulation with behavior cloning. At its core is ABC-130K: the largest open-source teleoperation dataset to date, featuring 3,500 hours of data spanning over 130K episodes across 195 diverse tasks. Furthermore, we open-source our accessible hardware setup, training infrastructure, and simulation pipeline. We also release 400 hours of sim-teleop data and provide a co-training recipe that produces correlated simulation and real-world evaluation, of

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2606.27375v1)
