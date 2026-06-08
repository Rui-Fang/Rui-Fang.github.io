---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

<section class="cv-section">
  <h2>Education</h2>
  <div class="cv-item">
    <div class="cv-item__main">
      <h3>National Taiwan University, Graduate Institute of Communication Engineering</h3>
      <p>Ph.D. at Network Database Laboratory. Supervisor: Prof. Ming-Syan Chen</p>
    </div>
    <div class="cv-item__date">2021 - Present</div>
  </div>
  <div class="cv-item">
    <div class="cv-item__main">
      <h3>National Taipei University of Technology, Graduate Institute of Manufacturing Technology</h3>
      <p>M.S. at Advanced Microsystems and Device Laboratory. Supervisor: Prof. Chih-Cheng Lu</p>
    </div>
    <div class="cv-item__date">2018 - 2021</div>
  </div>
  <div class="cv-item">
    <div class="cv-item__main">
      <h3>National Taipei University of Technology, College of Mechanical and Electrical Engineering</h3>
      <p>B.S. in Mechanical Engineering</p>
    </div>
    <div class="cv-item__date">2014 - 2018</div>
  </div>
</section>

<section class="cv-section">
  <h2>Awards</h2>
  <ul class="cv-simple-list">
    <li>2025 National Taiwan University Wen-Tzu Hsiang Memorial Scholarship</li>
  </ul>
</section>

<section class="cv-section">
  <h2>Research Interests</h2>
  <ul class="cv-simple-list">
    <li><strong>Efficient Transformer inference:</strong> early exiting, KV admission, long-context inference, and adaptive computation for generative retrieval and language models.</li>
    <li><strong>Model compression and quantization:</strong> quantization for recursive Transformers and early-exit Vision Transformers, LoRA-guided pruning, and multi-task compression.</li>
    <li><strong>Trustworthy deployment:</strong> multi-task unlearning, secure on-device language models with trusted execution environments, and interpretable medical AI.</li>
  </ul>
</section>

<section class="cv-section">
  <h2>Skills</h2>
  <div class="cv-skill-grid">
    <div>
      <h3>Deep Learning</h3>
      <p>Vision Transformers, Large Language Models, Graph Neural Networks, Convolutional Neural Networks</p>
    </div>
    <div>
      <h3>Model Optimization</h3>
      <p>Network pruning, quantization, early exiting, LoRA, parameter-efficient fine-tuning</p>
    </div>
    <div>
      <h3>Systems and Deployment</h3>
      <p>On-device inference, trusted execution environments, CUDA and GPU programming</p>
    </div>
    <div>
      <h3>Programming</h3>
      <p>Python, C++, CUDA, PyTorch, TensorFlow, JAX</p>
    </div>
  </div>
</section>

<section class="cv-section">
  <h2>Publications</h2>
  <ul class="cv-publications">
    {% for post in site.publications reversed %}
      {% include archive-single-cv.html %}
    {% endfor %}
  </ul>
</section>

<section class="cv-section">
  <h2>Professional Activity</h2>
  <ul class="cv-simple-list">
    <li>Conference Reviewer: CVPR, ICML, IJCAI, ECAI, ECCV, ICLR, NeurIPS, etc.</li>
  </ul>
</section>
