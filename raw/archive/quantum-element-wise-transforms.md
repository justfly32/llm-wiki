---
title: 양자 요소별 변환 (Quantum element-wise transforms)
created: 2026-06-08
updated: 2026-06-08
type: concept
tags: [research, ai-ml]
sources: [raw/papers/quantum-element-wise-transforms-2026-06-08.md]
confidence: medium
---

# 양자 요소별 변환 (Quantum element-wise transforms)

> 📄 원문: [Quantum element-wise transforms](https://arxiv.org/abs/2606.06456v1)
> ✍️ 저자: Zane M. Rossi, Rahul Sarkar
> 📅 발행: 2026-06-04
> 🏷️ 카테고리: quant-ph

## 요약

기본적인 수치 선형 대수 작양에 대한 양자 알고리즘은 다양한 문제를 통합된 양자 계산 맥락으로 변환하는 데 필수적임이 입증되었다. 이러한 작업 중 다수—예를 들어, 유니터리 과정(unitary process)에 내장된 행렬의 스펙트럼(spectrum)에 다항 함수를 적용하는 것(이른바 블록 인코딩(block encoding))이나 블록 인코딩들의 선형 결합을 취하는 것—은 양자 특이값 변환(QSVT, quantum singular value transformation)이나 유니터리의 선형 결합(LCU, linear combination of unitaries)과 같은 기법에 의해 잘 다루어지고 있다. 그러나 기존 양자 알고리즘으로는 구현이 불명확하거나 비효율적인 유용한 행렬 변환들도 존재한다. 본 연구에서는 이러한 변환들 중 일부에 대해 개선된 양자 알고리즘을 구성하며, 그중 가장 간단한 것은 원소별(element-wise)로 적용되는 다항 함수이다. 우리는 양자 원소별 변환을 계산하는 데 필요한 공간이 기존 연구에 비해 적용 함수의 차수에 대해 지수적으로 줄일 수 있음을 보이고, 이전 구성에서의 오류를 지적하고 수정한다. 또한 우리의 알고리즘을 머신러닝(machine learning), 시뮬레이션(simulation), 신호 처리(signal processing) 등의 응용 분야와 함께 제시한다.

## 원문 영어

<details>
<summary>원문 보기</summary>

Quantum algorithms for basic numerical linear algebraic tasks have proven essential for translating diverse problems to a unified quantum computational context. Many of these tasks -- e.g., applying a polynomial function to the spectrum of a matrix embedded in a unitary process (a so-called block encoding), or taking linear combinations of block encodings -- are well-addressed by techniques like quantum singular value transformation (QSVT) or linear combination of unitaries (LCU). However, there

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2606.06456v1)
