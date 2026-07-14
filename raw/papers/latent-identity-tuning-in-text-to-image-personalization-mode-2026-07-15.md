---
source_url: https://arxiv.org/abs/2607.11885v1
ingested: 2026-07-15
type: paper
arxiv_id: 2607.11885v1
authors: Daniel Garibi, Ronen Kamenetsky, Hadar Averbuch-Elor
published: 2026-07-13
categories: cs.CV, cs.GR
---

# Latent-Identity Tuning in Text-to-Image Personalization Models

**Authors:** Daniel Garibi, Ronen Kamenetsky, Hadar Averbuch-Elor
**Published:** 2026-07-13
**arXiv:** https://arxiv.org/abs/2607.11885v1
**Categories:** cs.CV, cs.GR

## Abstract

Generating and editing a person's face demands high precision, as even minor modifications can significantly alter a subject's perceived identity. Current personalization and editing methods built on general-purpose text-to-image models, however, often lack the precision required for fine-grained facial edits. We present a method for fine-grained identity tuning in text-to-image personalization models. Unlike standard image editing, which operates on a given image, identity tuning modifies the latent representation of a specific identity, enabling the generation of diverse images that consistently depict the same edited identity. To enable fine-grained latent identity tuning, we explore the latent space of a pre-trained, frozen encoder for text-to-image personalization. Our approach requires no additional training. Instead, it leverages the existing architecture of a frozen encoder to uncover latent semantic directions. This space consists of a set of latent tokens that play distinct roles in capturing different aspects of an identity and often correspond to specific spatial or semantic facial regions. We show that meaningful directions can be identified within this space and within subspaces defined by selected tokens, enabling localized, fine-grained, and semantically coherent edits. We validate our approach through qualitative and quantitative experiments that demonstrate diverse localized facial edits while preserving cross-image identity consistency. Project page at: https://garibida.github.io/IdentityTuning/
