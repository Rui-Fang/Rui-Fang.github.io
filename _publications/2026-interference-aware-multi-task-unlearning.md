---
title: Interference-Aware Multi-Task Unlearning
collection: publications
category: preprints
authors: Ying-Hua Huang, <b>Rui Fang</b>, Hsi-Wen Chen, and Ming-Syan Chen
permalink: /publication/2026-interference-aware-multi-task-unlearning/
excerpt: Develops an interference-aware approach to unlearning across multiple tasks.
date: 2026-05-01
venue: arXiv preprint arXiv:2605.19042
paperurl: https://arxiv.org/abs/2605.19042
citation: Ying-Hua Huang, <b>Rui Fang</b>, Hsi-Wen Chen, and Ming-Syan Chen. (2026). &quot;Interference-Aware Multi-Task Unlearning.&quot; <i>arXiv preprint arXiv:2605.19042</i>.
status: preprint
year: 2026
---

Unlearning in a multi-task model is complicated by parameter sharing. Removing information associated with one task can also change predictions for other tasks or unrelated training instances. The paper distinguishes full-task unlearning, which removes an instance's influence across all tasks, from partial-task unlearning, which removes selected task supervision while retaining other information associated with that instance.

The proposed framework addresses interference at two levels. Task-aware gradient projection constrains updates to task-specific subspaces, reducing unwanted changes to other task objectives. Instance-level gradient orthogonalization further limits conflicts between the examples being forgotten and those that should be retained. Together, these mechanisms make the unlearning update sensitive to both the requested scope of removal and the shared structure of the model.

Experiments span two vision benchmarks and five tasks, with separate evaluations for full-task and partial-task requests. The reported reductions in Unlearning Impact Score (UIS) relative to the strongest baseline are 30.3% and 52.9%, respectively. The study emphasizes evaluating retained behavior alongside forgetting quality, since successful removal in a shared model also requires controlling its effects outside the requested target.
