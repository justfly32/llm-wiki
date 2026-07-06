---
title: VT-WAM: Visual-Tactile World Action Model for Contact-Rich Manipulation
created: 2026-07-06
updated: 2026-07-06
type: concept
tags: [research]
sources: [raw/papers/vt-wam-visual-tactile-world-action-model-for-contact-rich-m-2026-07-06.md]
confidence: medium
---

# VT-WAM: Visual-Tactile World Action Model for Contact-Rich Manipulation

> 📄 원문: [VT-WAM: Visual-Tactile World Action Model for Contact-Rich Manipulation](https://arxiv.org/abs/2607.02503v1)
> ✍️ 저자: Shuai Tian, Yupeng Zheng, Yuhang Zheng
> 📅 발행: 2026-07-02
> 🏷️ 카테고리: cs.RO

## 요약

Contact-rich manipulation requires policies to react to local deformation, pressure, slip, and friction, yet these cues are temporally sparse and often invisible in visual observations. Existing visual-tactile policies usually feed tactile observations directly into action prediction, but rarely model tactile deformation dynamics during action generation. In this paper, we introduce VT-WAM, a Visual-Tactile World Action Model that jointly learns future visual prediction, tactile deformation prediction, and action prediction within a unified flow matching framework. In particular, VT-WAM introduces (1) Asymmetric Mixture-of-Transformers (MoT) attention to bridge a first-frame visual anchor with temporal tactile dynamics, and (2) contact-gated Action-Visual-Tactile Attention Guidance (AVTAG) to encourage action queries to rely on tactile evidence during contact phases. Across six real-world contact-rich manipulation tasks, VT-WAM achieves a 71.67% average success rate, outperforming Fast-WAM by 26.67% and OmniVTLA by 35.84%. Ablations demonstrate that modeling tactile deformation dynamics and guiding contact-phase tactile attention are both important for contact-rich tasks. Project website: https://vt-wam.github.io/.

## 원문 영어

<details>
<summary>원문 보기</summary>

Contact-rich manipulation requires policies to react to local deformation, pressure, slip, and friction, yet these cues are temporally sparse and often invisible in visual observations. Existing visual-tactile policies usually feed tactile observations directly into action prediction, but rarely model tactile deformation dynamics during action generation. In this paper, we introduce VT-WAM, a Visual-Tactile World Action Model that jointly learns future visual prediction, tactile deformation pred

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2607.02503v1)
