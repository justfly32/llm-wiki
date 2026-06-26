---
title: 세계 행동 모델을 통한 순환적 생성 재생을 활용한 지속적 모방 학습
created: 2026-06-27
updated: 2026-06-27
type: concept
tags: [research, diffusion]
sources: [raw/papers/world-action-models-enable-continual-imitation-learning-with-2026-06-27.md]
confidence: medium
---

# 세계 행동 모델을 통한 순환적 생성 재생을 활용한 지속적 모방 학습

> 📄 원문: [World Action Models Enable Continual Imitation Learning with Recurrent Generative Replays](https://arxiv.org/abs/2606.27374v1)
> ✍️ 저자: Manish Kumar Govind, Dominick Reilly, Smit Patel
> 📅 발행: 2026-06-25
> 🏷️ 카테고리: cs.RO, cs.CV

## 요약

로봇 동작 예측을 넘어서, World Action Models (WAMs)는 미래의 시각적 관측값을 생성할 수도 있다. 우리는 이 생성 능력을 활용하여, 이전에 학습한 과제를 원본 인간 시연 데이터를 저장하지 않고도 로봇 정책이 이를 복습할 수 있도록 의사 재생 경로(pseudo-replay trajectories)를 합성하는 지속적 모방 학습 프레임워크인 Recurrent Generative Replay (REGEN)를 제안한다. 지속적 적응 과정에서 REGEN은 이전 과제 명령어와 현재 과제의 관측값만을 조건으로 WAM에 반복적으로 질의하여 의사 재생 경로를 합성한다. 시뮬레이션과 실제 조작 환경 모두에서의 실험 결과, REGEN은 순차적 미세 조정 대비 치명적 망각(catastrophic forgetting)을 최대 $50\%$까지 줄이는 것으로 나타났으며, 실제 재생 데이터에 접근해야 하는 특권 경험 재생(privileged experience replay) 방법들의 성능에 근접하였다. 마지막으로, 생성된 재생의 성능을 제한하는 요인을 분석하여 장기 시각적 열화(long-horizon visual degradation)와 동작-관측 불일치(action-observation inconsistency)가 주요 병목임을 확인하였다. 우리의 결과는 저장된 시연 데이터 없이도 WAM이 지속적 로봇 학습을 위한 유망한 기반이 될 수 있음을 입증한다.

## 원문 영어

<details>
<summary>원문 보기</summary>

Going beyond predicting robot actions, World Action Models (WAMs) can also generate future visual observations. We build on this generative capability to propose Recurrent Generative Replay (REGEN), a continual imitation learning framework that synthesizes pseudo-replay trajectories, enabling a robot policy to rehearse previously learned tasks without storing their original human demonstrations. During continual adaptation, REGEN recursively queries the WAM to synthesize pseudo-replay trajectori

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2606.27374v1)
