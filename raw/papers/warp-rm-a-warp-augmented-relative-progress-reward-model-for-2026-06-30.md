---
source_url: https://arxiv.org/abs/2606.28320v1
ingested: 2026-06-30
type: paper
arxiv_id: 2606.28320v1
authors: Justin Yu, Andrew Goldberg, Kavish Kondap
published: 2026-06-26
categories: cs.RO
---

# WARP-RM: A Warp-Augmented Relative Progress Reward Model for Data Curation

**Authors:** Justin Yu, Andrew Goldberg, Kavish Kondap
**Published:** 2026-06-26
**arXiv:** https://arxiv.org/abs/2606.28320v1
**Categories:** cs.RO

## Abstract

Scaling imitation learning requires large datasets, yet human teleoperation inevitably produces mixed-quality demonstrations containing hesitations and recoveries. Prior frame-level progress reward models supervise on absolute temporal progress proxies that suffer from label noise, or require costly human annotations to define subtask boundaries. We present WARP (Warp-Augmented Relative Progress), a novel fully self-supervised algorithm for learning dense, signed relative progress magnitudes directly from successful demonstrations. WARP generates per-frame progress targets via time-warp augmentations of demonstrations (variable playback speeds and reversals) and we train WARP-RM to predict the normalized elapsed time between input frames. Aggregating these predictions across overlapping windows yields a dense frame-level progress signal. We then introduce WARP-BC, which leverages these scalar reward estimates to upweight high-advantage action chunks during behavior cloning, where chunk-level advantage is obtained by aggregating per-frame rewards. We evaluate our approach on a physical bimanual robot system performing a long-horizon deformable object manipulation task: folding T-shirts from a random crumpled start. To evaluate policy robustness against suboptimal data, we construct training datasets of varying quality using episode length as a proxy for teleoperation sub-optimality. As the dataset is widened to admit more inefficiencies, WARP-BC maintains a 19/20 success rate compared to vanilla BC's collapse to 2/20, improving throughput by up to 18x.
