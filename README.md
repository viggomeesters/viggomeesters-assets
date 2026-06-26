# ViggoMeesters Assets

Public-safe visual style pack for `viggomeesters.com`: rendered HTML references, prompt templates, generated/static assets, and provenance records.

**Browse the gallery:** https://viggomeesters.github.io/viggomeesters-assets/

![ViggoMeesters Assets hero](assets/hero.svg)

## What this is

Use this repo when creating a hero image, Open Graph image, article visual, or style-consistent static asset for `viggomeesters.com`.

## Usage

Start here:

1. `STYLE.md` — canonical ViggoMeesters visual style.
2. `index.html` — curated rendered gallery with top picks first.
3. `prompts/` — reusable prompt templates.
4. `viggomeesters-htmls/` — current public-site/article style anchors.
5. `inspiration-htmls/` — secondary public-safe layout, palette, and composition inspiration.
6. `indexes/public-safety-audit.md` — one-row-per-file public-safety/render audit.

Default generator direction:

```text
Match viggomeesters.com: a proof-first personal technical site with a dark static-site portfolio aesthetic, calm editorial code-card composition, readable systems diagrams, subtle aurora/glass accents, precise source-backed labels, and no generic SaaS/stock/cyberpunk styling.
```

## Asset contract

For article assets, save the image and prompt/provenance together in the consuming site repo:

```text
assets/blog/<slug>-hero.jpg
assets/blog/<slug>-hero.prompt.md
```

Prompt records should include site, consumer repo, slug/title/date, asset type, creation route, style version, template, references, final prompt, and generator/backend if known.

## Public-safety boundary

Allowed: public website visual language, public-safe generated images, reusable prompt templates, anonymized style examples, and provenance notes.

Forbidden: private knowledge-base content, customer/internal names, tickets, screenshots, internal URLs, secrets, credentials, proprietary SAP/customer documentation, hidden agent instructions, and private runbooks.

## Installation

No package installation is required. Clone the repository or browse the rendered gallery directly:

```bash
git clone https://github.com/viggomeesters/viggomeesters-assets.git
cd viggomeesters-assets
```

## Development

No GitHub Actions by design. Run checks locally before publishing changes:

```bash
git diff --check
scripts/public_safety_audit.py --write
scripts/public_safety_audit.py
# Optional local-only private term scan; keep actual private terms out of the repo.
PUBLIC_SAFETY_EXTRA_REGEX='<semicolon-separated-private-regexes>' scripts/public_safety_audit.py
```

## Consumer workflows

- `viggomeesters.nl` consumes final hero/OG assets.
- `viggo-agent-skills` owns the `viggomeesters-asset-prompt` skill.
- A generator workflow can read this repo as a style/reference pack; the generator is the execution route, not the style source.

## License

This repository is released under the MIT License. See `LICENSE` for the full text and attribution terms.
