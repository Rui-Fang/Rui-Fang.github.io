---
layout: home
permalink: /
title: Rui Fang
description: Ph.D. candidate at National Taiwan University researching efficient Transformer inference, quantization, and model compression.
redirect_from:
  - /about/
  - /about.html
---
<section class="about" aria-labelledby="about-heading">
  <header class="about-identity">
    <p class="affiliation"><span class="academic-role">Ph.D. Candidate</span><br>Graduate Institute of<br class="desktop-break"> Communication Engineering<br>National Taiwan University</p>
    <div class="profile-links">
      <a href="{{ site.author.googlescholar }}">{% include icons/scholar.svg %}<span>Google Scholar</span></a>
      <a href="https://github.com/{{ site.author.github }}">{% include icons/github.svg %}<span>GitHub</span></a>
      <a href="{{ site.author.orcid }}">{% include icons/orcid.svg %}<span>ORCID</span></a>
      <a href="{{ '/cv/' | relative_url }}">{% include icons/cv.svg %}<span>CV</span></a>
    </div>
  </header>
  <div class="about-bio">
    <p>I am a Ph.D. candidate at National Taiwan University, advised by Prof. Ming-Syan Chen in the Network Database Laboratory. Before joining NTU, I received my M.S. and B.S. degrees from National Taipei University of Technology.</p>
    <p>My research focuses on efficient inference and model compression for Transformers, including early exiting, quantization, pruning, and KV-cache management. I also work on multi-task learning and unlearning.</p>
    <p class="email"><a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a></p>
  </div>
</section>
