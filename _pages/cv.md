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
  <div class="cv-timeline">
    <div class="cv-entry">
      <div class="cv-entry__date">2021 - Present</div>
      <div class="cv-entry__body">
        <h3>Ph.D. in Communication Engineering</h3>
        <p>Graduate Institute of Communication Engineering, National Taiwan University</p>
        <p>Network Database Laboratory. Supervisor: Prof. Ming-Syan Chen</p>
      </div>
    </div>
    <div class="cv-entry">
      <div class="cv-entry__date">2018 - 2021</div>
      <div class="cv-entry__body">
        <h3>M.S. in Manufacturing Technology</h3>
        <p>Graduate Institute of Manufacturing Technology, National Taipei University of Technology</p>
        <p>Advanced Microsystems and Device Laboratory. Supervisor: Prof. Chih-Cheng Lu</p>
      </div>
    </div>
    <div class="cv-entry">
      <div class="cv-entry__date">2014 - 2018</div>
      <div class="cv-entry__body">
        <h3>B.S. in Mechanical Engineering</h3>
        <p>College of Mechanical and Electrical Engineering, National Taipei University of Technology</p>
      </div>
    </div>
  </div>
</section>

<section class="cv-section">
  <h2>Awards</h2>
  <div class="cv-entry cv-entry--compact">
    <div class="cv-entry__date">2025</div>
    <div class="cv-entry__body">
      <h3>National Taiwan University Wen-Tzu Hsiang Memorial Scholarship</h3>
    </div>
  </div>
</section>

<section class="cv-section">
  <h2>Research Interests</h2>
  <div class="cv-interest-grid">
    <div>
      <h3>Efficient Transformer Inference</h3>
      <p>Early exiting, KV admission, long-context inference, and adaptive computation for generative retrieval and language models.</p>
    </div>
    <div>
      <h3>Model Compression and Quantization</h3>
      <p>Quantization for recursive Transformers and early-exit Vision Transformers, plus LoRA-guided pruning and multi-task compression.</p>
    </div>
    <div>
      <h3>Trustworthy Deployment</h3>
      <p>Multi-task unlearning, secure on-device language models with trusted execution environments, and interpretable medical AI.</p>
    </div>
  </div>
</section>

<section class="cv-section">
  <h2>Skills</h2>
  <div class="skill-cloud">
    <span>Vision Transformers</span>
    <span>Large Language Models</span>
    <span>Graph Neural Networks</span>
    <span>Convolutional Neural Networks</span>
    <span>Network Pruning</span>
    <span>Quantization</span>
    <span>Early Exiting</span>
    <span>LoRA</span>
    <span>On-Device Inference</span>
    <span>Trusted Execution Environments</span>
    <span>CUDA</span>
    <span>PyTorch</span>
    <span>TensorFlow</span>
    <span>JAX</span>
    <span>Python</span>
    <span>C++</span>
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
  <p>Conference Reviewer: CVPR, ICML, IJCAI, ECAI, ECCV, ICLR, NeurIPS, etc.</p>
</section>
