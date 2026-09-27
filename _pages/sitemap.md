---
layout: page
title: Sitemap
permalink: /sitemap/
---

- [About]({{ '/' | relative_url }})
- [Publications]({{ '/publications/' | relative_url }})
- [CV]({{ '/cv/' | relative_url }})
- [XML sitemap]({{ '/sitemap.xml' | relative_url }})

## Publication pages

{% assign papers = site.publications | sort: 'date' | reverse %}
{% for post in papers %}
- [{{ post.title }}]({{ post.url | relative_url }})
{% endfor %}
