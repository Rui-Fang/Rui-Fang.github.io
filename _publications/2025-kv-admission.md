---
title: 'KV Admission: Learning What to Write for Efficient Long-Context Inference'
collection: publications
category: conferences
authors: Yen-Chieh Huang, Pi-Cheng Hsiu, <b>Rui Fang</b>, and Ming-Syan Chen
permalink: /publication/2025-kv-admission/
excerpt: Learns what to admit into the KV cache to improve long-context inference efficiency.
date: 2025-12-01
venue: EMNLP 2026
paperurl: https://arxiv.org/abs/2512.17452
codeurl: https://github.com/EMCLab-Sinica/WG-KV
citation: 'Yen-Chieh Huang, Pi-Cheng Hsiu, <b>Rui Fang</b>, and Ming-Syan Chen. (2026). &quot;KV Admission: Learning What to Write for Efficient Long-Context Inference.&quot; <i>EMNLP 2026 (accepted)</i>.'
status: accepted
year: 2026
selected: 2
---

Long-context language-model inference requires storing and repeatedly reading a large key-value cache. Many cache-management methods decide which entries to retrieve or evict after they have been written. This leaves an earlier decision largely implicit: whether a token's key and value should enter persistent cache storage in the first place. The paper separates cache admission, selection, and eviction as distinct causal decisions.

WG-KV learns an admission policy that predicts token utility before a cache write. A lightweight predictor determines which information merits longer-term retention, while a sliding local cache preserves recent context. This combination maintains a compact global cache without relying solely on removing entries after the cache has grown. Making the decision at write time targets costs incurred during both prompt processing and subsequent decoding.

The evaluation studies the resulting trade-off between inference quality, memory consumption, and latency for long-context workloads. The central contribution is an explicit learned write policy: cache efficiency depends not only on how stored information is accessed, but also on which information is admitted to persistent storage.
