---
title: 기능적 어텐션: 쌍별 친화도에서 기능적 대응으로
created: 2026-06-02
updated: 2026-06-02
type: concept
tags: [research, ai-ml]
sources: [raw/papers/functional-attention-from-pairwise-affinities-to-functional-2026-06-02.md]
confidence: medium
links: [cofida-m-concept-aware-feature-modulation-for-cross-domain, imaginative-perception-tokens-enhance-spatial-reasoning-in-m, soco-benchmarking-semantic-object-correspondence-in-vision, newtphys-do-foundation-models-understand-newtonian-physics]
---

# 기능적 어텐션: 쌍별 친화도에서 기능적 대응으로

> 관련: [[cofida-m-concept-aware-feature-modulation-for-cross-domain|CoFiDA-M]], [[imaginative-perception-tokens-enhance-spatial-reasoning-in-m|상상력 기반 인지 토큰]], [[soco-benchmarking-semantic-object-correspondence-in-vision|SOCO 벤치마크]]도 참고하세요.

> 📄 원문: [Functional Attention: From Pairwise Affinities to Functional Correspondences](https://arxiv.org/abs/2605.31559v1)
> ✍️ 저자: Jiefang Xiao, Maolin Gao, Simon Weber
> 📅 발행: 2026-05-29
> 🏷️ 카테고리: cs.LG

## 요약

무한 차원 함수 공간(function spaces) 사이의 매핑을 학습하는 것, 즉 연산자 학습(operator learning)은 다양한 머신러닝 응용 분야에서 필수적이다. 트랜스포머 기반 연산자들이 널리 사용되지만, 이들은 종종 토큰 단위 어텐션(token-wise attention)에 의존한다. 이러한 방법들은 연속장(continuous fields)을 이산 토큰으로 취급하며, 보통 전역적인 함수 구조를 무시한다. 우리는 어텐션을 적응형 기저(adaptive bases) 간의 함수적 대응 관계(functional correspondence)로 재해석하는 \emph{Functional Attention}을 제안한다. 기하학적 함수 맵(geometric functional maps)에서 영감을 받아, 우리의 방법은 소프트맥스 친화도(softmax affinities)를 구조화된 선형 연산자(structured linear operators)로 대체한다. 이를 통해 전역 의존성을 명시적으로 포착하는 간결하고, 일반화 가능하며, 해상도 불변(resolution-invariant)인 표현을 얻는다. 실험 결과, \emph{Functional Attention}은 편미분방정식(PDE) 풀이, 3D 분할(segmentation), 회귀(regression)를 포함한 다양한 연산자 학습 과제에서 최고 수준의 성능을 달성할 수 있음을 보여주며, 동시에 변화하는 이산화(discretizations)에 대해 강건성(robust)을 유지한다. 프로젝트 페이지는 https://github.com/xjffff/FUNCATTN 에서 확인할 수 있다.

## 원문 영어

<details>
<summary>원문 보기</summary>

Learning mappings between infinite-dimensional function spaces, or operator learning, is essential for many machine learning applications. Although transformer-based operators are popular, they often rely on token-wise attention. These methods treat continuous fields as discrete tokens and usually ignore the global functional structure. We introduce \emph{Functional Attention}, which reinterprets attention as a functional correspondence between adaptive bases. Inspired by geometric functional ma

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2605.31559v1)
