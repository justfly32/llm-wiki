---
title: 상상력 기반 인지 토큰(Imaginative Perception Tokens)이 다중 모달 언어 모델(Multimodal Language Models)의 공간 추론(Spatial Reasoning)을 향상시킨다
created: 2026-06-04
updated: 2026-06-04
type: concept
tags: [research, ai-ml, optimization, multimodal, agent]
sources: [raw/papers/imaginative-perception-tokens-enhance-spatial-reasoning-in-m-2026-06-04.md]
confidence: medium
---

# 상상력 기반 인지 토큰(Imaginative Perception Tokens)이 다중 모달 언어 모델(Multimodal Language Models)의 공간 추론(Spatial Reasoning)을 향상시킨다

> 📄 원문: [Imaginative Perception Tokens Enhance Spatial Reasoning in Multimodal Language Models](https://arxiv.org/abs/2606.03988v1)
> ✍️ 저자: Mahtab Bigverdi, Lindsey Li, Weikai Huang
> 📅 발행: 2026-06-02
> 🏷️ 카테고리: cs.AI

## 요약

비전 언어 모델(VLMs)은 다양한 작업에서 뛰어난 성능을 보이지만, 핵심 정보가 직접 관찰되지 않는 경우 공간 추론에서 여전히 한계를 보인다. 이러한 문제들 중 상당수는 상상적 지각(imaginative perception)을 요구한다: 보이지 않는 시점에서 무엇이 보일지를 추론하거나, 가려진 공간을 따라 경로를 추적하거나, 부분적인 관찰을 일관된 공간 표현으로 통합하는 것 등이다. 우리는 관찰된 입력과의 일관성을 유지하면서도 대안적 공간 구성 하에서 VLM이 지각할 수 있는 내용을 외부화한 중간 지각 표현인 상상적 지각 토큰(Imaginative Perception Tokens, IPT)을 제안한다. 이 능력을 연구하기 위해, 우리는 시점 전환(Perspective Taking, PET), 경로 추적(Path Tracing, PT), 다시점 계수(Multiview Counting, MVC)의 세 가지 과제를 정의하고, 정답 기반 상상, 정답, 평가 벤치마크를 포함한 약 2만 개의 예시로 구성된 데이터셋을 구축했다. 통합 VLM인 BAGEL을 백본으로 사용하여 IPT 감독은 공간 추론 성능을 일관되게 향상시켰으며, 추론 시 이미지를 생성하지 않더라도 텍스트 기반 사고 연쇄(chain of thought) 훈련보다 우수한 결과를 보였다. MVC에서 IPT는 정확도를 3.4%p 향상시켰고, PT에서는 강력한 폐쇄형 소스 모델과 경쟁력 있는 성능을 달성했다. 또한 IPT와 레이블 전용 감독을 결합하면 추가적인 성능 향상이 나타났으며, 반면 텍스트 기반 사고 연쇄는 성능을 크게 저하시켜, 공간 계산이 언어를 통해 강제될 때 양식 불일치(modality mismatch)가 발생함을 시사한다. 종합적으로, IPT는 관찰되지 않은 공간에 대한 추론을 위한 원리적인 감독 신호를 제공한다.

(이하 생략...)

## 원문 영어

<details>
<summary>원문 보기</summary>

Vision language models (VLMs) excel at many tasks but still struggle with spatial reasoning when critical information is not directly observable. Many such problems require imaginative perception: inferring what would be seen from an unseen viewpoint, tracing paths through occluded spaces, or integrating partial observations into a coherent spatial representation. We introduce Imaginative Perception Tokens (IPT), intermediate perceptual representations that externalize what a VLM would perceive 

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2606.03988v1)
