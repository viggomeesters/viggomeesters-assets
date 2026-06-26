# Contributing

This repository is a public-safe style and prompt system for `viggomeesters.com`.

## Contribution rules

1. Keep all content public-safe.
2. Add provenance for every copied or generated asset.
3. Prefer references and summaries over wholesale private context.
4. Do not add secrets, cookies, tokens, private screenshots, customer files, or proprietary data.
5. Keep prompts aligned with `STYLE.md` and the templates in `prompts/`.

## Adding a new asset

For a new article hero or Open Graph image:

1. Add or update the prompt record in `examples/` or next to the consuming site asset.
2. Reference `STYLE.md` and at least one existing public-safe artifact.
3. Add final public images under `assets/references/` only when they are safe to reuse as style anchors.
4. Update `indexes/design-artifacts.md` when adding copied HTML/CSS references.

## Validation

Run before committing:

```bash
git diff --check
python3 - <<'PY'
from pathlib import Path
for path in Path('.').rglob('*'):
    if path.is_file() and path.name.lower() in {'.env', 'id_rsa', 'id_ed25519'}:
        raise SystemExit(f'forbidden file: {path}')
print('basic public-safety file check passed')
PY
```
