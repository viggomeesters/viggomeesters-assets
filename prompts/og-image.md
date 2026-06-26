# Open Graph Image Prompt Template

Use for social preview images where crop safety and title readability matter more than diagram detail.

```text
Create a 16:9 Open Graph image for viggomeesters.com.

Site context:
- Website: viggomeesters.com
- Consumer repo: viggomeesters.nl static personal site
- Page slug: {{slug}}
- Page title: {{title}}
- Publication date: {{date}}
- Asset use: Open Graph / social card
- Style version: viggomeesters-dark-editorial-code-card-v1

Visual direction:
- Dark charcoal background with subtle aurora glow.
- Large readable title, safe within center crop.
- Small badge: viggomeesters.com · {{date}}
- 1 compact visual motif only: {{motif}}
- Use glass/code-card details sparingly.

Required text:
{{required_text}}

Style constraints:
- Follow STYLE.md in github.com/viggomeesters/viggomeesters-assets, especially the `Explicit viggomeesters.com style` section.
- Match viggomeesters.com: proof-first personal technical site, dark static-site portfolio aesthetic, calm editorial code-card composition, readable systems diagramming.
- Use restrained accent colors from the ViggoMeesters palette.
- Do not let consulting employer/care organization/design organization/private-source inspiration override the ViggoMeesters style.
- Do not use logos, stock people, generic cloud clipart, generic SaaS gloss, cyberpunk overload, or crowded diagrams.

Output/provenance:
- Target image path in consuming site: {{target_image_path}}
- Prompt record path: {{prompt_record_path}}
```
