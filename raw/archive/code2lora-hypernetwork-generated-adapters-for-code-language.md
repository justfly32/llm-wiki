---
title: Code2LoRA: 소프트웨어 진화에 따른 코드 언어 모델을 위한 하이퍼네트워크 기반 어댑터 생성
created: 2026-06-07
updated: 2026-06-07
type: concept
tags: [research, ai-ml, programming, optimization]
sources: [raw/papers/code2lora-hypernetwork-generated-adapters-for-code-language-2026-06-07.md]
confidence: medium
links: [cofida-m-concept-aware-feature-modulation-for-cross-domain, pc-layer-polynomial-weight-preconditioning-for-improving-ll, pretraining-recurrent-networks-without-recurrence, protoada-prototype-guided-adaptive-adapter-expansion-and-ge]
---

# Code2LoRA: 소프트웨어 진화에 따른 코드 언어 모델을 위한 하이퍼네트워크 기반 어댑터 생성

> 관련: [[cofida-m-concept-aware-feature-modulation-for-cross-domain|CoFiDA-M]], [[pc-layer-polynomial-weight-preconditioning-for-improving-ll|PC Layer]], [[pretraining-recurrent-networks-without-recurrence|Recurrent 네트워크 사전학습]]도 참고하세요.

> 📄 원문: [Code2LoRA: Hypernetwork-Generated Adapters for Code Language Models under Software Evolution](https://arxiv.org/abs/2606.06492v1)
> ✍️ 저자: Liliana Hotsko, Yinxi Li, Yuntian Deng
> 📅 발행: 2026-06-04
> 🏷️ 카테고리: cs.SE, cs.AI, cs.CL

## 요약

코드 언어 모델은 임포트(import), API, 프로젝트 컨벤션을 해결하기 위해 리포지토리 수준의 컨텍스트가 필요합니다. 기존 방법들은 이 지식을 긴 입력(RAG 또는 의존성 분석을 통해 검색된)으로 주입하거나, 리포지토리별 미세 조정(fine-tuning) 및 LoRA를 통해 주입합니다. 그러나 이러한 방법은 리포지토리 규모에서 비용이 많이 들고, 변화하는 코드베이스에 취약합니다. 우리는 리포지토리별 LoRA 어댑터를 생성하는 하이퍼네트워크(hypernetwork) 프레임워크인 Code2LoRA를 소개합니다. 이 프레임워크는 추론 시 토큰 오버헤드 없이 리포지토리 지식을 효과적으로 주입합니다. Code2LoRA는 두 가지 사용 시나리오를 지원합니다: Code2LoRA-Static은 단일 리포지토리 스냅샷을 어댑터로 변환하여 안정적인 코드베이스의 이해에 적합하며, Code2LoRA-Evo는 코드 차이(diff)마다 업데이트되는 GRU 은닉 상태(hidden state)에 의해 지원되는 어댑터를 유지하여 변화하는 코드베이스의 능동적 개발에 적합합니다. Code2LoRA를 파라미터 효율적 미세 조정(parameter-efficient fine-tuning) 기준선과 비교 평가하기 위해, 우리는 604개의 Python 리포지토리로 구성된 RepoPeftBench라는 벤치마크를 구축했습니다. 이 벤치마크는 두 가지 트랙을 포함합니다: 정적 트랙은 40K개의 훈련 및 12K개의 테스트 어서션 완성(assertion-completion) 작업을 포함하고, 진화 트랙은 215K개의 커밋 기반 훈련 및 87K개의 커밋 기반 테스트 작업을 포함합니다. 정적 트랙에서 Code2LoRA-Static은 63.8%의 크로스 리포지토리(cross-repo) 및 66.2%의 인 리포지토리(in-repo) 정확 일치(exact match)를 달성하여 리포지토리별 LoRA 상한선과 동등한 성능을 보였습니다. 진화 트랙에서 Code2LoRA-Evo는 60.3%의 크로스 리포지토리 정확 일치를 달성하여 단일 공유 LoRA 대비 5.2 퍼센트 포인트(pp) 향상을 보였습니다. Code2LoRA의 코드는 https://anonymous.4open.science/r/code2lora-6857에서 확인할 수 있으며, 모델 체크포인트와 RepoPeftBenc

(이하 생략...)

## 원문 영어

<details>
<summary>원문 보기</summary>

Code language models need repository-level context to resolve imports, APIs, and project conventions. Existing methods inject this knowledge as long inputs (retrieved through RAG or dependency analysis) or through per-repository fine-tuning and LoRA -- costly at repository scale and brittle to evolving codebases. We introduce Code2LoRA, a hypernetwork framework that generates repository-specific LoRA adapters, effectively injecting repository knowledge with zero inference-time token overhead. Co

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2606.06492v1)
