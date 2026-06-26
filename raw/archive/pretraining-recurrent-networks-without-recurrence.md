---
title: Recurrent 네트워크를 Recurrence 없이 사전학습하기
created: 2026-06-08
updated: 2026-06-08
type: concept
tags: [research, ai-ml, programming]
sources: [raw/papers/pretraining-recurrent-networks-without-recurrence-2026-06-08.md]
confidence: medium
links: [code2lora-hypernetwork-generated-adapters-for-code-language, pc-layer-polynomial-weight-preconditioning-for-improving-ll, neuron-populations-exhibit-divergent-selectivity-with-scale, quantum-element-wise-transforms]
---

# Recurrent 네트워크를 Recurrence 없이 사전학습하기

> 관련: [[code2lora-hypernetwork-generated-adapters-for-code-language|Code2LoRA]], [[pc-layer-polynomial-weight-preconditioning-for-improving-ll|PC Layer]], [[neuron-populations-exhibit-divergent-selectivity-with-scale|뉴런 집단 선택성]]도 참고하세요.

> 📄 원문: [Pretraining Recurrent Networks without Recurrence](https://arxiv.org/abs/2606.06479v1)
> ✍️ 저자: Akarsh Kumar, Phillip Isola
> 📅 발행: 2026-06-04
> 🏷️ 카테고리: cs.LG, cs.AI

## 요약

순환 신경망(RNNs)을 훈련하려면 긴 계산 시퀀스에 걸쳐 크레딧을 할당해야 합니다. 표준 시간을 통한 역전파(BPTT)는 이 문제를 제대로 해결하지 못합니다. 이 방법은 시간적으로 순차적이어서 병렬 처리를 제한하고, 기울기 소실(vanishing gradients) 또는 기울기 폭발(exploding gradients) 문제를 겪어 장거리 연관성을 학습하기 어렵게 만듭니다. 우리는 비선형 RNN을 훈련하기 위한 지도 메모리 훈련(Supervised Memory Training, SMT) 방법을 제안합니다. 이 방법은 RNN 훈련을 원스텝 메모리 전이 레이블 $(m_t, x_{t+1}) \rightarrow m_{t+1}$에 대한 지도 학습으로 축소하여 순환적 크레딧 전파를 완전히 우회합니다. SMT는 미래를 예측하는 데 필요한 과거 정보만 유지하는 예측 상태 목표(predictive state objective)를 기반으로 트랜스포머 기반 인코더를 훈련하여 이러한 메모리 레이블을 획득합니다. 무엇을 기억할지와 메모리를 어떻게 업데이트할지를 분리함으로써, SMT는 RNN을 펼치지 않고도 임의의 두 토큰 사이에 안정적인 $O(1)$ 길이의 기울기 경로를 갖는 시간 병렬 RNN 훈련을 가능하게 합니다. 우리는 언어 모델링 및 픽셀 시퀀스 모델링과 같은 작업에서 다양한 RNN 아키텍처를 사전 훈련할 때 SMT가 BPTT보다 우수한 성능을 보임을 확인했습니다. SMT는 비선형 RNN이 장거리 의존성을 더 잘 포착하고 병렬로 훈련할 수 있게 하여, 과거 경험의 시간적 추상화를 구축하는 모델의 스케일링을 잠재적으로 가능하게 합니다.

## 원문 영어

<details>
<summary>원문 보기</summary>

Training recurrent neural networks (RNNs) requires assigning credit across long sequences of computations. Standard backpropagation through time (BPTT) addresses this problem poorly: it is sequential in time, limiting parallelism, and suffers from vanishing or exploding gradients, making long-range associations difficult to learn. We propose Supervised Memory Training (SMT), a method for training nonlinear RNNs that sidesteps recurrent credit propagation entirely by reducing RNN training to supe

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2606.06479v1)
