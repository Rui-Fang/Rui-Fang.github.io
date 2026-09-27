#!/usr/bin/env python3
"""Check generated pages, internal links, SEO, and publication invariants offline."""
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
from xml.etree import ElementTree

root = Path(sys.argv[1] if len(sys.argv) > 1 else '_site').resolve()
origin = 'https://rui-fang.github.io'
errors = []

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links, self.ids, self.meta, self.tags = [], set(), {}, []
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.tags.append(tag)
        if 'id' in a:
            if a['id'] in self.ids:
                errors.append('Duplicate id: ' + a['id'])
            self.ids.add(a['id'])
        if tag == 'meta':
            self.meta[a.get('name', a.get('property', ''))] = a.get('content', '')
        for key in ('href', 'src'):
            if a.get(key): self.links.append(a[key])

pages = {p: Page(p.read_text()) for p in root.rglob('*.html')}
assert pages, 'Build the site before running this check.'
for path, page in pages.items():
    text = path.read_text()
    rel = path.relative_to(root).as_posix()
    redirect = 'http-equiv="refresh"' in text.lower()
    if not redirect:
        for key in ('description', 'og:description', 'og:image', 'twitter:card'):
            if not page.meta.get(key): errors.append(f'{rel}: missing {key}')
        if page.tags.count('h1') != 1: errors.append(f'{rel}: expected one h1')
        if page.tags.count('main') != 1: errors.append(f'{rel}: expected one main')
        for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, re.S):
            try: json.loads(block)
            except ValueError: errors.append(f'{rel}: invalid structured data')
    for bad in ('[paper-id]', '/https:', 'Future Blog Post', 'MathJax-script', 'polyfill.min.js'):
        if bad in text: errors.append(f'{rel}: unwanted content {bad}')
    for href in page.links + [page.meta.get('og:image', '')]:
        if not href: continue
        url = urlsplit(urljoin(origin + '/' + rel, href))
        if url.scheme not in ('http', 'https') or url.netloc != urlsplit(origin).netloc: continue
        target = root / unquote(url.path).lstrip('/')
        if target.is_dir(): target = target / 'index.html'
        if not target.is_file():
            errors.append(f'{rel}: broken local link {href}')
        elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
            errors.append(f'{rel}: missing fragment {href}')

for forbidden in ('posts', 'talks', 'teaching', 'portfolio', 'markdown', 'talkmap', 'docs', 'scripts', 'node_modules'):
    if (root / forbidden).exists(): errors.append('Unwanted output: ' + forbidden)
ElementTree.parse(root / 'sitemap.xml')
publications = list((root / 'publication').glob('*/index.html'))
if len(publications) != 12: errors.append(f'Expected 12 publication pages; found {len(publications)}')
for slug, venue in [('2026-amortized-precision-quantization','NeurIPS 2026'), ('2025-kv-admission','EMNLP 2026'), ('2026-hsmlog','ISSRE 2026')]:
    text = (root / 'publication' / slug / 'index.html').read_text()
    if venue not in text or '>Accepted<' not in text: errors.append(f'{slug}: acceptance missing')
loopq = (root / 'publication/2026-loopq/index.html').read_text()
for required in ('LOOPQ: QUANTIZATION FOR LOOPED LANGUAGE MODELS','ICLR 2027','Under review'):
    if required not in loopq: errors.append('LOOPQ missing ' + required)
if '2605.16343' in loopq: errors.append('LOOPQ still links to old arXiv version')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f'PASS: {len(pages)} HTML pages, {len(publications)} publications, local links, metadata, sitemap, and publication status.')
