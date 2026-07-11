---
title: Multi-Resolution Feature Stem for Diabetic Retinopathy lesion segmentation
created: 2026-07-12
updated: 2026-07-12
type: concept
tags: [research, ai-ml, multimodal]
sources: [raw/papers/multi-resolution-feature-stem-for-diabetic-retinopathy-lesio-2026-07-12.md]
confidence: medium
---

# Multi-Resolution Feature Stem for Diabetic Retinopathy lesion segmentation

> 📄 원문: [Multi-Resolution Feature Stem for Diabetic Retinopathy lesion segmentation](https://arxiv.org/abs/2607.08679v1)
> ✍️ 저자: Indranil Dutta, Taehee Jeong
> 📅 발행: 2026-07-09
> 🏷️ 카테고리: cs.CV

## 요약

Diabetic Retinopathy (DR) is a leading cause of preventable blindness worldwide, requiring automated lesion segmentation using deep learning models for early detection and monitoring. However, DR lesions vary dramatically in size from tiny microaneurysms to large hemorrhages and exudates. This variability creates conflicting demands on the model architecture and input resolution, posing a challenge for effective design. This work investigates the impact of input resolution on different lesion types. Through systematic experimentation with multiple architectures (U-Net, UNet++, Vision Transformers, DeepLabV3+) at $512 \times 512$ and $1024 \times 1024$ resolutions, we identify a critical, counter-intuitive phenomenon where increasing input resolution has opposing effects on different lesion types. We demonstrate that while higher resolution is essential for resolving fine-grained microaneurysms, it can unexpectedly degrade performance on larger hemorrhages. This finding challenges the common assumption that higher resolution is uniformly beneficial. To address this, we propose a novel Multi-Resolution Feature Stem, an input-level pyramid integrated with a UNet++ backbone. This architecture processes multiple scales in parallel, capturing fine-grained details without sacrificing contextual information. This work contributes crucial empirical evidence of this complex, resolution-dependent behavior and a practical, parameter-efficient architecture that successfully resolves this trade-off.

## 원문 영어

<details>
<summary>원문 보기</summary>

Diabetic Retinopathy (DR) is a leading cause of preventable blindness worldwide, requiring automated lesion segmentation using deep learning models for early detection and monitoring. However, DR lesions vary dramatically in size from tiny microaneurysms to large hemorrhages and exudates. This variability creates conflicting demands on the model architecture and input resolution, posing a challenge for effective design. This work investigates the impact of input resolution on different lesion ty

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2607.08679v1)
