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
  * Supervisor: Prof. Ming-Syan Chen

* M.S. in Manufacturing Technology, National Taipei University of Technology, 2018 - 2021
  * Advanced Microsystems and Device Laboratory
  * Supervisor: Prof. Chih-Cheng Lu

* B.S. in Mechanical Engineering, National Taipei University of Technology, 2014 - 2018

Research Interests
======
* Efficient Transformer inference
  * Early exiting, KV admission, and long-context inference
  * Adaptive computation for generative retrieval and language models

* Model compression and quantization
  * Quantization for recursive Transformers and early-exit Vision Transformers
  * LoRA-guided pruning and multi-task compression

* Trustworthy and deployable machine learning
  * Multi-task unlearning
  * Secure on-device language models with trusted execution environments
  * Interpretable medical AI with 3-D ECG representations

Skills
======
* Deep Learning
  * Vision Transformers
  * Large Language Models
  * Graph Neural Networks
  * Convolutional Neural Networks

* Model Optimization
  * Network pruning
  * Quantization
  * Early exiting
  * LoRA and parameter-efficient fine-tuning

* Systems and Deployment
  * On-device inference
  * Trusted execution environments
  * CUDA and GPU programming

* Programming
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
