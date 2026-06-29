---
title: StructSplat: Generalizable 3D Gaussian Splatting from Uncalibrated Sparse Views
created: 2026-06-30
updated: 2026-06-30
type: concept
tags: [research, programming, alignment, optimization, multimodal]
sources: [raw/papers/structsplat-generalizable-3d-gaussian-splatting-from-uncali-2026-06-30.md]
confidence: medium
---

# StructSplat: Generalizable 3D Gaussian Splatting from Uncalibrated Sparse Views

> 📄 원문: [StructSplat: Generalizable 3D Gaussian Splatting from Uncalibrated Sparse Views](https://arxiv.org/abs/2606.28321v1)
> ✍️ 저자: Jia-Chen Zhao, Beiqi Chen, Xinyang Chen
> 📅 발행: 2026-06-26
> 🏷️ 카테고리: cs.CV

## 요약

본 문에서는 카메라 파라미터 없이 미보정(uncalibrated) 이미지에 직접 작동하는 피드포워드(feed-forward) 기반 범용 3D 가우시안 재구성 프레임워크인 StructSplat을 제안합니다. 기존 방법들은 장면별 최적화(per-scene optimization)에 의존하거나 알려진 카메라 포즈(camera poses)를 가정하며, 통합된 백본(backbone) 내에서 기하(geometry)와 외관(appearance)을 합하여 재구성 충실도와 일반화 성능을 제한합니다. 우리의 핵심 아이디어는 재구성 과정에서 기하, 의미론(semantic), 스처(texture) 단서에 명확한 역할을 부여하는 구조화된 현(structured representation)을 채택하는 것입니다. 구체적으로, 2D 관찰로부터 정확한 스처 모델링을 가능하게 하는 픽 정 특징 주입(pixel-aligned feature injection) 메커니즘을 도입하고, 의미론적 사전 지식(semantic-aware priors)을 통합하여 전역적 일관성을 개선하며, 정보 누출을 방지하고 일반화 성능을 향상시키기 위한 카메라 정렬(camera alignment) 전략을 설계했습니다. 실험 결과, 본 방법은 까다로운 치마크에서 기존 방법들을 크게 능가합니다. DL3DV에서 본 방법은 28.045 PSNR을 달성하여 AnySplat(22.377) 대비 +5.67 dB 향상을 보였습니다. 교차 데이터(cross-dataset) 평가에서도 ACID에서 AnySplat 대비 +1.94 dB, RealEstate10K에서 +1.72 dB의 향상을 달성했습니다. 프로젝트 페이지: https://structsplat.github.io 코드: https://github.com/J-C-Zhao/StructSplat

## 원문 영어

<details>
<summary>원문 보기</summary>

We present StructSplat, a feed-forward and generalizable 3D Gaussian reconstruction framework that operates directly on uncalibrated images without requiring camera parameters. Existing methods either rely on per-scene optimization or assume known camera poses, and often entangle geometry and appearance within a unified backbone, limiting reconstruction fidelity and generalization. Our key idea is to adopt a structured representation that organizes geometry, semantic, and texture cues with expli

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2606.28321v1)
