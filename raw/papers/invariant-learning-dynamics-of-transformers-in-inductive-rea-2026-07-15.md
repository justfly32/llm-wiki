---
source_url: https://arxiv.org/abs/2607.11875v1
ingested: 2026-07-15
type: paper
arxiv_id: 2607.11875v1
authors: Tiberiu Musat, Tiago Pimentel, Nicholas Zucchet
published: 2026-07-13
categories: cs.LG, cs.AI
---

# Invariant Learning Dynamics of Transformers in Inductive Reasoning Tasks

**Authors:** Tiberiu Musat, Tiago Pimentel, Nicholas Zucchet
**Published:** 2026-07-13
**arXiv:** https://arxiv.org/abs/2607.11875v1
**Categories:** cs.LG, cs.AI

## Abstract

We present a theoretical framework to explain the emergence of inductive reasoning abilities in Transformer language models. While previous works on Transformer learning dynamics have so far been mostly tied to specific tasks, we study a generalized class of inductive tasks that unifies several synthetic tasks known in the literature, including in-context n-grams and multi-hop reasoning. In this class, we theoretically prove that the training dynamics of attention models can be confined to a highly interpretable, low-dimensional invariant manifold. On this manifold, the learning dynamics are captured by a handful of interpretable coordinates rather than millions of parameters, making both theoretical and empirical analysis more tractable. Using this framework, we characterize how data statistics govern the competition between in-context and in-weights learning, we study how random initializations determine the `winning' circuit when multiple solutions are possible, and we demonstrate that the coordinate frame associated with the manifold can be used to automatically detect which circuits have been learned in trained models. By casting circuit formation as a low-dimensional dynamical phenomenon, we take a step toward a predictive theory of how Transformers learn.
