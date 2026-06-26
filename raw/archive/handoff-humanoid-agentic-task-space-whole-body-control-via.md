---
title: HANDOFF: 증류된 상보적 교사(Distilled Complementary Teachers)를 통한 휴머노이드 에이전틱 태스크-스페이스 전신 제어(Humanoid Agentic Task-Space Whole-Body Control)
created: 2026-06-07
updated: 2026-06-07
type: concept
tags: [research, alignment, agent]
sources: [raw/papers/handoff-humanoid-agentic-task-space-whole-body-control-via-2026-06-07.md]
confidence: medium
links: [robodream-compositional-world-models-for-scalable-robot-dat, tempovla-learning-speed-controllable-vision-language-action, newtphys-do-foundation-models-understand-newtonian-physics, riskflow-fast-and-faithful-safety-critical-traffic-scenario]
---

# HANDOFF: 증류된 상보적 교사(Distilled Complementary Teachers)를 통한 휴머노이드 에이전틱 태스크-스페이스 전신 제어(Humanoid Agentic Task-Space Whole-Body Control)

> 관련: [[robodream-compositional-world-models-for-scalable-robot-dat|RoboDream]], [[tempovla-learning-speed-controllable-vision-language-action|TempoVLA]], [[riskflow-fast-and-faithful-safety-critical-traffic-scenario|RiskFlow]]도 참고하세요.

> 📄 원문: [HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers](https://arxiv.org/abs/2606.06493v1)
> ✍️ 저자: Lizhi Yang, Junheng Li, Nehar Poddar
> 📅 발행: 2026-06-04
> 🏷️ 카테고리: cs.RO, cs.AI, cs.LG

## 요약

인간형 로봇을 실제 환경에 배치하기 위해서는 명령 공간(즉, 작업 계획과 전신 제어 사이의 인터페이스)의 선택이 매우 중요합니다. 기존의 전신 제어기(whole-body controller)는 일반적으로 계획기가 작업 의미론(task semantics)으로부터 생성하기 어려운 고밀도 운동학적 또는 공간적 참조를 요구합니다. 우리는 대신 직관적이고, 범용적이며, 모듈식이고, 다양한 조작 기술을 표현할 수 있을 만큼 충분한 간결하고 명시적인 인터페이스를 제안합니다. 이를 위해, 우리는 HANDOFF를 소개합니다. HANDOFF는 이 인터페이스를 따르는 단일 인간형 전신 제어기로, 맥락 조건부 게이팅 스킴(context-conditioned gating scheme) 하에서 세 가지 상호 보완적인 전문가들—안전 필터링된 데이터를 사용한 전신 운동 추적, 보행(locomotion), 그리고 낙상 복구(fall-recovery)—으로부터 다중 교사 KL 증류(multi-teacher KL distillation)를 통해 전문가 혼합(mixture-of-experts) 학생 모델로 증류되었습니다. Unitree G1에서 HANDOFF는 최첨단 속도 추적 성능을 달성하며, 가장 넓은 강건한 조작 작업 공간 중 하나를 제공합니다. 또한, 작업별 데이터나 제어기 미세 조정(fine-tuning) 없이 VLM 기반 에이전틱 계획기(VLM-driven agentic planner)에 의해 구동되는 여러 자연어 기반 작업 수행을 통해 하드웨어 실현 가능성을 추가로 입증했습니다.

## 원문 영어

<details>
<summary>원문 보기</summary>

For a humanoid robot to be deployed in the real world, the choice of command space (i.e., the interface between task planning and whole-body control) is crucial. Existing whole-body controllers typically demand dense kinematic or spatial references that planners struggle to synthesize from task semantics. We instead propose a compact, explicit interface that is intuitive, general, modular, and expressive enough for diverse manipulation skills. To this end, we introduce HANDOFF, a single humanoid

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2606.06493v1)
