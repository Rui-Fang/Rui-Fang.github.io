---
title: 'LoGIC: Multi-LoRA Guided Importance Consensus for Multi-Task Pruning in Vision Transformers'
collection: publications
category: conferences
authors: Yu-Hong Chou<sup>*</sup>, <b>Rui Fang</b><sup>*</sup>, Hsi-Wen Chen, and Ming-Syan Chen
permalink: /publication/2026-logic/
excerpt: Proposes Multi-LoRA guided importance consensus for multi-task pruning in Vision Transformers.
date: 2026-04-01
venue: Proceedings of the AAAI Conference on Artificial Intelligence 40(25), 20588-20596
paperurl: https://doi.org/10.1609/aaai.v40i25.39195
citation: 'Yu-Hong Chou<sup>*</sup>, <b>Rui Fang</b><sup>*</sup>, Hsi-Wen Chen, and Ming-Syan Chen. (2026). &quot;LoGIC: Multi-LoRA Guided Importance Consensus for Multi-Task Pruning in Vision Transformers.&quot; <i>Proceedings of the AAAI Conference on Artificial Intelligence</i>, 40(25), 20588-20596.'
equal_contribution: true
status: published
selected: 4
year: 2026
---

A shared Vision Transformer can support several tasks through low-rank adapters, but pruning the backbone using a single task's importance scores can remove parameters needed by another. The adapters also have their own redundancy and structural dependencies on the backbone. LoGIC addresses these coupled decisions by using signals from multiple LoRA modules to guide a common pruning process.

The method proceeds in two phases. It first prunes the LoRA modules with task-consistent structured masks. A task-adaptive gate balances shared and task-specific paths, allowing specialization within a deployable sparse structure. It then prunes the frozen backbone using cross-task importance consensus. The importance assessment combines gradient sensitivity, task-dependent routing, and adaptation magnitude to preserve parameters that are broadly useful or particularly important to an individual task.

Across five vision benchmarks, LoGIC reaches up to 50% structured sparsity while retaining competitive accuracy. The experiments examine the consequences of pruning across task boundaries, supporting the use of shared and specialized importance signals together when compressing a multi-task backbone.
