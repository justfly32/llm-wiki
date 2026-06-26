---
source_url: https://arxiv.org/abs/2605.31591v1
ingested: 2026-06-02
type: paper
arxiv_id: 2605.31591v1
authors: Nurjahan Sultana, Moi Hoon Yap, Xinqi Fan
published: 2026-05-29
categories: cs.CV
---

# CoFiDA-M: Concept-Aware Feature Modulation for Cross-Domain Adaptation with Image-Only Inference

**Authors:** Nurjahan Sultana, Moi Hoon Yap, Xinqi Fan
**Published:** 2026-05-29
**arXiv:** https://arxiv.org/abs/2605.31591v1
**Categories:** cs.CV

## Abstract

Models for AI-based skin cancer screening suffer a severe performance drop when shifting from expert dermoscopic (source) images to consumer-grade clinical (target) images, hindering real-world deployment. Existing domain adaptation methods often ignore crucial semantic invariants, such as clinical concepts. While new foundation models like MONET can provide this semantic information as dense, probabilistic scores, this metadata is unavailable at test time, creating a deployment paradox for practical image-only screening tools. We address this gap by proposing CoFiDA-M, a privileged information framework that learns from concepts at training time but deploys as an image-only model. Our method trains a teacher network that uses MONET concept probabilities to guide a FiLM modulator, transforming visual features into a semantically ``edited" feature space. A lightweight, image-only student is then trained to reproduce this edited representation, not just the teacher's final predictions. This distillation ``bakes" the clinical reasoning into the student's weights. On a challenging multi-dataset benchmark, our image-only student significantly outperforms state-of-the-art approaches, especially in melanoma recall. Our work provides a practical and generalizable framework for leveraging noisy, probabilistic metadata as privileged information, demonstrating strong cross-dataset robustness and potential for real-world deployment beyond dermatology. Implementation code is available at: https://github.com/mmu-dermatology-research/CoFiDA.git
