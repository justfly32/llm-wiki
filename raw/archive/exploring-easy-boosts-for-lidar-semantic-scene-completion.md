---
title: LiDAR Semantic Scene Completion을 위한 간단한 성능 향상 기법 탐구
created: 2026-06-04
updated: 2026-06-04
type: concept
tags: [research, programming, multimodal]
sources: [raw/papers/exploring-easy-boosts-for-lidar-semantic-scene-completion-2026-06-04.md]
confidence: medium
---

# LiDAR Semantic Scene Completion을 위한 간단한 성능 향상 기법 탐구

> 📄 원문: [Exploring Easy Boosts for Lidar Semantic Scene Completion](https://arxiv.org/abs/2606.03992v1)
> ✍️ 저자: Tetiana Martyniuk, Jonathan Seele, Alexandre Boulch
> 📅 발행: 2026-06-02
> 🏷️ 카테고리: cs.CV, cs.RO

## 요약

본 논문에서는 복잡한 아키텍처 재설계 없이 LiDAR 의미론적 장면 완성(SSC, Semantic Scene Completion)의 성능을 향상시키는 "공짜 점심(free lunch)" 전략을 조사합니다. 먼저, 기존 세그멘테이션 모델(off-the-shelf segmentors)로부터 의미론적 의사 레이블(semantic pseudo-labels)을 입력 포인트 클라우드에 부여하면 기존 아키텍처의 성능이 크게 향상됨을 보여줍니다. 이러한 모델을 오라클(oracle)과 비교 평가함으로써, 고품질 의미론적 사전 정보(semantic priors)가 mIoU 향상의 주요 원인임을 확인합니다. 또한, 빈 공간과 미지 공간을 구분하는 가시성 정보(visibility information)를 입력 LiDAR 스캔에 추가함으로써, 테스트된 모든 아키텍처에서 부수적인 성능 향상을 얻을 수 있음을 보여줍니다. 이러한 간단한 개선만으로도 오래된 모델들이 최신 시스템(state-of-the-art systems)과 경쟁력을 유지하며, 심지어 이를 능가할 수 있음을 관찰했습니다. 본 연구의 코드는 https://github.com/astra-vision/SSC-Priors에서 공개되어 있습니다.

## 원문 영어

<details>
<summary>원문 보기</summary>

This paper investigates "free lunch" strategies to boost the performance of lidar semantic scene completion (SSC) without requiring complex architectural redesigns. We first demonstrate that endowing input point clouds with semantic pseudo-labels from off-the-shelf segmentors significantly improves the performance of existing architectures. By evaluating these models against an oracle, we establish that high-quality semantic priors are a primary driver of mIoU gains. Furthermore, we equip the in

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2606.03992v1)
