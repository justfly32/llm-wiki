---
title: 무엇이 가장 먼저 드러나는가? 그래프-텍스트 생성을 위한 확산 모델(Diffusion Models)의 궤적 분석
created: 2026-06-02
updated: 2026-06-02
type: concept
tags: [research, ai-ml, programming, optimization, diffusion]
sources: [raw/papers/what-gets-unmasked-first-trajectory-analysis-of-diffusion-m-2026-06-02.md]
confidence: medium
---

# 무엇이 가장 먼저 드러나는가? 그래프-텍스트 생성을 위한 확산 모델(Diffusion Models)의 궤적 분석

> 📄 원문: [What Gets Unmasked First? Trajectory Analysis of Diffusion Models for Graph-to-Text Generation](https://arxiv.org/abs/2605.31564v1)
> ✍️ 저자: Qing Wang, Jacob Devasier, Chengkai Li
> 📅 발행: 2026-05-29
> 🏷️ 카테고리: cs.CL, cs.AI

## 요약

그래프-텍스트 생성(graph-to-text generation)을 위한 마스킹 확산 언어 모델(Masked Diffusion Language Models, MDLMs)의 최초의 체계적 연구를 제시합니다. 우리는 MDLM 생성 궤적(iterative decoding 과정에서 토큰이 마스크 해제되는 순서)을 분석한 결과, 텍스트를 선형적으로 생성하는 자동회귀 대규모 언어 모델(autoregressive LLMs)과 달리, MDLM은 엔티티를 먼저 생성한 뒤 관계 및 기능어를 생성하고, 마지막으로 구조적 토큰을 해결하는 경향이 있음을 발견했습니다. 또한, 감독 미세 조정(supervised fine-tuning, SFT)의 이전에 보고되지 않았던 실패 모드를 추가로 확인했습니다: SFT는 디코딩 궤적 초기에 구조적 문장 종료 토큰을 조기에 고정하여 이 전략을 방해하며, 결과적으로 출력 길이를 고정하여 정보 누락 또는 환각(hallucination)을 유발할 수 있습니다. 이를 해결하기 위해, 훈련이 없는 추론 시 구조적 토큰 신뢰도를 낮추는 람다 스케일 구조적 디코딩(lambda-scaled structural decoding)을 제안하며, 이를 통해 BLEU-4 점수가 +9.4 향상되었습니다. 마지막으로, 그래프 트랜스포머 인코더(Graph Transformer encoder)를 LLaDA의 디코딩 과정에 통합하여 관계 그래프 구조를 명시적으로 반영하는 Graph-LLaDA를 소개합니다. LAGRANGE 데이터셋에 대한 교차 데이터셋 평가에서, 이전 기준 모델(baselines)이 데이터셋 특화 패턴에 과적합(overfit)되는 반면, LLM 및 MDLM 기반 접근 방식이 유의미하게 더 잘 일반화(generalize)됨을 확인했습니다.

## 원문 영어

<details>
<summary>원문 보기</summary>

We present the first systematic study of masked diffusion language models (MDLMs) for graph-to-text generation. We analyze MDLM generation trajectories -- the order in which tokens are unmasked during iterative decoding -- and find that, unlike autoregressive LLMs which generate text linearly, MDLMs naturally prioritize entities first, followed by relational and function words, with structural tokens resolved last. We further identify a previously undocumented failure mode of supervised fine-tun

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2605.31564v1)
