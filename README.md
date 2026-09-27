# Rui Fang — academic website

A lightweight Jekyll website for research, publications, and CV, deployed with GitHub Pages. The active template is maintained in this repository: compact academic layout, white background, blue links, and no JavaScript dependency for navigation. Original Academic Pages / Minimal Mistakes files and their MIT attribution are retained, but unused demo content and legacy assets are excluded from the build.

## Preview and verify

Use Ruby 3.2.2 and Bundler 2.3.5 (also used by CI and Docker):

```sh
gem install bundler -v 2.3.5
bundle install
bundle exec jekyll serve --host 127.0.0.1
```

Open http://127.0.0.1:4000. Restart Jekyll after changing `_config.yml`.

```sh
JEKYLL_ENV=production bundle exec jekyll build
python3 scripts/check_site.py _site
```

The checks validate internal links and fragments, metadata, sitemap XML, demo exclusions, and the currently maintained publication records. External publisher availability is checked separately when updating papers. `Gemfile.lock` is tracked; do not delete it to resolve build failures. Update dependencies intentionally with Bundler.

Alternatively:

```sh
docker build -t rui-academic .
docker run --rm -p 4000:4000 -v "$PWD:/usr/src/app" rui-academic
```

## Update content

- `_pages/about.md`: introduction and research focus.
- `_publications/*.md`: the single data source for publications, selected work, and web CV.
- `_pages/cv.md`: education, awards, skills, and service.
- `_data/publication_sections.yml`: publication grouping and order.
- `_data/navigation.yml`: main navigation.
- `_includes/primary-nav.html`: shared navigation; the homepage combines its only name heading with navigation.
- `_includes/icons/*.svg`: four small inline outlines extracted from the original Academicons and Font Awesome fonts. Icons are decorative alongside visible link text; no icon font download is needed.
- `assets/css/academic.css`: active responsive template, print styles, and color variables.
- `_layouts/{default,home,page,publication}.html` and `_includes/paper*.html`: active layouts and shared paper rendering.
- `_config.yml`: contact details, content update date, build exclusions, and analytics.

Each paper needs `title`, `authors`, `date`, `year`, `category`, `status`, `venue`, `excerpt`, and a unique **local** `permalink`. Put external URLs in `paperurl` or `codeurl`; omit unavailable links. `year` is the displayed publication year; `date` preserves the original record date. Keep existing permalinks when renaming a paper. `selected: 1` (or 2, 3, ...) controls homepage selection and order. For shared first authorship, mark the relevant names with `<sup>*</sup>` and set `equal_contribution: true`; the listing and detail templates display the explanation.

Categories: `conferences`, `manuscripts`, `submissions`, `preprints`.
Statuses: `published`, `accepted`, `under-review`, `preprint`. Accepted papers must not be labeled published, and submissions must not be labeled accepted. Add `citation` for a formatted citation on the detail page. No proceedings DOI or page numbers should be invented for accepted manuscripts.

`files/CV.pdf` is the current downloadable CV (updated September 28, 2026). Its LaTeX source is maintained separately in [CV_Latex](https://github.com/Rui-Fang/CV_Latex), in `rui_fang_cv.tex`. After compiling a new version, copy `rui_fang_cv.pdf` to `files/CV.pdf` and update `pdf_updated` in `_pages/cv.md`. LaTeX sources and build artifacts are kept out of this website repository. All current paper records are reflected automatically in the web CV.

Set `math: true` on a page only if it needs MathJax. Analytics runs only with `JEKYLL_ENV=production`. The site works without JavaScript.

## Publishing

The check workflow builds and validates pushes and pull requests; it does not change deployment settings. Keep the repository's existing GitHub Pages deployment. Verify the actual deployment settings before switching to an Actions deployment workflow.

## Sources and maintenance

See `docs/publication-audit.md` for the September 2026 Scholar reconciliation. When adding a paper, update the expected publication count and any status expectations in `scripts/check_site.py`. Template assets use local system fonts and preserve existing publication URLs.

Original template: [Academic Pages](https://github.com/academicpages/academicpages.github.io), derived from [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes). See `LICENSE` for retained attribution.
