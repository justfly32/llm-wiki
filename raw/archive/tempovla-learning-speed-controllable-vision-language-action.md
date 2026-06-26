---
title: TempoVLA: 속도 제어가 가능한 비전-언어-행동 정책 학습
created: 2026-06-07
updated: 2026-06-07
type: concept
tags: [research, multimodal]
sources: [raw/papers/tempovla-learning-speed-controllable-vision-language-action-2026-06-07.md]
confidence: medium
---

# TempoVLA: 속도 제어가 가능한 비전-언어-행동 정책 학습

> 📄 원문: [TempoVLA: Learning Speed-Controllable Vision-Language-Action Policies](https://arxiv.org/abs/2606.06491v1)
> ✍️ 저자: Dong Jing, Jingchen Nie, Tianqi Zhang
> 📅 발행: 2026-06-04
> 🏷️ 카테고리: cs.RO, cs.AI

## 요약

로봇 조작은 빠른 실행이 요구되는 저위험 이동 단계와 느리고 정밀한 동작이 필요한 고위험 접촉 단계를 반복한다. 그러나 기존의 Vision-Language-Action 모델(VLA)은 학습 시연에서 물려받은 단일 고정 속도만을 사용한다. 모델 압축, KV-cache 재사용, 강화 학습 등을 통해 VLA를 가속화하려는 기존 노력은 정책을 하나의 고정 속도에서 다른 고정 속도로 전환할 뿐이며, 감속은 거의 탐구되지 않았다. 우리는 예측된 각 동작(action)의 크기가 이미 로봇의 이동 속도를 결정한다는 점을 관찰했으며, 이를 통해 제어 가능한 실행 속도로 이어지는 직접적인 경로를 열었다. 우리는 이 관찰을 바탕으로 명시적 조건에 의해 실행 속도가 제어되는 단일 VLA인 TempoVLA를 제안한다. TempoVLA는 두 가지 결합된 구성 요소로 이루어져 있다. (1) 데이터 측의 Variable-Speed Trajectory Augmentation(VSTA): 동작의 의미를 보존하면서 동작을 병합하거나 분할하여 시연을 임의의 목표 속도로 재타이밍한다. (2) 모델 측의 조건 부여 메커니즘: 속도를 정책에 입력으로 제공한다. 통계 분석 결과, VSTA는 미세한 동작 오류만으로 요청된 속도에 도달하는 것으로 나타났다. 시뮬레이션 및 실제 환경 실험에서 TempoVLA는 양방향으로 유연한 속도 제어를 달성하며, VSTA는 더 나은 데이터 활용을 통해 기본 $1\times$ 성능도 향상시킨다. 더 나아대, 대규모 다중 모달 모델과 협력함으로써 TempoVLA는 저위험 단계에서는 가속하고 고위험 단계에서는 감속하는 동적 속도 제어를 실현한다.

(이하 생략...)

## 원문 영어

<details>
<summary>원문 보기</summary>

Robot manipulation alternates between low-risk transit phases that call for fast execution and high-risk contact stages that demand slow, precise motion. Yet existing Vision-Language-Action models (VLAs) only inherit a single fixed speed from training demonstrations. Prior efforts to accelerate VLAs through model compression, KV-cache reuse, or reinforcement learning only shift the policy from one fixed speed to another, and leave deceleration almost unexplored. We observe that the magnitude of 

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2606.06491v1)
