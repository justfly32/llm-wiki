---
title: TunerDiT: 다중 이벤트 비디오 생성을 위한 확산 트랜스포머(Diffusion Transformer)의 훈련 없는 점진적 스티어링
created: 2026-06-02
updated: 2026-06-02
type: concept
tags: [research, alignment, multimodal, diffusion]
sources: [raw/papers/tunerdit-training-free-progressive-steering-of-diffusion-tr-2026-06-02.md]
confidence: medium
---

# TunerDiT: 다중 이벤트 비디오 생성을 위한 확산 트랜스포머(Diffusion Transformer)의 훈련 없는 점진적 스티어링

> 📄 원문: [TunerDiT: Training-free Progressive Steering of Diffusion Transformer for Multi-Event Video Generation](https://arxiv.org/abs/2605.31590v1)
> ✍️ 저자: Ruotong Liao, Guowen Huang, Qing Cheng
> 📅 발행: 2026-05-29
> 🏷️ 카테고리: cs.CV, cs.AI

## 요약

텍스트-비디오(T2V) 생성은 여러 이벤트가 포함된 긴 시간 범위(long horizons)의 비디오를 생성할 때 까다로운 문제에 직면하게 된다. 디퓨전 과정(diffusion process)의 본질에서 영감을 받아, 우리는 비디오 디퓨전 트랜스포머(DiTs)를 탐구하고, 조건화 텍스트(conditioning text)가 전역적 레이아웃(global layout)에서 미세한 디테일(fine-grained details)로 생성에 영향을 미치게 되는 DiT 노이즈 제거 궤적(denoising trajectory) 내의 본질적인 전환점(turning points)을 발견했다. 이 발견에 기반하여, 우리는 다중 이벤트 생성을 위한 추가 학습이 필요 없는 간단하면서도 효과적인 점진적 조향 방법(progressive steering method)인 TunerDiT를 제안한다. TunerDiT는 두 가지 조향 핸들(steering handles)로 구성된다: (1) 이벤트 경계를 강제하면서도 이벤트 간 전환 구간(cross-event transition bands)을 허용하는 이벤트 분할 마스킹(Event-Partitioned Masking); (2) 후반부 정제(late-stage refinement)를 위해 인접 이벤트의 의미(semantics)를 주입하는 이벤트 간 프롬프트 융합(Cross-Event Prompt Fusion). 우리는 다중 이벤트 생성을 벤치마킹하기 위해 자체 큐레이션한 프롬프트 모음인 Meve를 제공한다. TunerDiT는 8가지 지표에서 최고 수준(state-of-the-art)의 성능을 달성하며, 다른 학습 불필요(training-free) 방법들과 비교했을 때 비디오 일관성(video consistency)과 이벤트 분리(event separation) 사이의 조절 가능한 트레이드오프(trade-off)를 제공한다. 텍스트 정렬(text alignment)의 향상은 이벤트 수가 증가함에 따라 커지며, 이는 이벤트 수가 증가함에 따른 스케일링 가능성(scaling possibility)을 시사한다.

## 원문 영어

<details>
<summary>원문 보기</summary>

Text-to-video (T2V) generation faces challenging questions when generating videos with long horizons containing multiple events. Inspired by the intrinsics of the diffusion process, we probe video diffusion transformers (DiTs) and uncover intrinsic turning points in the DiT denoising trajectory where conditioning text affects generation from global layout to fine-grained details. Building on this finding, we present TunerDiT, a simple yet effective progressive steering method that requires no ad

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2605.31590v1)
