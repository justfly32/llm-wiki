---
title: 다중 모달 LLM-as-a-Judge에서 지각적 판단 편향(Perceptual Judgment Bias)을 완화하기 위한 지각적 교란(Perceptual Perturbation)과 보상 모델링(Reward Modeling) 기법
created: 2026-06-03
updated: 2026-06-03
type: concept
tags: [research, ai-ml, alignment, multimodal, agent]
sources: [raw/papers/mitigating-perceptual-judgment-bias-in-multimodal-llm-as-a-j-2026-06-03.md]
confidence: medium
---

# 다중 모달 LLM-as-a-Judge에서 지각적 판단 편향(Perceptual Judgment Bias)을 완화하기 위한 지각적 교란(Perceptual Perturbation)과 보상 모델링(Reward Modeling) 기법

> 📄 원문: [Mitigating Perceptual Judgment Bias in Multimodal LLM-as-a-Judge via Perceptual Perturbation and Reward Modeling](https://arxiv.org/abs/2606.02578v1)
> ✍️ 저자: Seojeong Park, Jiho Choi, Junyong Kang
> 📅 발행: 2026-06-01
> 🏷️ 카테고리: cs.CV, cs.AI

## 요약

최근 다중 모달 대규모 언어 모델은 강력한 추론 능력을 보여주고 있지만, 자동화된 평가자로서의 신뢰성은 여전히 중요한 한계에 의해 제약된다. 시각적 증거가 텍스트 단서와 충돌할 때, MLLM 심사자는 지각적으로 정확한 답변보다 그럴듯한 서사를 선호하는 경향이 있다. 우리는 이 현상을 '지각적 판단 편향(Perceptual Judgment Bias)'으로 명명하고 체계적으로 분석한다. 통제된 시각적 교란을 통해 기존 다중 모달 심사자들은 자신의 시각적 인식 대신 응답 텍스트에 고착되는 경우가 빈번하며, 이는 일관성 없고 검증 불가능한 평가로 이어진다. 이 문제를 해결하기 위해 우리는 지각적 오류를 분리하고 검증 가능한 감독을 가능하게 하는 최소한의 편집된 반사실적 응답을 구성하는 '지각적 교란 판단 데이터셋(Perceptually Perturbed Judgment Dataset)'을 도입한다. 이 데이터셋을 기반으로, 구조화된 GRPO 기반 보상과 배치 순위 목표를 결합한 통합 훈련 프레임워크를 개발하여 명시적인 쌍별 레이블 없이 일관된 전역 순서를 달성한다. 다양한 MLLM-as-a-Judge 벤치마크에 걸친 실험 결과, 우리의 접근법이 지각적 충실도, 순위 일관성, 그리고 인간 평가와의 정렬을 상당히 향상시킨 것으로 나타났다. 본 연구 결과는 지각적으로 근거 있고, 해석 가능하며, 시각적 추론 충돌에 강건한 다중 모달 심사자를 훈련하기 위한 확장 가능하고 일반화 가능한 경로를 확립한다.

## 원문 영어

<details>
<summary>원문 보기</summary>

Recent multimodal large language models have demonstrated strong reasoning ability, yet their reliability as automated evaluators remains limited by a critical weakness: when visual evidence conflicts with textual cues, MLLM judges tend to reward plausible narratives over perceptually correct answers. We identify and systematically analyze this phenomenon, which we term Perceptual Judgment Bias. Through controlled visual perturbations, existing multimodal judges frequently anchor on the response

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2606.02578v1)
