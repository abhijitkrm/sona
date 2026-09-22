# Sona Design System

A design system for landing pages and printable documents:
self-contained HTML templates, a canonical token register, and a full
spec. Dark-first on screen; eggshell covers light mode and print.

**Aesthetic**: deep-space canvas, starlight type, a starfield carries
the sky, pills and 20px cards carry structure.

## Layout

```
tokens.json            Canonical color register (all hexes live here)
design.md              Full spec: color, type, spacing, components, motion, print
CHEATSHEET.md          One-page quick reference
mermaid-theme.json     Token -> diagram-theme mapping (dark + print notes)
templates/
  landing-page.html    Dark, screen-first page (nav, hero, cards, marquee, pricing, FAQ)
  landing-page-light.html  Same page on eggshell (light mode variant)
  one-pager.html       Eggshell A4 print template (WeasyPrint-ready)
site/
  index.html           The system's own showcase + spec site (dark),
                       rendered entirely with its own tokens
  index-light.html     The same showcase in light mode
                       (both pages toggle dark/light in place)
scripts/
  check_tokens.py      Drift guard: var() refs and hexes must be registered
```

## Use

Open `templates/landing-page.html` in a browser, or serve the folder:

```bash
python3 -m http.server 8000    # then open http://localhost:8000/templates/landing-page.html
```

Render the print template:

```bash
weasyprint templates/one-pager.html one-pager.pdf
```

Verify token integrity after any style edit:

```bash
python3 scripts/check_tokens.py
```

## Rules that bite

- Text hierarchy on dark is the `--ink-*` alpha ladder only; no gray hexes.
- No gradient treatments: the starfield (hero only) is the only sky
  texture; closing/cover bands use flat `--nebula-navy`.
- Radii are `10 / 20 / 30 / 999px` only.
- Print templates flatten alpha to `--print-ink-*` solids; no 8-digit hex
  ships to WeasyPrint.
- New color -> register in `tokens.json` first, then use `var(--*)`.

## Credits

- Fonts: Space Grotesk and JetBrains Mono (free substitutes for the
  commercial "The Future" / "The Future Mono"; swap in the licensed
  families first in each stack if owned).
