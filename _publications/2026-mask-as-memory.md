---
title: 'Mask as Memory: Streaming Multi-task Pruning for Vision Transformers'
authors: Ying-Hua Huang, <b>Rui Fang</b>, Hsi-Wen Chen, and Ming-Syan Chen
category: conferences
status: published
date: '2026-09-06'
year: 2026
venue: ECML PKDD 2026, Research Track, 391–409
paperurl: https://doi.org/10.1007/978-3-032-37667-1_23
excerpt: Studies streaming multi-task pruning for Vision Transformers.
collection: publications
permalink: /publication/2026-mask-as-memory/
citation: 'Ying-Hua Huang, <b>Rui Fang</b>, Hsi-Wen Chen, and Ming-Syan Chen. (2026). &quot;Mask as Memory: Streaming Multi-task Pruning for Vision Transformers.&quot; <i>ECML PKDD 2026, Research Track, 391–409</i>.'
---

A pruned Vision Transformer may need to learn new task objectives over time, such as moving from classification to detection or segmentation. A structure chosen for an earlier task can remove pathways needed by a later one, while adapting too freely can damage previously learned capabilities. This paper formulates streaming multi-task pruning and analyzes both catastrophic forgetting and difficulty learning new tasks under static pruning decisions.

PruneStream treats the pruning mask as structural memory. Depth-guided adaptive LoRA decomposition separates shared and task-specific adaptations, and shared-specific importance evaluation uses these adapters to assess backbone parameters. Stability-plasticity mask refinement then combines cross-task importance with task heterogeneity to update the sparse structure. A protection mechanism preserves previously retained parameters while the framework manages adaptation to new objectives.

Experiments cover five heterogeneous vision tasks and compare PruneStream with six baselines. The reported model maintains performance comparable to fully fine-tuned dense models using 50% of the parameters. The work frames pruning as an ongoing structural learning process, with the mask recording which parts of the model should remain available as task requirements change.
