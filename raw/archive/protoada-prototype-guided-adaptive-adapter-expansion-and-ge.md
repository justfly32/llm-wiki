---
title: ProtoAda: 다중모달 연속 지시 튜닝을 위한 프로토타입 기반 적응형 어댑터 확장 및 기하학적 통합
created: 2026-06-03
updated: 2026-06-03
type: concept
tags: [research, ai-ml, multimodal]
sources: [raw/papers/protoada-prototype-guided-adaptive-adapter-expansion-and-ge-2026-06-03.md]
confidence: medium
---

# ProtoAda: 다중모달 연속 지시 튜닝을 위한 프로토타입 기반 적응형 어댑터 확장 및 기하학적 통합

> 📄 원문: [ProtoAda: Prototype-Guided Adaptive Adapter Expansion and Geometric Consolidation for Multimodal Continual Instruction Tuning](https://arxiv.org/abs/2606.02576v1)
> ✍️ 저자: Yu-Cheng Shi, Zhen-Hao Xie, Jun-Tao Tang
> 📅 발행: 2026-06-01
> 🏷️ 카테고리: cs.CV, cs.LG

## 요약

다중 모달 대규모 언어 모델(Multimodal Large Language Models, MLLMs)은 명령어 튜닝(instruction tuning)을 통해 강력한 성능을 달성하지만, 실제 배포 환경에서는 새로운 비전-언어 능력을 지속적으로 습득해야 하므로 다중 모달 지속적 명령어 튜닝(Multimodal Continual Instruction Tuning, MCIT)이 필수적이다. 작업 간 간섭을 줄이고 협업을 촉진하기 위해 최근 방법들은 이미지-텍스트 유사도 라우팅을 사용하는 LoRA 전문가 혼합(Mixture of LoRA Experts)과 같은 희소 아키텍처를 자주 활용한다. 그러나 응답 구조가 서로 다른 작업들이 매우 유사한 시각-언어적 의미를 공유할 수 있어 동일한 전문가로 잘못 라우팅될 수 있으며, 이미지-텍스트 유사도만으로는 신뢰할 수 있는 작업 할당이 불충분하다. 예를 들어, 좌표 예측이 필요한 그라운딩(grounding) 작업의 전문가가 의미적으로 유사한 VQA 작업을 학습한 후 짧은 텍스트 답변을 생성하는 방향으로 편향될 수 있다. 이러한 형식 무시 작업 할당(format-blind task assignment)은 이질적인 응답 유형을 공유 파라미터에 통합하여 그래디언트 간섭을 유발하고 전문가 간 비효율적인 협업을 초래한다. 이 문제를 해결하기 위해 우리는 프로토타입 기반 적응형 튜닝 프레임워크인 ProtoAda를 제안한다. ProtoAda는 형식 인식 작업 프로토타입(format-aware task prototypes)을 도입하여 작업 할당과 라우팅을 작업 의미론과 출력 구조 모두에 맞추고, 기하학 인식 방식(geometry-aware manner)으로 형식 호환 업데이트를 통합하여 기존 파라미터를 효과적으로 재사용하고 점진적으로 개선한다. 여러 벤치마크에 대한 광범위한 실험 결과, ProtoAda가 우수한 성능을 달성함을 입증한다.

(이하 생략...)

## 원문 영어

<details>
<summary>원문 보기</summary>

Multimodal Large Language Models (MLLMs) achieve strong performance through instruction tuning, but real-world deployment requires them to continually acquire new vision-language capabilities, making Multimodal Continual Instruction Tuning (MCIT) essential. To reduce inter-task interference and promote collaboration, recent methods often employ sparse architectures like Mixture of LoRA Experts with image-text similarity routing. However, tasks with distinct response structures could share highly

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2606.02576v1)
