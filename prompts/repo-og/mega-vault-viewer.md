# Mega Vault Viewer — repo Open Graph prompt

Asset metadata:
- Website: viggomeesters.com
- Source style repo: viggomeesters-assets
- Target GitHub repo: https://github.com/viggomeesters/mega-vault-viewer
- Repo slug: mega-vault-viewer
- Repo title: Mega Vault Viewer
- Repo description: Local-first macOS viewer for large mixed-format Markdown knowledge vaults.
- Asset type: GitHub repository Open Graph / README hero image
- Target image path: `assets/repo-og/mega-vault-viewer-repo-og.jpg`
- Prompt record path: `assets/repo-og/mega-vault-viewer-repo-og.prompt.md`
- Style version: viggomeesters-dark-editorial-code-card-v1
- Creation route: copy this prompt into an image-generation tool such as ChatGPT image generation; save the generated raster as JPEG/PNG/WebP, not SVG.

Style references:
- `STYLE.md`
- `prompts/og-image.md`
- `assets/blog/cli-agents-guide-hero.jpg` as the current generated-raster style anchor
- `viggomeesters-htmls/cli-agents-guide.html` for current article/card feel

Prompt:
```text
Create a 16:9 Open Graph / README hero image for the public GitHub repository `viggomeesters/mega-vault-viewer`.

Repository context:
- Owner/site: viggomeesters.com
- Repo: viggomeesters/mega-vault-viewer
- Title: Mega Vault Viewer
- Description: Local-first macOS viewer for large mixed-format Markdown knowledge vaults.
- Asset use: GitHub repository social preview and optional README hero
- Output format: generated raster image, preferably 1280x720 JPG or PNG; do not create SVG.
- Style version: viggomeesters-dark-editorial-code-card-v1

Visual style:
Match viggomeesters.com: proof-first personal technical site; dark static-site portfolio aesthetic; calm editorial code-card composition; readable systems diagramming; subtle aurora/glass accents; precise source-backed labels; no generic SaaS/stock/cyberpunk styling.
Use dark charcoal background (#0c0c0f / #141418), soft off-white typography, muted slate secondary text, fine low-alpha borders, and restrained blue/cyan/purple/green/amber accents.

Core visual motif:
large local knowledge vault rendered as searchable panels.

Composition:
- Large readable title area: `Mega Vault Viewer`.
- Small top badge: `github.com/viggomeesters/mega-vault-viewer`.
- Center/right technical motif built from 3–5 glass/code cards, grouped cleanly with arrows or thin connector lines.
- Make the source-of-truth / input layer visually distinct from generated/runtime/output cards.
- Keep the image crop-safe for GitHub social previews and README use.

Required readable labels:
- large vault
- local search
- viewer
- metadata

Negative prompt:
No SVG output, no stock-photo people, no cartoon mascot, no generic cloud clipart, no bright cyberpunk/neon overload, no random node cloud, no messy spaghetti graph, no tiny unreadable paragraphs, no fake brand logos, no private/customer data, no screenshots of real private files.
```

Provenance to save next to the generated image:
```yaml
site: viggomeesters.com
style_repo: viggomeesters-assets
target_repo: viggomeesters/mega-vault-viewer
repo_title: Mega Vault Viewer
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
