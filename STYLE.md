# ViggoMeesters Visual Style

Style version: `viggomeesters-dark-editorial-code-card-v1`

## Core feel

Calm technical editorial assets for `viggomeesters.com`.

The image should feel like a static-site article hero or README/repo card: dark, precise, system-oriented, and not over-produced.

## Explicit viggomeesters.com style

Use this section as the primary style anchor for every ChatGPT/image-generator prompt.

`viggomeesters.com` should look like a **proof-first personal technical site**: editorial, restrained, dark, source-backed, and built around readable systems thinking rather than marketing gloss.

Mandatory cues:

- Dark portfolio/static-site aesthetic: charcoal page, soft off-white text, muted slate secondary text.
- Editorial code-card layout: article/repo cards, file-path labels, tiny terminal/schema hints, subtle grid structure.
- Proof-first composition: visual hierarchy should make the thesis, source-of-truth, and generated/runtime artifacts obvious.
- Calm technical diagramming: few strong grouped cards, clean arrows, compact labels, no random node cloud.
- Personal-site polish: quiet confidence, not enterprise SaaS, not agency landing page, not stock/AI influencer style.
- Static HTML feel: crisp typography, content-first layout, no fake app dashboard unless the article is actually about a dashboard.

Do **not** let external, private-source-derived, external, or local example source inspiration override this. Only public-safe, anonymized examples may be used as secondary layout/composition inspiration. The canonical style is always:

```text
viggomeesters.com → viggomeesters.nl public site HTML → STYLE.md → prompts/examples
```

## Visual rules

- Dark charcoal base: `#0c0c0f` / `#141418`.
- Soft off-white text, muted slate secondary text.
- Restrained aurora/glow background, never loud cyberpunk.
- Glass/code cards with fine low-alpha borders.
- Monospace labels for system parts and file paths.
- Publication date visible on article hero assets.
- Use the article's real words, not generic placeholder labels.
- Visualize the system concept, not a literal metaphor.

## Accent palette

- JSONL / canonical records: blue/cyan.
- SQLite / FTS / local runtime: green.
- vector / sqlite-vec / semantic layer: purple.
- DuckDB / analytics: amber.
- Postgres / service/runtime state: orange.
- Risks/warnings: restrained red/orange only when relevant.

## Composition defaults

Article hero / OG assets:

- 16:9 landscape.
- Top-left or top-edge publication badge.
- One clear title area.
- Central diagram or code-card composition.
- Small number of readable labels.
- Good crop safety for social previews.

System diagrams:

- Left-to-right or top-to-bottom data flow.
- Source of truth visually distinct from generated artifacts.
- Avoid spaghetti graphs.
- Use arrows and grouping cards, not random node clouds.

## Negative constraints

Avoid:

- stock-photo people or office scenes;
- cartoon mascots;
- generic cloud clipart;
- database cylinder clichés as the main motif;
- messy node-network diagrams;
- bright cyberpunk/neon overload;
- tiny unreadable paragraphs;
- fake UI screenshots;
- brand logos unless explicitly required and legally safe.

## Consistency contract

Future prompts should reference this style version and at least one public-safe reference asset or example prompt in this repo. If a new image establishes a better pattern, add it to `assets/references/` with provenance before relying on it as a style anchor.
