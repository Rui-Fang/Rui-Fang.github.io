---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* Ph.D. in Communication Engineering, National Taiwan University, 2021 - Present
  * Network Database Laboratory
  * Supervisor: Ming-Syan Chen

* M.S. in Manufacturing Technology, National Taipei University of Technology, 2018 - 2021
  * Advanced Microsystems and Device Laboratory
  * Supervisor: Chih-Cheng Lu

* B.S. in Mechanical Engineering, National Taipei University of Technology, 2014 - 2018

Research Interests
======
* Efficient Deep Learning for Transformers (2024–Present)
  * Dynamic LLM inference (BiLEE, ECAI 2024)
  * Pruning Vision Transformers with LoRA-guided importance consensus (LoGIC, AAAI 2026)
  * KV-cache compression for long-context inference

* Few-Shot Learning under Distribution Shifts (2023–2024)
  * Dual alignment and optimal transport-based feature calibration for robust few-shot adaptation (DuAL, NeurIPS 2025)

* Interpretable ECG Diagnosis (2019–2021)
  * Interpretable 3-D ECG deep models for myocardial infarction detection (CMPB 2022)
  
Skills
======
* Deep Learning & Neural Networks
  * Vision Transformers (ViT)
  * Large Language Models (LLMs)
  * Graph Neural Networks
  * Convolutional Neural Networks (CNNs)

* Model Optimization
  * Network Pruning
  * Knowledge Distillation
  * Quantization
  * LoRA and Parameter Efficient Fine-tuning

* Signal Processing
  * ECG Analysis
  * Biomedical Signal Processing

* Programming Languages
  * Python, C++, CUDA
  * PyTorch, TensorFlow, JAX

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

Professional Activity
======
* Conference Reviewer: CVPR, ICML, IJCAI, ECAI, ECCV, etc.
