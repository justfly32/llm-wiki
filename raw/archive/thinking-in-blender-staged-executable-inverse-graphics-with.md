---
title: Blender에서의 사고: 비전-언어 모델을 활용한 단계적 실행 가능 역 그래픽스
created: 2026-06-03
updated: 2026-06-03
type: concept
tags: [research, ai-ml, programming, multimodal, agent]
sources: [raw/papers/thinking-in-blender-staged-executable-inverse-graphics-with-2026-06-03.md]
confidence: medium
---

# Blender에서의 사고: 비전-언어 모델을 활용한 단계적 실행 가능 역 그래픽스

> 📄 원문: [Thinking in Blender: Staged Executable Inverse Graphics with Vision-Language Models](https://arxiv.org/abs/2606.02580v1)
> ✍️ 저자: Guangzhao He, Rundong Luo, Wei-Chiu Ma
> 📅 발행: 2026-06-01
> 🏷️ 카테고리: cs.CV

## 요약

인버스 그래픽스(inverse graphics)는 이미지를 렌더링, 조명 재설정, 조작이 가능한 편집 가능한 3D 장면으로 재구성하고자 하는 오래된 동시에 매우 제약이 적은 문제이다. 본 연구에서는 사전 학습된 비전-언어 모델(VLMs)이 특화된 2D 또는 3D 파운데이션 모델, 미분 가능한 렌더링(differentiable rendering), 또는 다중 뷰 감독(multi-view supervision)에 의존하지 않고, 단일 이미지로부터 편집 가능한 블렌더(Blender) 프로그램으로 장면을 재구성하여 실행 가능한 인버스 그래픽스를 직접 수행할 수 있는지 조사한다. 우리는 단계별 실행 가능한 인버스 그래픽스(Staged Executable Inverse Graphics, SEIG)를 제안한다. 이는 기하학, 재료, 구성, 조명 등 장면 요소를 실행 가능한 블렌더 코드 공간에서 점진적으로 정제하여 단일 이미지로부터 3D 장면을 재구성하는 에이전틱(agentic) 프레임워크이다. 우리는 픽셀 수준, 지각적(perceptual), 의미론적(semantic) 충실도를 아우르는 다양한 재구성 메트릭을 사용하여 다양한 장면에서 프레임워크를 평가한다. 실험 결과, 단계별 재구성이 재구성 충실도를 크게 향상시키며, 범용 VLM을 활용한 실행 가능한 인버스 그래픽스에서 작업 분해(task decomposition)의 중요성을 강조한다. 마지막으로, 재구성된 편집 가능한 블렌더 장면을 통해 가능한 다양한 다운스트림 애플리케이션을 보여준다.

## 원문 영어

<details>
<summary>원문 보기</summary>

Inverse graphics is a longstanding and highly underconstrained problem that seeks to reconstruct images as editable 3D scenes which can be rendered, relit, and manipulated. In this work, we investigate whether pretrained vision-language models (VLMs) can perform executable inverse graphics directly from a single image by reconstructing a scene as an editable Blender program, without relying on specialized 2D or 3D foundation models, differentiable rendering, or multi-view supervision. We introdu

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2606.02580v1)
