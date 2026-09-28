---
title: 'HSMLog: Small Language Model-Assisted Hardware Security Module Log Anomaly Detection with Behavioral Analysis'
authors: Chia-Hsuan Wu, Dar-Hsin Dustin Wu, <b>Rui Fang</b>, Yi-Ting Lee, Chia-Chih Lin, and Ming-Syan Chen
category: conferences
status: accepted
date: '2026-08-30'
year: 2026
venue: ISSRE 2026, Industry Track
paperurl: https://arxiv.org/abs/2608.29773
excerpt: Combines small language models with retrieval-grounded behavioral analysis to detect anomalies in hardware security module logs.
collection: publications
permalink: /publication/2026-hsmlog/
citation: 'Chia-Hsuan Wu, Dar-Hsin Dustin Wu, <b>Rui Fang</b>, Yi-Ting Lee, Chia-Chih Lin, and Ming-Syan Chen. (2026). &quot;HSMLog: Small Language Model-Assisted Hardware Security Module Log Anomaly Detection with Behavioral Analysis.&quot; <i>ISSRE 2026, Industry Track</i> (accepted).'
---

Hardware security module logs record operations whose security meaning depends on their context: key histories, object states, sessions, and timing can distinguish a legitimate sequence from a suspicious one. Detecting anomalies from isolated log entries can miss these relationships. HSMLog uses a small language model to analyze behavior across structured log windows and relate candidate anomalies to operational policies.

The system has two stages. First, a policy-guided analysis of each window proposes suspicious events. A second review stage brings together retrieved policies, related logs, and historical records associated with suspicious keys to assess candidates conservatively and assemble incidents. Historical evidence is restricted to information available before the alert window, so the assessment does not benefit from future records.

Evaluation uses real industrial background logs augmented with anomaly scenarios developed with industry partners. In this setting, HSMLog reports 98.97% precision, 96.00% recall, and a 97.46% F1 score, with 98.66% event coverage. The results assess the combined role of contextual behavioral analysis and evidence-based candidate review in reducing missed events and false alerts.
