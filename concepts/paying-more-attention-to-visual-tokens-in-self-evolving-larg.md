---
title: 자기 진화 대규다중양모델(Self-Evolving Large Multimodal Models)에서 시각적 토큰(Visual Tokens)에 더 많은 주의 기울이기
created: 2026-06-29
updated: 2026-06-29
type: concept
tags: [research, programming, multimodal, agent]
sources: [raw/papers/paying-more-attention-to-visual-tokens-in-self-evolving-larg-2026-06-29.md]
confidence: medium
---

# 자기 진화 대규다중양모델(Self-Evolving Large Multimodal Models)에서 시각적 토큰(Visual Tokens)에 더 많은 주의 기울이기

> 📄 원문: [Paying More Attention to Visual Tokens in Self-Evolving Large Multimodal Models](https://arxiv.org/abs/2606.27373v1)
> ✍️ 저자: Shravan Venkatraman, Ritesh Thawkar, Omkar Thawakar
> 📅 발행: 2026-06-25
> 🏷️ 카테고리: cs.CV

## 요약

최근, 순전히 비지도 설정에서 시각적 추론을 개선하기 위한 자기 진화 대규모 다중 모달 모델(self-evolving LMMs)이 주목받고 있다. 그러나 기존 자기 진화 LMM에서 사용되는 다중 역할 셀프플레이(multi-role self-play)와 자기 일관성 보상(self-consistency reward) 방식은 디코더가 시각적 콘텐츠에 주의를 기울이도록 보장하지 않고 답변 일관성만을 최적화하며, 대신 통계적 언어 사전 지식(language priors)에 의존하여 자기 일관된 출력을 생성한다. 이는 디코더가 생성 과정에서 이미지가 아닌 언어 사전 지식에 의존하게 만드는 지속적인 실패 모드인 시각적 과소 조건화(visual under-conditioning)로 이어지며, 시각 토큰에 대한 불충분한 주의로 나타난다. 그 결과, 현재의 자기 진화 LMM은 이미지 캡셔닝 및 시각적 질의응답과 같은 비전-언어 이해 과제에서 어려움을 겪고 있다. 이를 해결하기 위해, 우리는 VISE(Visual Invariance Self-Evolution)를 제안한다. 이는 순전히 비지도 자기 진화 프레임워크로, 두 가지 상호 보완적인 불변성 기반 보상을 통해 모델의 시각적 조건화 정책(visual conditioning policy)을 직접적으로 정규화한다: 알려진 변환 하에서 공간적 일관성을 강제하는 기하학적 불변성 보상(geometric invariance reward)과, 예측된 영역이 교란될 때 증거 부재를 인식하도록 요구하여 증거 무관적 생성(evidence-agnostic generation)을 페널티하는 의미론적 불변성 보상(semantic invariance reward)이다. VISE는 전문가 역할(specialist roles), 외부 보상 모델(external reward models), 또는 어노테이션(annotations) 없이 단일 모델 내에서 작동하며, 원시 레이블 없는 이미지(raw unlabeled images)로 훈련된다. 18개 벤치마크에서의 실험은 우리 접근법의 효과를 입증한다. Qwen3-VL-2B를 사용하여

(이하 생략...)

## 원문 영어

<details>
<summary>원문 보기</summary>

Recently, self-evolving large multimodal models (LMMs) have received attention for improving visual reasoning in a purely unsupervised setting. However, multi-role self-play and self-consistency reward schemes in existing self-evolving LMMs optimize answer agreement without ensuring the decoder attends to visual content, relying instead on statistical language priors to produce self consistent outputs. This leads to a persistent failure mode we term visual under-conditioning, where the decoder r

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2606.27373v1)
