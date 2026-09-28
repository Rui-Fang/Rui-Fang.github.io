---
title: 'LOOPQ: QUANTIZATION FOR LOOPED LANGUAGE MODELS'
collection: publications
category: submissions
authors: <b>Rui Fang</b>, Hsi-Wen Chen, and Ming-Syan Chen
permalink: /publication/2026-loopq/
excerpt: Studies quantization for looped language models that reuse Transformer blocks.
date: 2026-05-01
venue: ICLR 2027
citation: '<b>Rui Fang</b>, Hsi-Wen Chen, and Ming-Syan Chen. (2026). &quot;LOOPQ: QUANTIZATION FOR LOOPED LANGUAGE MODELS.&quot; Submitted to ICLR 2027; under review.'
status: under-review
year: 2026
selected: 3
---

Looped language models increase effective depth by repeatedly applying shared Transformer blocks. This reuse saves parameters but makes post-training quantization sensitive to how computation evolves across loops. The same block encounters different hidden-state distributions, quantized states are passed across loop boundaries, and errors introduced early can accumulate during later iterations. LOOPQ studies these three sources of degradation and develops a quantization framework around them.

The method retains a shared quantized backbone. Loop-aware activation scaling accommodates changes in activation magnitude, while a sharing-sensitivity score identifies a small subset of transformation groups that benefit from loop-specific treatment. Lightweight transition adapters correct hidden states at loop boundaries. Trajectory-aware calibration then coordinates these components by matching full-precision boundary states and final output distributions, addressing error propagation over the complete recurrent computation.

With 4-bit weights and 4-bit activations, the manuscript reports a 67.8% average relative improvement in five-task mean accuracy across four backbones, compared with the strongest static quantization baseline for each comparison. Perplexity experiments further assess language-modeling quality across eight backbone–dataset pairs. The results examine how targeted loop-dependent adaptation can improve low-precision inference while retaining the parameter-sharing advantage of looped models.
