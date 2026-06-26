# 11mhz MCP — repo Open Graph prompt

Asset metadata:
- Website: viggomeesters.com
- Source style repo: viggomeesters-assets (`https://github.com/viggomeesters/viggomeesters-assets`)
- Target GitHub repo: https://github.com/viggomeesters/11mhz-mcp
- Repo slug: 11mhz-mcp
- Repo title: 11mhz MCP
- Repo description: MCP server for the 11MHz API
- Asset type: GitHub repository Open Graph / README hero image
- Target image path: `assets/repo-og/11mhz-mcp-repo-og.jpg`
- Prompt record path: `assets/repo-og/11mhz-mcp-repo-og.prompt.md`
- Style version: viggomeesters-dark-editorial-code-card-v1
- Creation route: copy this prompt into an image-generation tool such as ChatGPT image generation; save the generated raster as JPEG/PNG/WebP, not SVG.

Style references:
- `https://github.com/viggomeesters/viggomeesters-assets` as the canonical style/reference repo
- `STYLE.md` from viggomeesters-assets
- `prompts/og-image.md` from viggomeesters-assets
- `assets/blog/cli-agents-guide-hero.jpg` from viggomeesters-assets as the current generated-raster style anchor
- `viggomeesters-htmls/cli-agents-guide.html` from viggomeesters-assets for current article/card feel

Prompt:
```text
Create a 16:9 Open Graph / README hero image for the public GitHub repository `viggomeesters/11mhz-mcp`.

Repository context:
- Owner/site: viggomeesters.com
- Repo: viggomeesters/11mhz-mcp
- Title: 11mhz MCP
- Description: MCP server for the 11MHz API
- Asset use: GitHub repository social preview and optional README hero
- Output format: generated raster image, preferably 1280x720 JPG or PNG; do not create SVG.
- Style version: viggomeesters-dark-editorial-code-card-v1

Visual style:
Use the public viggomeesters-assets repo as the style pack: https://github.com/viggomeesters/viggomeesters-assets. Match viggomeesters.com: proof-first personal technical site; dark static-site portfolio aesthetic; calm editorial code-card composition; readable systems diagramming; subtle aurora/glass accents; precise source-backed labels; no generic SaaS/stock/cyberpunk styling.
Use dark charcoal background (#0c0c0f / #141418), soft off-white typography, muted slate secondary text, fine low-alpha borders, and restrained blue/cyan/purple/green/amber accents.

Core visual motif:
MCP server bridge between API tools and agent cards.

Composition:
- Large readable title area: `11mhz MCP`.
- Small top badge: `github.com/viggomeesters/11mhz-mcp`.
- Center/right technical motif built from 3–5 glass/code cards, grouped cleanly with arrows or thin connector lines.
- Make the source-of-truth / input layer visually distinct from generated/runtime/output cards.
- Keep the image crop-safe for GitHub social previews and README use.

Required readable labels:
- MCP server
- API bridge
- agent tools
- typed calls

Negative prompt:
No SVG output, no stock-photo people, no cartoon mascot, no generic cloud clipart, no bright cyberpunk/neon overload, no random node cloud, no messy spaghetti graph, no tiny unreadable paragraphs, no fake brand logos, no private/customer data, no screenshots of real private files.
```

Provenance to save next to the generated image:
```yaml
site: viggomeesters.com
style_repo: https://github.com/viggomeesters/viggomeesters-assets
target_repo: viggomeesters/11mhz-mcp
repo_title: 11mhz MCP
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
