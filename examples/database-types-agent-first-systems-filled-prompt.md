# Filled Prompt: Database Types for Agent-First Systems

Asset metadata:

- Website: `viggomeesters.com`
- Consumer repo: `viggomeesters.nl`
- Source style repo: `viggomeesters-assets`
- Page slug: `database-types-agent-first-systems`
- Article title: `Database Types for Agent-First Systems`
- Publication date: `24 Jun 2026`
- Asset type: `article hero / Open Graph source`
- Target image path: `assets/blog/database-types-agent-first-systems-hero.jpg`
- Prompt record path: `assets/blog/database-types-agent-first-systems-hero.prompt.md`
- Style version: `viggomeesters-dark-editorial-code-card-v1`

Style references:

- `STYLE.md`
- `prompts/article-hero.md`
- `viggomeesters-htmls/database-types-agent-first-systems.html`
- `viggomeesters-htmls/jsonl-agent-first-data-structures.html`
- `inspiration-htmls/beautiful-html-templates/soft-editorial.html`
- `inspiration-htmls/beautiful-html-templates/cobalt-grid.html`
- `style-files/brand-experiments/neo-whimsical-style.css` for soft editorial alternatives only

## Copy-pasteable prompt

```text
Create a 16:9 landscape article hero image for viggomeesters.com.

Site context:
- Website: viggomeesters.com
- Consumer repo: viggomeesters.nl static personal site
- Source style repo: viggomeesters-assets
- Page slug: database-types-agent-first-systems
- Article title: Database Types for Agent-First Systems
- Publication date: 24 Jun 2026
- Asset use: article hero image and optional Open Graph source
- Style version: viggomeesters-dark-editorial-code-card-v1

Style references:
- Follow STYLE.md from github.com/viggomeesters/viggomeesters-assets.
- Match the current article feel from viggomeesters-htmls/database-types-agent-first-systems.html and viggomeesters-htmls/jsonl-agent-first-data-structures.html.
- Use inspiration-htmls/beautiful-html-templates/soft-editorial.html for calm editorial spacing.
- Use inspiration-htmls/beautiful-html-templates/cobalt-grid.html for controlled grid composition only.
- Use style-files/brand-experiments/neo-whimsical-style.css only as a soft alternative cue for rounded cards and warmth; do not copy CSS.

Core thesis:
JSONL is the canonical, reviewable source of truth. Databases and indexes are generated runtime artifacts chosen by job: SQLite for local runtime, FTS5 for exact keyword search, sqlite-vec for local semantic search, DuckDB for analytics, Postgres/Turso for application state, and vector DBs for service-scale retrieval.

Composition:
Dark charcoal editorial code-card hero. Left side shows stacked JSONL record cards labelled “records/*.jsonl” and “canonical records”. Center shows a compact build/compile node labelled “schema + evals”. Right side shows generated runtime cards labelled “SQLite”, “FTS5”, “sqlite-vec”, “DuckDB”, and “Postgres / Vector DB”. Use thin arrows from canonical records to generated runtime. Make the hierarchy obvious: canonical records on the left, generated runtime surfaces on the right.

Required readable labels:
- viggomeesters.com
- Database Types for Agent-First Systems
- 24 Jun 2026
- JSONL
- canonical records
- generated runtime
- SQLite
- FTS5
- sqlite-vec
- DuckDB
- Postgres

Palette:
Near-black charcoal background (#0c0c0f / #141418), soft off-white text, muted slate secondary text, restrained aurora glow. Use blue/cyan for JSONL, green for SQLite/FTS5, purple for sqlite-vec/vector, amber for DuckDB/analytics, orange for Postgres/service state.

Negative prompt:
No people, no stock-photo office, no server racks, no 3D database cylinders as the main motif, no bright cyberpunk overload, no messy spaghetti graph, no tiny unreadable paragraphs, no corporate SaaS clipart, no brand logos, no fake product UI screenshot.

Output/provenance:
- Target image path in consuming site: assets/blog/database-types-agent-first-systems-hero.jpg
- Prompt record path: assets/blog/database-types-agent-first-systems-hero.prompt.md
- Save the final prompt, style version, references, generator/backend metadata if known, and public-safety note.
```

## Provenance frontmatter to save beside the image

```yaml
site: viggomeesters.com
consumer_repo: viggomeesters.nl
style_repo: viggomeesters-assets
slug: database-types-agent-first-systems
title: Database Types for Agent-First Systems
date: 2026-06-24
asset_type: article_hero
style_version: viggomeesters-dark-editorial-code-card-v1
template: prompts/article-hero.md
references:
  - STYLE.md
  - prompts/article-hero.md
  - viggomeesters-htmls/database-types-agent-first-systems.html
  - viggomeesters-htmls/jsonl-agent-first-data-structures.html
  - inspiration-htmls/beautiful-html-templates/soft-editorial.html
  - inspiration-htmls/beautiful-html-templates/cobalt-grid.html
generator: unknown
public_safety: reviewed-no-private-data
notes: Reisplanner or another generator may consume this prompt as an execution workflow, but the style source remains viggomeesters-assets.
```
