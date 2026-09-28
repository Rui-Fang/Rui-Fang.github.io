---
title: Dual-Triangular QR Decomposition with Global Acceleration and Partially Q-Rotation Skipping
collection: publications
category: conferences
authors: <b>Rui Fang</b>, Siyang Jiang, Hsi-Wen Chen, Wei Ding, and Ming-Syan Chen
permalink: /publication/2022-dual-triangular-qr/
excerpt: Presents an optimized QR decomposition method with global acceleration and partial Q-rotation skipping.
date: 2022-12-01
venue: 2022 International Conference on Field-Programmable Technology (ICFPT), 1-4
paperurl: https://doi.org/10.1109/ICFPT56656.2022.9974402
citation: <b>Rui Fang</b>, Siyang Jiang, Hsi-Wen Chen, Wei Ding, and Ming-Syan Chen. (2022). &quot;Dual-Triangular QR Decomposition with Global Acceleration and Partially Q-Rotation Skipping.&quot; <i>2022 International Conference on Field-Programmable Technology (ICFPT)</i>, 1-4.
status: published
year: 2022
---

Tall-and-skinny QR decomposition is an important operation in data compression and feature extraction. One of its central steps combines triangular factors through dual-triangular QR decomposition. Although the input already has considerable structure, a general decomposition routine can still perform unnecessary rotations and intermediate updates. This work investigates how the structure of both the orthogonal factor Q and the triangular factor R can be used to reduce that work.

The proposed acceleration framework combines two mechanisms. Global Acceleration Schemes reorganize the triangular input, compute diagonal elements in parallel, and pipeline subsequent operations. Partially Q-Rotation Skipping identifies updates that can be omitted because of the structure that emerges in Q. Considering both factors exposes opportunities that are missed when optimization focuses only on R.

The framework is implemented using one-dimensional and two-dimensional systolic arrays through high-level synthesis. These architectures organize data movement and reuse to reduce memory requirements while supporting parallel computation. The hardware evaluation compares latency and computational resources, showing how algorithmic simplification and the systolic organization jointly accelerate this structured matrix operation.
