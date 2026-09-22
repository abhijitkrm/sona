# Cheatsheet

One-line aesthetic: **deep-space canvas, starlight type, a starfield
carries the sky, pills and 20px cards carry structure.**

## Tokens (full list in tokens.json)

```
SURFACES   --void #000  --surface-1 #181818  --surface-2 #1e1f20
           --surface-3 #212121  --edge #37383a
TEXT       --ink #fff  --ink-80  --ink-60  --ink-50  --ink-40  --ink-30
           (white at 100/80/60/50/40/30%)
STROKES    --stroke-50  --stroke-20  --stroke-13   FILLS  --fill-20/10/5
LIGHT      --eggshell #f1f4f4  --paper #fff  --edge-light #e1e1e1
           --eggshell-dark #cfdadc  --gray-medium #bbb  --gray-mid #808080
           --gray-dark #666 (labels and small text on light)
ACCENTS    --mint #22e2a8  --cyan #40b3ff
NEBULA HUES  --nebula-navy #1a2340 (print accent)  --nebula-pink #f2a7b8
             --nebula-violet #c98bd8 (code syntax)  --nebula-peach #f6d6c2
           (palette colors only - no gradient treatment anywhere)
```

## Type

- Sans: `"Space Grotesk", "The Future", system stack` (The Future if licensed)
- Mono: `"JetBrains Mono", "The Future Mono", "Space Mono", ui-monospace`
- Ladder: 12 / 13 / 14 / 16 / 18 / 20 / 24 / 32 / 36 px; display is a fluid clamp(56px, 7vw, 96px). Never between steps.
- Weights: headings 500, body 400, mono labels 500. No thin, no black-900.
- Line-height: display 1.13-1.22, headings 1.25-1.35, body 1.5, labels 1.6.
- Tracking: prose 0.02em, nav/buttons 0.32px, labels 0.48px uppercase.

## Layout

- Container 1440px, sides ~100px desktop / ~30px phone.
- Section gaps: 96-108px desktop, 72 tablet, 56 phone. Scale the ladder, not one gap.
- Radius: 10 / **20 (cards)** / 30 / 999 (pills). Nothing else.
- Breakpoints: 640 / 1024 / 1280.

## Components

- Pill button: 999px, 34/42px tall, hover = fill/fg inversion, 300ms.
- Link: accent text, hairline underline at rest, accent underline on hover, focus ring.
- Tabs: pill container + 2px pad, mono segments, active inverts. The hero toggle is one.
- Field: `--surface-2`/`--paper` fill, `--stroke-13`/`--edge-light` rim, 10px. Focus = accent rim.
- Checkbox/radio: `accent-color` = mode accent.
- Alert: hairline band + 7px dot. Mint = ok, pink = error. No fills.
- Card: `--surface-2` + `--stroke-13` rim + 20px + 24-28px padding. Flat.
- Chip: mono 12px uppercase, `--fill-10` + `--stroke-13`, pill radius.
- Blockquote: 1px left rule + mono cite. No quote glyph.
- Marker list: `+` mint / `-` dim for included/excluded.
- Divider: hairline only - `--stroke-13` default, `--stroke-20` between chapters.
- Stat strip: 4-col grid, 32-36px number + mono label, `--stroke-13` separators. Never boxed.
- Pricing: 3 cards max, one `--stroke-50` rim + `--mint` plan name for the highlight, mint check list.
- FAQ: native `<details>`, hairline rows, mono `+` rotates 45deg open.
- Media frame: 30px radius + hairline rim; captions outside.
- CTA band: flat `--nebula-navy`, centered, one eggshell pill. Always navy.
- Nav / footer: wordmark + mono links + pill CTA / mark + links + legal on one baseline.
- Product mock: pure-CSS window, `--surface-1` frame, three-dot bar, real tokens only.
- Table: hairlines only (`--stroke-20` header, `--stroke-13` rows), mono uppercase header.
- Code: `--surface-1` block, mono 13.5px. Syntax = cyan keyword, mint string, pink number, violet fn.

## Depth / motion

- Flat everywhere. Shadow only on `--paper` cards: `0 2px 10px rgba(30,31,32,.10)`.
- Entrance: fade + translateY(32px), 700ms ease-out. Not on hero title.
- Gradient-flow beam on hairlines: white, 5s, marks live paths only.
- Marquee: linear infinite, pauses on hover. `prefers-reduced-motion` kills all.

## Hard rules

- No gradient treatments. The starfield is the only sky, and it lives in the hero only.
- Text on dark = alpha ladder only, no gray hexes; `--ink-50` is the text floor. On light = `#000`/`#212121`/`#666666` labels.
- Light screen = eggshell mode too: `--paper` cards + one shadow, navy accent, no mint/cyan text.
- Print = eggshell mode, alpha flattens to `--print-ink-*`, accent `--nebula-navy`.
- New color = register in tokens.json first. `python3 scripts/check_tokens.py` must pass.
