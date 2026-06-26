---
title: 로보드림(RoboDream): 확장 가능한 로봇 데이터 합성을 위한 구성적 세계 모델(Compositional World Models)
created: 2026-06-03
updated: 2026-06-03
type: concept
tags: [research, multimodal, diffusion]
sources: [raw/papers/robodream-compositional-world-models-for-scalable-robot-dat-2026-06-03.md]
confidence: medium
links: [newtphys-do-foundation-models-understand-newtonian-physics, tempovla-learning-speed-controllable-vision-language-action, handoff-humanoid-agentic-task-space-whole-body-control-via, thinking-in-blender-staged-executable-inverse-graphics-with]
---

# 로보드림(RoboDream): 확장 가능한 로봇 데이터 합성을 위한 구성적 세계 모델(Compositional World Models)

> 관련: [[newtphys-do-foundation-models-understand-newtonian-physics|NewtPhys]], [[tempovla-learning-speed-controllable-vision-language-action|TempoVLA]], [[handoff-humanoid-agentic-task-space-whole-body-control-via|HANDOFF]]도 참고하세요.

> 📄 원문: [RoboDream: Compositional World Models for Scalable Robot Data Synthesis](https://arxiv.org/abs/2606.02577v1)
> ✍️ 저자: Junjie Ye, Rong Xue, Basile Van Hoorick
> 📅 발행: 2026-06-01
> 🏷️ 카테고리: cs.RO, cs.CV

## 요약

로봇 학습의 확장에는 대규모이고 다양한 시연 데이터가 필요하지만, 원격 조작(teleoperation)을 통한 실제 데이터 수집은 여전히 비용이 많이 들고 시간이 오래 걸린다. 비디오 확산 모델(video diffusion models)은 데이터 확장에 유망한 방법을 제공하지만, 기존의 생성 접근법은 표면적인 시각적 증강에 그치거나, 물리적으로 실현 불가능한 동작을 초래하는 엠보디먼트 할루시네이션(embodiment hallucinations) 문제를 겪는다. 우리는 일반화 가능한 엠보디먼트 중심 세계 모델(embodiment-centric world model)을 제시하며, 이 모델은 새로운 물체, 새로운 장면, 새로운 시점에서 사실적인 시연 데이터를 합성함으로써 확장 가능한 데이터 생성을 달성한다. 우리의 접근법은 렌더링된 로봇 동작에 생성을 고정하면서 명시적인 장면 및 물체 사전 정보(scene and object priors)를 조건으로 설정하여 궤적 실행과 환경 합성을 효과적으로 분리한다. 이러한 구성은 두 가지 강력한 데이터 확장 기능을 가능하게 할 잠재력을 지닌다: (1) 기존 궤적을 새로운 맥락에서 새로운 동작 데이터 없이 재활용하는 '검색 및 재탄생(retrieval and rebirth)', 그리고 (2) 조작자가 빈 공간을 조작하면 모델이 이후 대상 물체와 장면을 생성하는 '프롭 없는 원격 조작(prop-free teleoperation)'으로, 이를 통해 리셋 시간을 제거할 수 있다. 실제 실험을 통해 생성된 데이터가 다양한 조작 과제에서 하위 정책(policy) 성능을 일관되게 향상시키고 실제 데이터 요구량을 크게 줄인다는 것을 보여준다.

## 원문 영어

<details>
<summary>원문 보기</summary>

Scaling robot learning requires large-scale, diverse demonstrations, yet real-world data collection via teleoperation remains prohibitively expensive and time-consuming. While video diffusion models offer a promising avenue for data scaling, existing generative approaches are often limited to superficial visual augmentation, or suffer from embodiment hallucinations that yield physically infeasible motions. We present a generalizable embodiment-centric world model that achieves scalable data gene

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2606.02577v1)
