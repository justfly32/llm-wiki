---
source_url: https://arxiv.org/abs/2606.06423v1
ingested: 2026-06-08
type: paper
arxiv_id: 2606.06423v1
authors: Qi Lan, Yining Tang, Yu Shen
published: 2026-06-04
categories: cs.RO, cs.AI
---

# RiskFlow: Fast and Faithful Safety-Critical Traffic Scenario Generation

**Authors:** Qi Lan, Yining Tang, Yu Shen
**Published:** 2026-06-04
**arXiv:** https://arxiv.org/abs/2606.06423v1
**Categories:** cs.RO, cs.AI

## Abstract

Safety-critical traffic scenario generation is essential for evaluating autonomous driving systems under rare but high-risk interactions. Existing diffusion-based methods offer strong controllability in closed-loop generation, but their iterative denoising process is computationally expensive and may accumulate sampling and guidance errors over long rollouts, causing unrealistic motion artifacts such as jitter, abnormal acceleration, and off-road behavior. To address these issues, we propose RiskFlow, a closed-loop safety-critical multi-agent traffic generation framework that formulates future trajectory generation as transport in the action space. Instead of relying on iterative denoising, RiskFlow learns an average velocity field over a finite interval to transform Gaussian action sequences into future acceleration and yaw-rate commands with a single forward pass, using a JVP-based objective for efficient and stable training. At test time, RiskFlow applies output-space guidance to the generated actions, steering selected critical agents toward risky interactions while regularizing off-road behavior, and reconstructs physically feasible trajectories through vehicle dynamics. Experiments on nuScenes with tbsim closed-loop evaluation show that RiskFlow achieves a strong adversariality-realism trade-off across multi-agent and long-horizon settings. Compared with representative baselines, RiskFlow consistently improves realism while maintaining competitive safety-critical generation capability, and substantially reduces inference time for evaluation.
