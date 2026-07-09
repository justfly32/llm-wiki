---
source_url: https://arxiv.org/abs/2607.07680v1
ingested: 2026-07-10
type: paper
arxiv_id: 2607.07680v1
authors: Eitan Levin, Venkat Chandrasekaran
published: 2026-07-08
categories: math.ST, cs.LG, math.PR
---

# Any-Dimensional Learning by Sampling

**Authors:** Eitan Levin, Venkat Chandrasekaran
**Published:** 2026-07-08
**arXiv:** https://arxiv.org/abs/2607.07680v1
**Categories:** math.ST, cs.LG, math.PR

## Abstract

Many machine learning models are defined for inputs of different sizes, such as point clouds containing different numbers of points, sequences of tokens of different lengths, and graphs on different numbers of nodes. Such models are trained on finitely-many examples of necessarily limited sizes. How well do these models generalize from inputs of small size to larger inputs of size not seen during training? Furthermore, evaluating such models on large inputs is often expensive. How can we sketch large inputs to obtain smaller ones on which the model takes similar values? At the heart of both questions is the need to compare inputs of different sizes and to approximate large inputs by small ones. We present a unified approach to address these questions by using random sampling maps to compare inputs of different sizes. The sampling maps we consider are generalizations of sampling with replacement, random binning, and species sampling. We characterize the application domains in which each type of sampling is appropriate in terms of the symmetries and relations between problem instances of different sizes in the domain. Our framework yields explicit generalization and sketching rates for function classes continuous with respect to a chosen notion of sampling, encompassing large families of functions defined on sequences, graphs, and tensors of different sizes. Specific examples include moment polynomials on measures, homomorphism densities and numbers of graphs, permutation-invariant transformers, and graph neural networks.
