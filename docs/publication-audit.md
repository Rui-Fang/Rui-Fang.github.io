# Publication reconciliation — 2026-09-28

The public [Google Scholar profile](https://scholar.google.com/citations?user=If-6koYAAAAJ&hl=en&pagesize=100) returned 12 records. The current remote repository had 10 records; all ten were preserved, with the changes below. No citation counts are copied to the website because they change frequently.

## User-confirmed updates

- Amortized-Precision Quantization: accepted at NeurIPS 2026. Keep the existing arXiv link, stable permalink, and authors; move into conference papers.
- KV Admission: accepted at EMNLP 2026. Keep the existing arXiv and code links and 2025 permalink; display 2026 as the conference year.
- LOOPQ: title changed to `LOOPQ: QUANTIZATION FOR LOOPED LANGUAGE MODELS`; under review at ICLR 2027. Keep the existing permalink and authors. Omit the old arXiv link pending the user's updated URL. The manuscript year remains 2026; ICLR 2027 is the submission venue, not an accepted publication.

## Added records

- Mask as Memory: Streaming Multi-task Pruning for Vision Transformers. Scholar lists ECML PKDD 2026 and authors Y.-H. Huang, R. Fang, H.-W. Chen, M.-S. Chen. [Springer proceedings](https://link.springer.com/book/10.1007/978-3-032-37667-1?page=2) confirm that order and pages 391–409; the chapter link is https://doi.org/10.1007/978-3-032-37667-1_23. The publisher lists online publication in September 2026 with a 2027 copyright year; retain the Scholar/conference year 2026.
- HSMLog: Small Language Model-Assisted Hardware Security Module Log Anomaly Detection with Behavioral Analysis. [arXiv:2608.29773](https://arxiv.org/abs/2608.29773) confirms the full author list, submitted August 30, 2026, and acceptance to the ISSRE 2026 Industry Track. Scholar still labels it a preprint; the explicit author-provided arXiv acceptance note is used.

## Preserved records

3-D ECG (CMPB), Dual-Triangular QR (ICFPT), BiLEE (ECAI), SEAL (EDGE), Dual Alignment (NeurIPS proceedings), Interference-Aware Multi-Task Unlearning (preprint), and LoGIC (AAAI). The Dual Alignment record retains its existing 2026 proceedings year as also listed by Scholar; the conference itself was NeurIPS 2025.

The web CV uses the same collection as the publications list. The downloadable PDF was replaced with the September 28, 2026 CV, containing all 12 records and the authorship/status updates above. Its LaTeX source is maintained separately in the CV_Latex repository.

## Authorship correction

The user confirmed that Yu-Hong Chou and Rui Fang are co-first authors of LoGIC. Both names carry an asterisk; the shared listing and detail templates explain equal contribution, including on the web CV.

## Expanded paper overviews

All 12 detail pages now contain three paragraphs covering the research problem, method, and evaluation. Short front-matter excerpts remain available for metadata; the detail template renders the body without repeating the excerpt. Existing publication status and authorship are preserved.

Sources checked for the expanded text:

- 3-D ECG, Dual-Triangular QR, BiLEE, and LoGIC: the manuscripts already in `files/2021-CMPB.pdf`, `files/2022-ICFPT.pdf`, `files/2024-ECAI.pdf`, and `files/2026-AAAI-LoGIC.pdf`.
- KV Admission: [arXiv v4](https://arxiv.org/abs/2512.17452v4), including admission before cache writes and the global/local cache design.
- APQ: [author abstract](https://arxiv.org/abs/2605.07317), including utilization-aware precision, MAQEE, and the reported BOP reduction.
- Dual Alignment: [official NeurIPS proceedings](https://proceedings.nips.cc/paper_files/paper/2025/hash/5dc387343572bb95f264e05b66e83951-Abstract-Conference.html).
- HSMLog: [author abstract](https://arxiv.org/abs/2608.29773). The overview explicitly retains the experimental condition that industrial background logs were augmented with constructed anomaly scenarios.
- Multi-Task Unlearning: [manuscript](https://arxiv.org/html/2605.19042v1). Percentage improvements refer to Unlearning Impact Score (UIS).
- Mask as Memory: [Springer chapter](https://link.springer.com/chapter/10.1007/978-3-032-37667-1_23), including the PruneStream components and the five-task evaluation.
- SEAL: the author's [NTU thesis abstract](https://tdr.lib.ntu.edu.tw/handle/123456789/98825?mode=full) supports the framework description. No thesis-only numerical result is presented as a conference-paper result. [Crossref's publisher-deposited record](https://api.crossref.org/works/10.1109/EdgeCom66327.2025.00030) confirms the paper's DOI and title; the previous DOI, `10.1109/EDGE67615.2025.00026`, returned 404 and was corrected.
- LOOPQ: the user-supplied `41948_LoopQ_Quantization_for_L.pdf` (ICLR 2027 submission). The overview reflects loop-aware scaling, selective transformations, transition adapters, and trajectory-aware calibration. The 67.8% result is an average **relative** improvement over the strongest static baseline for each comparison, not a percentage-point gain. The supplied PDF is not added to the public site, and the arXiv link remains pending.
