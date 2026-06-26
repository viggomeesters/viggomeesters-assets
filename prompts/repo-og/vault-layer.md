# Vault Layer — repo Open Graph prompt

Asset metadata:
- Website: viggomeesters.com
- Source style repo: viggomeesters-assets
- Target GitHub repo: https://github.com/viggomeesters/vault-layer
- Repo slug: vault-layer
- Repo title: Vault Layer
- Repo description: Local-first database and retrieval layer for huge Markdown/Obsidian vaults
- Asset type: GitHub repository Open Graph / README hero image
- Target image path: `assets/repo-og/vault-layer-repo-og.jpg`
- Prompt record path: `assets/repo-og/vault-layer-repo-og.prompt.md`
- Style version: viggomeesters-dark-editorial-code-card-v1
- Creation route: copy this prompt into an image-generation tool such as ChatGPT image generation; save the generated raster as JPEG/PNG/WebP, not SVG.

Style references:
- `STYLE.md`
- `prompts/og-image.md`
- `assets/blog/cli-agents-guide-hero.jpg` as the current generated-raster style anchor
- `viggomeesters-htmls/cli-agents-guide.html` for current article/card feel

Prompt:
```text
Create a 16:9 Open Graph / README hero image for the public GitHub repository `viggomeesters/vault-layer`.

Repository context:
- Owner/site: viggomeesters.com
- Repo: viggomeesters/vault-layer
- Title: Vault Layer
- Description: Local-first database and retrieval layer for huge Markdown/Obsidian vaults
- Asset use: GitHub repository social preview and optional README hero
- Output format: generated raster image, preferably 1280x720 JPG or PNG; do not create SVG.
- Style version: viggomeesters-dark-editorial-code-card-v1

Visual style:
Match viggomeesters.com: proof-first personal technical site; dark static-site portfolio aesthetic; calm editorial code-card composition; readable systems diagramming; subtle aurora/glass accents; precise source-backed labels; no generic SaaS/stock/cyberpunk styling.
Use dark charcoal background (#0c0c0f / #141418), soft off-white typography, muted slate secondary text, fine low-alpha borders, and restrained blue/cyan/purple/green/amber accents.

Core visual motif:
Markdown vault compiled into SQLite/FTS/vector runtime layers.

Composition:
- Large readable title area: `Vault Layer`.
- Small top badge: `github.com/viggomeesters/vault-layer`.
- Center/right technical motif built from 3–5 glass/code cards, grouped cleanly with arrows or thin connector lines.
- Make the source-of-truth / input layer visually distinct from generated/runtime/output cards.
- Keep the image crop-safe for GitHub social previews and README use.

Required readable labels:
- Markdown vault
- SQLite + FTS5
- retrieval layer
- local-first

Negative prompt:
No SVG output, no stock-photo people, no cartoon mascot, no generic cloud clipart, no bright cyberpunk/neon overload, no random node cloud, no messy spaghetti graph, no tiny unreadable paragraphs, no fake brand logos, no private/customer data, no screenshots of real private files.
```

Provenance to save next to the generated image:
```yaml
site: viggomeesters.com
style_repo: viggomeesters-assets
target_repo: viggomeesters/vault-layer
repo_title: Vault Layer
asset_type: repo_open_graph
style_version: viggomeesters-dark-editorial-code-card-v1
template: prompts/og-image.md
references:
  - STYLE.md
  - prompts/og-image.md
  - assets/blog/cli-agents-guide-hero.jpg
  - viggomeesters-htmls/cli-agents-guide.html
generator: ChatGPT image generation or equivalent
creation_route: generated from this copy-paste prompt; save as raster, not SVG
public_safety: reviewed-no-private-data
```
