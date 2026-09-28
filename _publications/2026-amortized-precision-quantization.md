---
title: Amortized-Precision Quantization for Early-Exit Vision Transformers
collection: publications
category: conferences
authors: <b>Rui Fang</b>, Hsi-Wen Chen, and Ming-Syan Chen
permalink: /publication/2026-amortized-precision-quantization/
excerpt: Studies quantization under adaptive early-exit computation paths in Vision Transformers.
date: 2026-05-01
venue: NeurIPS 2026
paperurl: https://arxiv.org/abs/2605.07317
citation: <b>Rui Fang</b>, Hsi-Wen Chen, and Ming-Syan Chen. (2026). &quot;Amortized-Precision Quantization for Early-Exit Vision Transformers.&quot; <i>NeurIPS 2026 (accepted)</i>.
status: accepted
year: 2026
selected: 1
---

Early-exit Vision Transformers save computation by allowing an input to stop before the final layer. Quantization can further reduce arithmetic cost, but the two mechanisms interact: quantization noise can change intermediate predictions and exit decisions, while different layers are used with different frequencies. A precision assignment optimized for full-depth inference may therefore be poorly matched to an early-exit model.

Amortized-Precision Quantization accounts for this unequal layer utilization through stochastic layer exposure. It treats the cost of a precision choice in relation to how often the corresponding computation is reached, connecting bit-width allocation with the model's effective depth. The MAQEE framework uses bi-level optimization to coordinate quantization bit widths and exit thresholds, with explicit risk control for the resulting predictions.

Experiments cover image classification, object detection, and semantic segmentation. The reported configurations reduce bit operations by up to 95% while maintaining task accuracy. These results illustrate why depth and precision should be optimized together: the useful operating point depends on both the arithmetic precision of a layer and the probability that an input needs it.
