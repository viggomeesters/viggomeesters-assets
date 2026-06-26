# Article Hero Prompt Template

Use for `viggomeesters.com` article hero images and visual header cards.

```text
Create a 16:9 landscape article hero image for viggomeesters.com.

Site context:
- Website: viggomeesters.com
- Consumer repo: viggomeesters.nl static personal site
- Article slug: {{slug}}
- Article title: {{title}}
- Publication date: {{date}}
- Asset use: article hero image and optional Open Graph source
- Style version: viggomeesters-dark-editorial-code-card-v1

Style references:
- Follow STYLE.md in github.com/viggomeesters/viggomeesters-assets, especially the `Explicit viggomeesters.com style` section.
- Primary style: viggomeesters.com as a proof-first personal technical site with a dark static-site portfolio aesthetic.
- Match the visual language of viggomeesters-htmls/ as the canonical current site/article anchor.
- Use inspiration-htmls/ and style-files/ only as secondary layout, palette, typography, and composition inspiration.
- Do not let consulting employer/care organization/design organization/private-source inspiration override the ViggoMeesters style.
- Calm editorial code-card hero, subtle aurora/glass accents, precise readable systems diagram, source-backed labels.

Article thesis:
{{thesis}}

Required readable labels:
{{labels}}

Composition:
{{composition}}

Palette:
{{palette}}

Negative prompt:
No people, no stock-photo office, no server racks, no 3D database cylinders as the main motif, no bright cyberpunk overload, no messy spaghetti graph, no tiny unreadable paragraphs, no corporate SaaS clipart, no logos unless explicitly requested.

Output/provenance:
- Target image path in consuming site: {{target_image_path}}
- Prompt record path: {{prompt_record_path}}
- Save the final prompt, style version, references, and generator/backend metadata if known.
```
