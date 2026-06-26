---
title: 다중 세분성 AI 텍스트 검출을 위한 작업 기반 점진적 인간-AI 텍스트 변환 벤치마크
created: 2026-06-08
updated: 2026-06-08
type: concept
tags: [research, programming, multimodal]
sources: [raw/papers/operation-guided-progressive-human-to-ai-text-transformation-2026-06-08.md]
confidence: medium
---

# 다중 세분성 AI 텍스트 검출을 위한 작업 기반 점진적 인간-AI 텍스트 변환 벤치마크

> 📄 원문: [Operation-Guided Progressive Human-to-AI Text Transformation Benchmark for Multi-Granularity AI-Text Detection](https://arxiv.org/abs/2606.06481v1)
> ✍️ 저자: Sondos Mahmoud Bsharat, Jiacheng Liu, Xiaohan Zhao
> 📅 발행: 2026-06-04
> 🏷️ 카테고리: cs.CL, cs.AI, cs.LG

## 요약

AI 글쓰기 보조 도구가 실제 초안 작성 및 수정 워크플로에 점점 더 깊이 통합되면서, 많은 문서는 더 이상 순수하게 인간이 작성한 것이거나 AI가 생성한 것이 아니라 인간과 AI가 점진적으로 공동 편집한 결과물이 되고 있습니다. 그러나 기존의 AI 텍스트 탐지 벤치마크는 대부분 최종 결과물에 초점을 맞추고 있으며, 수정 과정 전반에 걸쳐 AI 저작 신호가 어떻게 발생, 축소, 또는 소멸하는지에 대한 이해를 제한적으로 제공합니다. 우리는 문장, 토큰, 스팬(span) 등 다양한 세분성(granularity)에서 점진적인 인간-텍스트에서 AI-텍스트로의 변환을 연구하기 위한 작업 기반(operation-guided) 벤치마크인 OpAI-Bench를 소개합니다. 인간이 작성한 문서에서 출발하여, OpAI-Bench는 사전 정의된 AI 커버리지 수준과 5가지 대표적인 AI 편집 작업을 기반으로 각 샘플에 대해 순차적으로 수정된 9가지 버전을 구성하며, 네 가지 도메인을 포괄하면서 다양한 세분성에서 완전한 저작 출처(authorship provenance)를 보존합니다. 이 벤치마크는 8개의 문서 수준 탐지기, 7개의 문장 수준 탐지기, 그리고 2개의 세밀한 토큰/스팬 수준 탐지기를 사용한 포괄적인 평가를 지원합니다. 실험 결과, AI 텍스트 탐지 가능성은 AI 편집 콘텐츠의 비율뿐만 아니라 편집 작업, 도메인, 누적 수정 이력에 의해서도 좌우됨을 밝혀냈습니다. 흥미롭게도, 혼합 저작권을 가진 중간 버전은 종종 완전히 인간이 작성한 문서나 대량으로 AI가 편집된 최종 결과물보다 탐지하기 더 어려운 경우가 많았으며, 이는 기존 벤치마크가 놓치고 있던 비단조적(non-monotonic) 탐드 패턴을 드러냅니다. OpAI-Bench는 분석을 위한 통제된 테스트베드를 제공합니다.

(이하 생략...)

## 원문 영어

<details>
<summary>원문 보기</summary>

As AI writing assistants become increasingly integrated into real-world drafting and revision workflows, many documents are no longer purely human-written or AI-generated, but instead result from progressive human-AI co-editing. However, existing AI-text detection benchmarks largely focus on final outputs and provide limited understanding of how AI authorship signals emerge, accumulate, or disappear throughout the revision process. We introduce OpAI-Bench, an operation-guided benchmark for study

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2606.06481v1)
