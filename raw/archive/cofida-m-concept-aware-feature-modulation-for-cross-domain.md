---
title: CoFiDA-M: 이미지 전용 추론을 통한 도메인 간 적응을 위한 개념 인지 기능 변조
created: 2026-06-02
updated: 2026-06-02
type: concept
tags: [research, programming, optimization, multimodal, agent]
sources: [raw/papers/cofida-m-concept-aware-feature-modulation-for-cross-domain-2026-06-02.md]
confidence: medium
links: [code2lora-hypernetwork-generated-adapters-for-code-language, functional-attention-from-pairwise-affinities-to-functional, protoada-prototype-guided-adaptive-adapter-expansion-and-ge, pc-layer-polynomial-weight-preconditioning-for-improving-ll]
---

# CoFiDA-M: 이미지 전용 추론을 통한 도메인 간 적응을 위한 개념 인지 기능 변조

> 관련: [[code2lora-hypernetwork-generated-adapters-for-code-language|Code2LoRA]], [[functional-attention-from-pairwise-affinities-to-functional|기능적 어텐션]], [[protoada-prototype-guided-adaptive-adapter-expansion-and-ge|ProtoAda]]도 참고하세요.

> 📄 원문: [CoFiDA-M: Concept-Aware Feature Modulation for Cross-Domain Adaptation with Image-Only Inference](https://arxiv.org/abs/2605.31591v1)
> ✍️ 저자: Nurjahan Sultana, Moi Hoon Yap, Xinqi Fan
> 📅 발행: 2026-05-29
> 🏷️ 카테고리: cs.CV

## 요약

AI 기반 피부암 선별 검사 모델은 전문가용 피부경(dermoscopic) 이미지(소스)에서 일반 소비자용 임상(clinical) 이미지(타겟)로 전환할 때 심각한 성능 저하를 겪으며, 이는 실제 환경에서의 적용을 저해한다. 기존의 도메인 적응(domain adaptation) 방법들은 임상적 개념과 같은 중요한 의미론적 불변량(semantic invariants)을 간과하는 경우가 많다. MONET과 같은 새로운 파운데이션 모델(foundation model)이 이러한 의미론적 정보를 밀도 있는 확률 점수(dense, probabilistic scores)로 제공할 수 있지만, 이 메타데이터는 테스트 시점에는 사용할 수 없어 실용적인 이미지 전용 선별 도구에 배포 역설(deployment paradox)을 야기한다. 우리는 이러한 격차를 해소하기 위해 CoFiDA-M이라는 특권 정보(privileged information) 프레임워크를 제안한다. 이 프레임워크는 훈련 시점에는 개념(concepts)으로부터 학습하지만, 배포 시에는 이미지 전용 모델로 작동한다. 우리의 방법은 MONET의 개념 확률을 활용하여 FiLM 변조기(modulator)를 안내하는 교사 네트워크(teacher network)를 훈련시켜 시각적 특징을 의미론적으로 "편집된" 특징 공간으로 변환한다. 이후 경량의 이미지 전용 학생 네트워크(student network)는 교사의 최종 예측뿐만 아니라 이 편집된 표현을 재현하도록 훈련된다. 이러한 지식 증류(distillation)는 임상적 추론을 학생 네트워크의 가중치에 "구워 넣는다(bakes)". 도전적인 다중 데이터셋 벤치마크에서 우리의 이미지 전용 학생 네트워크는 최첨단 접근법들을 상회하며, 특히 흑색종 재현율(melanoma recall)에서 뛰어난 성능을 보인다. 우리의 연구는 노이즈가 있는 확률적 메타데이터를 특권 정보로 활용하기 위한 실용적이고 일반화 가능한 프레임워크를 제공하며, 피부과 분야를 넘어 실제 환경에서의 강력한 교차 데이터셋 강건성(cross-dataset robustness)과 배포 가능성을 입증한다. 구현 코드는 다음에서 확인할 수 있다:

(이하 생략...)

## 원문 영어

<details>
<summary>원문 보기</summary>

Models for AI-based skin cancer screening suffer a severe performance drop when shifting from expert dermoscopic (source) images to consumer-grade clinical (target) images, hindering real-world deployment. Existing domain adaptation methods often ignore crucial semantic invariants, such as clinical concepts. While new foundation models like MONET can provide this semantic information as dense, probabilistic scores, this metadata is unavailable at test time, creating a deployment paradox for prac

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2605.31591v1)
