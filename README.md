# Sona

**Every pixel answers to the register.**

[![Version](https://img.shields.io/badge/version-1.0-1a2340)](https://github.com/abhijitkrm/sona)
[![License](https://img.shields.io/badge/license-MIT-22e2a8)](LICENSE)
[![Tokens](https://img.shields.io/badge/tokens-34-40b3ff)](tokens.json)

## Why

Sona is a design system for landing pages and printable documents: one
token register, three self-contained HTML templates, and a checker that
fails the page when a value drifts outside it.

Sona (सोना) means gold in Hindi. The system keeps surfaces calm and
hierarchy legible: a deep-space canvas, starlight type, a starfield
carries the sky, and pills and 20px cards carry structure.

Inspired by the restraint of [Kami](https://kami.tw93.fun/) — a
different palette, the same discipline.

## Showcase

Every page below is rendered entirely with its own tokens. Serve the
folder and open them, or read the source — the markup is the specimen.

| Page | Mode | What it shows |
|---|---|---|
| `site/index.html` | Dark | The full spec rendered live: color ramps, a type wall, 24 components, a dark/light/print mode specimen |
| `site/index-light.html` | Light | The same showcase on eggshell and paper — both pages toggle dark/light in place |
| `templates/landing-page.html` | Dark | A screen-first product page: fixed nav, starfield hero, stat strip, cards, marquee, pricing, FAQ |
| `templates/landing-page-light.html` | Light | The same page remapped to paper, one sanctioned shadow |
| `templates/one-pager.html` | Print | An eggshell A4 one-pager, solids only, WeasyPrint-ready |

```bash
python3 -m http.server 8000   # then open http://localhost:8000/site/
```

## Use

Copy a template, fill in your content, and restyle through the register
only — a value outside `tokens.json` fails the checker:

```bash
python3 scripts/check_tokens.py
```

Print render:

```bash
weasyprint templates/one-pager.html one-pager.pdf
```

## Design

- **Register.** `tokens.json` is canonical. Every `var()` reference must
  resolve and every hex must be registered; the checker is the guard.
- **Modes.** Dark, light, and print are remaps of the same register, not
  second palettes. The showcase toggles dark/light in place; islands
  (code, starfield demos, the navy CTA band) keep their native canvas.
- **Type.** Space Grotesk carries everything; JetBrains Mono handles
  labels and numbers. The ladder runs 12px to a fluid 96px display step.
- **Form.** Radii are `10 / 20 / 30 / 999px` and nothing else. Depth is
  hairlines; the only sanctioned shadow lives on `--paper` cards.
- **Components.** Two tiers: primitives (pill, link, tabs, field, alert,
  chip, card, code, table, blockquote, list, divider) and the patterns
  they compose into (section head, nav, hero, metrics, stat strip,
  pricing, CTA band, media frame, marquee, flow line, FAQ, footer).
- **Motion.** 300ms inversions, 700ms entrances, a 5s beam on live paths.
  `prefers-reduced-motion` kills all of it.
- **Print.** Eggshell mode flattens alpha to `--print-ink-*` solids with
  `--nebula-navy` as the one chromatic voice; the dark page prints light
  through a media-query remap.

Full spec: [design.md](design.md). Cheatsheet: [CHEATSHEET.md](CHEATSHEET.md).
Diagram theming: [mermaid-theme.json](mermaid-theme.json).

## Layout

```
tokens.json            Canonical color register (all hexes live here)
design.md              Full spec: color, type, spacing, components, motion, print
CHEATSHEET.md          One-page quick reference
mermaid-theme.json     Token -> diagram-theme mapping (dark + print notes)
templates/
  landing-page.html    Dark, screen-first page
  landing-page-light.html  Same page on eggshell
  one-pager.html       Eggshell A4 print template (WeasyPrint-ready)
site/
  index.html           The system's own showcase + spec site (dark)
  index-light.html     The same showcase in light mode
scripts/
  check_tokens.py      Drift guard: var() refs and hexes must be registered
```

## Credits

- Fonts: [Space Grotesk](https://floriankarsten.github.io/space-grotesk/)
  and [JetBrains Mono](https://www.jetbrains.com/lp/mono/), loaded from
  Google Fonts. The stacks keep "The Future" / "The Future Mono" first in
  line if you own the licensed families.
- Visual DNA: [Kami](https://github.com/tw93/kami) by tw93.

## License

[MIT](LICENSE)
