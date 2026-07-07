---
title: From Fixed to Free Cameras: Calibration-Free View-Robust Vision-Language-Action Model
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [research, multimodal]
sources: [raw/papers/from-fixed-to-free-cameras-calibration-free-view-robust-vis-2026-07-08.md]
confidence: medium
---

# From Fixed to Free Cameras: Calibration-Free View-Robust Vision-Language-Action Model

> 📄 원문: [From Fixed to Free Cameras: Calibration-Free View-Robust Vision-Language-Action Model](https://arxiv.org/abs/2607.05396v1)
> ✍️ 저자: Wenhao Li, Xueying Jiang, Quanhao Qian
> 📅 발행: 2026-07-06
> 🏷️ 카테고리: cs.CV, cs.AI, cs.LG

## 요약

Real-world robot deployment rarely maintains the training-stage camera setup, where cameras often experience repositioning or remounting depending on actual scenarios. Existing view-robust Vision-Language-Action (VLA) policies tolerate such camera variations only when the camera extrinsics are explicitly provided, making them fragile and hard to use especially when view robustness is critical. We argue that the policy should not be told where the camera is, but rather figure it out by itself. To this end, we introduce Camera-Centric VLA (CamVLA), a new VLA model that decouples manipulation controls from camera geometry by predicting (i) a camera-centric end-effector action expressed in the local camera frame, and (ii) a 6-DoF hand-eye matrix relating cameras to the robot base. A deterministic geometric transformation composes the two predictions into a robot base-frame action. This disentangles how I should move in pose-independent camera-centric action generation from where I am looking from in camera-perspective geometric grounding. The resulting policy is calibration-free, depth-free, and single-view, requiring only a single monocular RGB image as the visual observation and task instruction at deployment. Evaluations in both simulation and real-world robot data show that CamVLA consistently improves success rates across diverse unseen viewpoints. Project page: https://alibaba-damo-academy.github.io/CamVLA/.

## 원문 영어

<details>
<summary>원문 보기</summary>

Real-world robot deployment rarely maintains the training-stage camera setup, where cameras often experience repositioning or remounting depending on actual scenarios. Existing view-robust Vision-Language-Action (VLA) policies tolerate such camera variations only when the camera extrinsics are explicitly provided, making them fragile and hard to use especially when view robustness is critical. We argue that the policy should not be told where the camera is, but rather figure it out by itself. To

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2607.05396v1)
