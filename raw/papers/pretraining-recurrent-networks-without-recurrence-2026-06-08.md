---
source_url: https://arxiv.org/abs/2606.06479v1
ingested: 2026-06-08
type: paper
arxiv_id: 2606.06479v1
authors: Akarsh Kumar, Phillip Isola
published: 2026-06-04
categories: cs.LG, cs.AI
---

# Pretraining Recurrent Networks without Recurrence

**Authors:** Akarsh Kumar, Phillip Isola
**Published:** 2026-06-04
**arXiv:** https://arxiv.org/abs/2606.06479v1
**Categories:** cs.LG, cs.AI

## Abstract

Training recurrent neural networks (RNNs) requires assigning credit across long sequences of computations. Standard backpropagation through time (BPTT) addresses this problem poorly: it is sequential in time, limiting parallelism, and suffers from vanishing or exploding gradients, making long-range associations difficult to learn. We propose Supervised Memory Training (SMT), a method for training nonlinear RNNs that sidesteps recurrent credit propagation entirely by reducing RNN training to supervised learning on one-step memory transition labels $(m_t, x_{t+1}) \rightarrow m_{t+1}$. SMT acquires these memory labels by training a Transformer-based encoder on a predictive state objective--retaining only information from the past necessary to predict the future. By decoupling what to remember from how to update memory, SMT enables time-parallel RNN training with a stable $O(1)$ length gradient path between any two tokens--without ever unrolling the RNN. We find that SMT outperforms BPTT when pretraining various RNN architectures on tasks like language modeling and pixel sequence modeling. SMT enables nonlinear RNNs to better capture long-range dependencies and train in parallel, potentially unlocking the scaling of models that build temporal abstractions of past experience.
