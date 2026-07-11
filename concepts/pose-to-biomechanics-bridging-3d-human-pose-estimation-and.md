---
title: Pose-to-Biomechanics: Bridging 3D Human Pose Estimation and Biomechanical Attribute Prediction
created: 2026-07-12
updated: 2026-07-12
type: concept
tags: [research, multimodal]
sources: [raw/papers/pose-to-biomechanics-bridging-3d-human-pose-estimation-and-2026-07-12.md]
confidence: medium
---

# Pose-to-Biomechanics: Bridging 3D Human Pose Estimation and Biomechanical Attribute Prediction

> 📄 원문: [Pose-to-Biomechanics: Bridging 3D Human Pose Estimation and Biomechanical Attribute Prediction](https://arxiv.org/abs/2607.08725v1)
> ✍️ 저자: Ayda Eghbalian, Kevin Desai
> 📅 발행: 2026-07-09
> 🏷️ 카테고리: cs.CV, cs.AI, cs.LG

## 요약

Recent progress in 3D human pose estimation has made markerless recovery of skeletal motion increasingly accurate and scalable. However, most pose estimators remain optimized for geometric keypoint accuracy, while many real-world applications in rehabilitation, sports science, ergonomics, and clinical movement analysis require biomechanical quantities that describe how the body moves, loads, and activates. In this work, we propose BioModule, a lightweight plug-in temporal transformer that attaches downstream of any 3D pose estimator and predicts biomechanical attributes from standard 17-joint 3D skeletons. BioModule is estimator-agnostic and requires no modification of the upstream pose model, enabling existing pose estimators to be extended toward physically interpretable motion analysis.   To train and evaluate BioModule, we construct a large-scale aligned dataset pairing Human3.6M video and 3D keypoints with the biomechanical label space of Human3.6Mplus. We establish and verify anatomical correspondence between coordinate systems of the two datasets, enabling frame-accurate cross-modal supervision. Using this aligned supervision, BioModule predicts biomechanical quantities. We further benchmark BioModule across seven state-of-the-art 3D pose estimators, providing the first systematic analysis of how upstream pose estimation quality propagates to downstream biomechanical prediction fidelity. The results position BioModule as a compact, modular bridge between vision-based pose estimation and biomechanically meaningful human motion analysis.

## 원문 영어

<details>
<summary>원문 보기</summary>

Recent progress in 3D human pose estimation has made markerless recovery of skeletal motion increasingly accurate and scalable. However, most pose estimators remain optimized for geometric keypoint accuracy, while many real-world applications in rehabilitation, sports science, ergonomics, and clinical movement analysis require biomechanical quantities that describe how the body moves, loads, and activates. In this work, we propose BioModule, a lightweight plug-in temporal transformer that attach

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2607.08725v1)
