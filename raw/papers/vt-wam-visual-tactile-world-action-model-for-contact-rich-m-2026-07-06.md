---
source_url: https://arxiv.org/abs/2607.02503v1
ingested: 2026-07-06
type: paper
arxiv_id: 2607.02503v1
authors: Shuai Tian, Yupeng Zheng, Yuhang Zheng
published: 2026-07-02
categories: cs.RO
---

# VT-WAM: Visual-Tactile World Action Model for Contact-Rich Manipulation

**Authors:** Shuai Tian, Yupeng Zheng, Yuhang Zheng
**Published:** 2026-07-02
**arXiv:** https://arxiv.org/abs/2607.02503v1
**Categories:** cs.RO

## Abstract

Contact-rich manipulation requires policies to react to local deformation, pressure, slip, and friction, yet these cues are temporally sparse and often invisible in visual observations. Existing visual-tactile policies usually feed tactile observations directly into action prediction, but rarely model tactile deformation dynamics during action generation. In this paper, we introduce VT-WAM, a Visual-Tactile World Action Model that jointly learns future visual prediction, tactile deformation prediction, and action prediction within a unified flow matching framework. In particular, VT-WAM introduces (1) Asymmetric Mixture-of-Transformers (MoT) attention to bridge a first-frame visual anchor with temporal tactile dynamics, and (2) contact-gated Action-Visual-Tactile Attention Guidance (AVTAG) to encourage action queries to rely on tactile evidence during contact phases. Across six real-world contact-rich manipulation tasks, VT-WAM achieves a 71.67% average success rate, outperforming Fast-WAM by 26.67% and OmniVTLA by 35.84%. Ablations demonstrate that modeling tactile deformation dynamics and guiding contact-phase tactile attention are both important for contact-rich tasks. Project website: https://vt-wam.github.io/.
