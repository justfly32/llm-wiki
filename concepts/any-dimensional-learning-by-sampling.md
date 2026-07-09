---
title: Any-Dimensional Learning by Sampling
created: 2026-07-10
updated: 2026-07-10
type: concept
tags: [research, ai-ml]
sources: [raw/papers/any-dimensional-learning-by-sampling-2026-07-10.md]
confidence: medium
---

# Any-Dimensional Learning by Sampling

> 📄 원문: [Any-Dimensional Learning by Sampling](https://arxiv.org/abs/2607.07680v1)
> ✍️ 저자: Eitan Levin, Venkat Chandrasekaran
> 📅 발행: 2026-07-08
> 🏷️ 카테고리: math.ST, cs.LG, math.PR

## 요약

Many machine learning models are defined for inputs of different sizes, such as point clouds containing different numbers of points, sequences of tokens of different lengths, and graphs on different numbers of nodes. Such models are trained on finitely-many examples of necessarily limited sizes. How well do these models generalize from inputs of small size to larger inputs of size not seen during training? Furthermore, evaluating such models on large inputs is often expensive. How can we sketch large inputs to obtain smaller ones on which the model takes similar values? At the heart of both questions is the need to compare inputs of different sizes and to approximate large inputs by small ones. We present a unified approach to address these questions by using random sampling maps to compare inputs of different sizes. The sampling maps we consider are generalizations of sampling with replacement, random binning, and species sampling. We characterize the application domains in which each type of sampling is appropriate in terms of the symmetries and relations between problem instances of different sizes in the domain. Our framework yields explicit generalization and sketching rates for function classes continuous with respect to a chosen notion of sampling, encompassing large families of functions defined on sequences, graphs, and tensors of different sizes. Specific examples include moment polynomials on measures, homomorphism densities and numbers of graphs, permutation-invariant transformers, and graph neural networks.

## 원문 영어

<details>
<summary>원문 보기</summary>

Many machine learning models are defined for inputs of different sizes, such as point clouds containing different numbers of points, sequences of tokens of different lengths, and graphs on different numbers of nodes. Such models are trained on finitely-many examples of necessarily limited sizes. How well do these models generalize from inputs of small size to larger inputs of size not seen during training? Furthermore, evaluating such models on large inputs is often expensive. How can we sketch 

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2607.07680v1)
