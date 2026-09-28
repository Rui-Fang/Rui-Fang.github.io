---
title: 'BiLEE: Bi-Level Early Exiting for Generative Document Retrieval'
collection: publications
category: conferences
authors: <b>Rui Fang</b>, Chin-Yuan Yeh, Hsi-Wen Chen, and Ming-Syan Chen
permalink: /publication/2024-bilee/
excerpt: Introduces bi-level early exiting for faster generative document retrieval.
date: 2024-10-01
venue: 'ECAI 2024: 27th European Conference on Artificial Intelligence, 4035-4042'
paperurl: https://doi.org/10.3233/FAIA240971
citation: '<b>Rui Fang</b>, Chin-Yuan Yeh, Hsi-Wen Chen, and Ming-Syan Chen. (2024). &quot;BiLEE: Bi-Level Early Exiting for Generative Document Retrieval.&quot; <i>ECAI 2024: 27th European Conference on Artificial Intelligence</i>, 4035-4042.'
status: published
year: 2024
---

Generative document retrieval identifies relevant documents by generating their identifier tokens. These identifiers encode a hierarchy, so an incorrect early token can send retrieval into the wrong branch. Meanwhile, beam search spends computation on candidate sequences that may already be unlikely to lead to useful documents. Applying a uniform early-exit rule therefore overlooks both the varying difficulty of token positions and the uneven value of search candidates.

BiLEE combines early exiting at two levels. Layer Level Early Exiting allows token prediction to stop at an intermediate Transformer layer when confidence exceeds a calibrated threshold. Its thresholds account for the hierarchical structure of document identifiers and differences between token positions. Token Level Early Exiting terminates unpromising candidate sequences, reducing the number of beams that continue through decoding. The two mechanisms control how deeply each token is processed and how much search effort each candidate receives.

The experiments show that these complementary decisions can double retrieval inference speed and reduce FLOPs by a factor of 13 while preserving comparable retrieval accuracy. The study examines acceleration in the document-retrieval setting, where maintaining the quality of complete identifiers is essential.
