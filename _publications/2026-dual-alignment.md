---
title: Dual Alignment Framework for Few-shot Learning with Inter-Set and Intra-Set Shifts
collection: publications
category: conferences
authors: Siyang Jiang, <b>Rui Fang</b>, Hsi-Wen Chen, Wei Ding, Guoliang Xing, and Ming-Syan Chen
permalink: /publication/2026-dual-alignment/
excerpt: Addresses few-shot learning under both inter-set and intra-set distribution shifts.
date: 2026-01-01
venue: Advances in Neural Information Processing Systems 38, 64804-64830
paperurl: https://openreview.net/forum?id=qMWD6qYHdk
codeurl: https://github.com/siyang-jiang/DUAL
citation: Siyang Jiang, <b>Rui Fang</b>, Hsi-Wen Chen, Wei Ding, Guoliang Xing, and Ming-Syan Chen. (2026). &quot;Dual Alignment Framework for Few-shot Learning with Inter-Set and Intra-Set Shifts.&quot; <i>Advances in Neural Information Processing Systems</i>, 38, 64804-64830.
status: published
year: 2026
---

Few-shot learning usually assumes that a small labeled support set provides a reliable reference for classifying query examples. In practice, distribution shifts can occur between the support and query sets and within either set. These effects can distort class structure simultaneously, making alignment based on only one type of shift insufficient. This paper studies their joint effect through a dual-shift query-support setting.

DUAL first repairs feature embeddings using a network trained with perturbed examples and adversarially constructed hard examples. The objective is to recover cleaner representations before performing distribution alignment. A two-stage optimal-transport procedure then addresses the remaining mismatch: it first aligns support instances to reduce within-class dispersion, and subsequently aligns the query distribution with support anchors. Negative-entropy regularization is used in the transport formulation.

The paper provides a theoretical analysis of the alignment framework and evaluates it on three image datasets against ten baselines. The experiments examine robustness when inter-set and intra-set shifts coexist, showing the benefit of combining representation repair with separate alignment stages for the two sources of variation.
