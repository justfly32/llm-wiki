---
title: 세계 행동 모델(World Action Models)을 통한 반복적 생성 리플레이(Recurrent Generative Replays)를 활용한 연속적 모방 학습(Continual Imitation Learning)
created: 2026-06-29
updated: 2026-06-29
type: concept
tags: [research, diffusion]
sources: [raw/papers/world-action-models-enable-continual-imitation-learning-with-2026-06-29.md]
confidence: medium
---

# 세계 행동 모델(World Action Models)을 통한 반복적 생성 리플레이(Recurrent Generative Replays)를 활용한 연속적 모방 학습(Continual Imitation Learning)

> 📄 원문: [World Action Models Enable Continual Imitation Learning with Recurrent Generative Replays](https://arxiv.org/abs/2606.27374v1)
> ✍️ 저자: Manish Kumar Govind, Dominick Reilly, Smit Patel
> 📅 발행: 2026-06-25
> 🏷️ 카테고리: cs.RO, cs.CV

## 요약

로봇 동작 예측을 넘어, 세계 행동 모델(World Action Models, WAMs)은 미래의 시각적 관측값을 생성할 수도 있다. 우리는 이러한 생성 능력에 기반하여 의사 재생 궤적(pseudo-replay trajectories)을 합성하는 지속적 모방 학습 프레임워크인 순환 생성 재생(Recurrent Generative Replay, REGEN)을 제안한다. 이를 통해 로봇 정책은 원본 인간 시연 데이터를 저장하지 않고도 이전에 학습한 과제를 복습할 수 있다. 지속적 적응 과정에서, REGEN은 이전 과제 지시문과 현재 과제 관측값에 조건화된 의사 재생 궤적을 WAM에 순차적으로 질의하여 생성한다. 시뮬레이션 및 실제 조작(manipulation) 환경에서의 실험 결과, REGEN은 순차적 미세조정(sequential fine-tuning) 대비 치명적 망각(catastrophic forgetting)을 최대 50%까지 줄이는 동시에, 실제 재생 데이터에 접근해야 하는 특권적 경험 재생(privileged experience replay) 방법의 성능에 근접하는 것으로 나타났다. 마지막으로, 우리는 생성된 재생의 성능을 제한하는 요인을 분석하여 장기 시각적 열화(long-horizon visual degradation)와 행동-관측 불일치(action-observation inconsistency)가 주요 병목임을 확인했다. 본 연구 결과는 WAM이 저장된 시연 데이터 없이 지속적 로봇 학습을 위한 유망한 기반임을 입증한다.

## 원문 영어

<details>
<summary>원문 보기</summary>

Going beyond predicting robot actions, World Action Models (WAMs) can also generate future visual observations. We build on this generative capability to propose Recurrent Generative Replay (REGEN), a continual imitation learning framework that synthesizes pseudo-replay trajectories, enabling a robot policy to rehearse previously learned tasks without storing their original human demonstrations. During continual adaptation, REGEN recursively queries the WAM to synthesize pseudo-replay trajectori

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2606.27374v1)
