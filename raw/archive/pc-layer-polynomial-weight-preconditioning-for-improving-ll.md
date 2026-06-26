---
title: PC Layer: LLM 사전 학습 개선을 위한 다항식 가중치 전처리(Polynomial Weight Preconditioning)
created: 2026-06-08
updated: 2026-06-08
type: concept
tags: [research, ai-ml, programming, optimization]
sources: [raw/papers/pc-layer-polynomial-weight-preconditioning-for-improving-ll-2026-06-08.md]
confidence: medium
links: [code2lora-hypernetwork-generated-adapters-for-code-language, pretraining-recurrent-networks-without-recurrence, protoada-prototype-guided-adaptive-adapter-expansion-and-ge, neuron-populations-exhibit-divergent-selectivity-with-scale]
---

# PC Layer: LLM 사전 학습 개선을 위한 다항식 가중치 전처리(Polynomial Weight Preconditioning)

> 관련: [[code2lora-hypernetwork-generated-adapters-for-code-language|Code2LoRA]], [[pretraining-recurrent-networks-without-recurrence|Recurrent 네트워크 사전학습]], [[neuron-populations-exhibit-divergent-selectivity-with-scale|뉴런 집단 선택성]]도 참고하세요.

> 📄 원문: [PC Layer: Polynomial Weight Preconditioning for Improving LLM Pre-Training](https://arxiv.org/abs/2606.06470v1)
> ✍️ 저자: Senmiao Wang, Tiantian Fang, Haoran Zhang
> 📅 발행: 2026-06-04
> 🏷️ 카테고리: cs.LG, cs.AI

## 요약

우리는 LLM 학습 전반에 걸쳐 안정적인 가중치 조건을 보장하는 다항식 전처리기(polynomial preconditioner)를 통한 가중치 매개변수화인 전처리(PC) 레이어를 제안합니다. PC 모듈은 저차 다항식 전처리를 통해 가중치 행렬의 특이값 스펙트럼을 재구성합니다. 학습 후, 전처리된 가중치는 원래 아키텍처에 다시 병합될 수 있으며, 추론 시 오버헤드가 발생하지 않습니다. 우리는 AdamW 및 Muon 옵티마이저 모두에 대해 Llama-1B 사전 학습에서 제안된 PC 레이어가 표준 트랜스포머보다 우수한 성능을 보임을 입증합니다. 이론적으로, 각 레이어의 특이값을 균일하게 제한하는 것이 특정 딥 선형 네트워크에서 경사 하강법이 전역 최소값으로 기하학적으로 수렴함을 보장함을 증명하여 이 스펙트럼 제어 원리를 정당화합니다. 코드는 https://github.com/Empath-aln/PC-layer에서 확인할 수 있습니다.

## 원문 영어

<details>
<summary>원문 보기</summary>

We propose a preconditioning (PC) layer, a weight parameterization via polynomial preconditioner that ensures stable weight conditioning throughout LLM training. The PC module reshapes the singular-value spectrum of weight matrices via low-degree polynomial preconditioning. After training, the preconditioned weights can be merged back into the original architecture, incurring no inference overhead. We demonstrate the advantage of the proposed PC layer over standard transformers in Llama-1B pre-t

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2606.06470v1)
