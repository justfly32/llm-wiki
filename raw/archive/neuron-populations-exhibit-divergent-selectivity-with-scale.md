---
title: 뉴런 집단은 규모에 따라 서로 다른 선택성(selectivity)을 나타낸다.
created: 2026-06-04
updated: 2026-06-04
type: concept
tags: [research, ai-ml, multimodal]
sources: [raw/papers/neuron-populations-exhibit-divergent-selectivity-with-scale-2026-06-04.md]
confidence: medium
---

# 뉴런 집단은 규모에 따라 서로 다른 선택성(selectivity)을 나타낸다.

> 📄 원문: [Neuron Populations Exhibit Divergent Selectivity with Scale](https://arxiv.org/abs/2606.03990v1)
> ✍️ 저자: Amil Dravid, Yasaman Bahri, Alexei A. Efros
> 📅 발행: 2026-06-02
> 🏷️ 카테고리: cs.LG, cs.CL, cs.CV

## 요약

신경망 내의 뉴런 집단이 스케일에 따라 예측 가능하게 진화하는지 조사하여, 손실(loss)과 같은 거시적 관측치를 넘어 스케일링 법칙을 확장합니다. 이 질문을 탐구하기 위해, 독립적으로 훈련된 모델에서도 유사한 활성화 패턴을 보이는 이전에 특성화된 뉴런 클래스인 Rosetta Neurons를 연구합니다. 최대 30B 파라미터의 언어 모델과 최대 5B 파라미터의 비전 모델을 각각 분석한 결과, Rosetta Neurons의 집단은 모델 크기에 대해 아선형 멱법칙(sublinear power law)을 따르며, 절대 수는 증가하지만 전체 뉴런 수에서 차지하는 비율은 감소하는 것을 관찰했습니다. 또한 Neuron Polarization Effect를 발견했습니다: Rosetta Neurons는 스케일이 커질수록 더 선택적이고 점점 단의적(monosemantic)이 되어, 덜 선택적인 비-Rosetta 집단과 분리됩니다. 특성 유용성(feature utility)과 제한된 뉴런 용량(neuron capacity)의 균형을 맞추는 분석 모델이 아선형 멱법칙 스케일링과 이 분극 효과를 설명합니다. 마지막으로, Rosetta Neurons가 스케일에 따라 더 도메인 특화(domain-specialized)되며, 계속 사전 훈련(continued pretraining)을 위한 표적 데이터 필터링 사례 연구를 통해 그 선택성을 보여줍니다. 우리의 결과는 해석 가능하고 공유된 뉴런 수준 구조에 대한 스케일링 법칙을 제시하며, 모델 크기를 뉴런의 보편성, 선택성, 특화의 체계적 변화와 연결합니다.

## 원문 영어

<details>
<summary>원문 보기</summary>

We investigate whether neuron populations within neural networks evolve predictably with scale, extending scaling laws beyond macroscopic observables such as loss. To probe this question, we study Rosetta Neurons, a previously characterized class of neurons whose activation patterns are similar across independently trained models (Dravid et al., 2023). In separate analyses of language models up to 30B parameters and vision models up to 5B parameters, we observe that the population of Rosetta Neu

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2606.03990v1)
