# Design System

A dark-first design system. Screen-first by default; the light (eggshell)
mode covers print and light sections.

## Principles

The aesthetic compresses into one sentence: **deep-space canvas, starlight
type, a starfield carries the sky, pills and 20px cards carry structure**.

This is not a UI framework. It is a constraint system for pages, designed to
keep dark surfaces calm and hierarchy legible. There is no signature
gradient: restraint is the signature.

**The ten invariants** (each has a real cost, think before overriding):

1. Page background is `--void` `#000` on screen and `--eggshell` `#f1f4f4` in
   light sections. Never a mid-gray page background.
2. The chromatic signature is the starfield plus two functional accents.
   Mint and cyan are functional (data, status, links), not decoration.
   The `--nebula-*` hues survive only as palette colors: pink/violet in
   code syntax, navy as the print emphasis color. There is no gradient
   treatment anywhere.
3. Text hierarchy on dark comes from the alpha ladder
   (`--ink` -> `--ink-80` -> `--ink-60` -> `--ink-50` -> `--ink-40` ->
   `--ink-30`), never from a second hue and never from gray hexes.
4. One geometric sans per page (`--sans`, Space Grotesk). `--mono` is for
   eyebrows, labels, code, and tabular figures, not prose.
5. Radius scale is `10 / 20 / 30 / full` and nothing else. Pills are always
   fully round; cards are almost always 20px.
6. Lines on dark are alpha strokes (`--stroke-*`), never solid grays. On
   light, hairlines are `--edge-light` / `--eggshell-dark`.
7. Surfaces are flat. The only shadow in the system belongs to cards on
   light surfaces. A hover never lifts; it inverts fill/foreground or
   brightens the alpha fill.
8. The starfield is the only sky texture and it lives in heroes only,
   masked so it fades before the next section. No gradient fills, no
   blurred orbs. A closing band uses flat `--nebula-navy`, never a
   gradient.
9. Print output flattens every alpha token to its registered
   `--print-ink-*` solid (WeasyPrint renders alpha fills as double
   rectangles). No 8-digit hex ships in a print template.
10. Motion is slow and single-purpose: gradient-flow 5s, entrances 700ms,
    marquee linear-infinite. Everything stops under
    `prefers-reduced-motion`.

---

## 1. Color

**Dark-first, alpha hierarchy, no gradient treatments** - this is the core.

### Surfaces (dark)

```css
--void:       #000000;   /* Page background - pure black, the space itself */
--surface-1:  #181818;   /* almost-black - hover state, sunken surface */
--surface-2:  #1e1f20;   /* off-black - the card fill on dark */
--surface-3:  #212121;   /* deepest raised surface, nav/dropdown */
--edge:       #37383a;   /* darker-gray - strongest solid border on dark */
```

**Rule**: raised surfaces step *up* from `#000` in tiny increments
(`18 -> 1e/1f/20 -> 21 -> 37` per channel). If a card needs more separation
than `--surface-2` gives, add a `--stroke-13` hairline, not a lighter fill.

### Text ladder (on dark)

Hierarchy is opacity, not hue. All values are white at a fixed alpha:

| Token | Hex | Alpha | Use |
|---|---|---|---|
| `--ink` | `#ffffff` | 100% | Titles, key figures, highlighted stats |
| `--ink-80` | `#ffffffcc` | 80% | Emphasized body, active nav |
| `--ink-60` | `#ffffff99` | 60% | Body copy, nav links, card text |
| `--ink-50` | `#ffffff80` | 50% | **The text floor.** Labels, eyebrows, captions, subdued prose |
| `--ink-40` | `#ffffff66` | 40% | Below the text floor - decorative or large text only |
| `--ink-30` | `#ffffff4d` | 30% | Ornament only - starfield, placeholders, marks |

Six levels is the whole ladder. Do not invent a 45% or a 90%.
`--ink-50` (~5.3:1 on black) is the floor for any text that carries
information; `--ink-40` (~3.7:1) and `--ink-30` (~2.6:1) pass only at
large sizes, so they are reserved for decoration and oversized display.

### Strokes and fills (on dark)

| Token | Hex | Alpha | Use |
|---|---|---|---|
| `--stroke-50` | `#ffffff80` | 50% | Strong border: focused inputs, active pill |
| `--stroke-20` | `#ffffff33` | 20% | Default card/pill border |
| `--stroke-13` | `#ffffff21` | 13% | Hairline: table rules, card rims |
| `--fill-20` | `#ffffff33` | 20% | Chip/tag fill |
| `--fill-10` | `#ffffff1a` | 10% | Hover fill on dark |
| `--fill-5` | `#ffffff0d` | 5% | Quietest fill: code gutter, inset band |

### Surfaces and text (light / eggshell mode)

```css
--eggshell:      #f1f4f4;   /* Light section background - cool porcelain */
--paper:         #ffffff;   /* Card fill on eggshell */
--eggshell-dark: #cfdadc;   /* Strong hairline, muted text on light */
--edge-light:    #e1e1e1;   /* Default hairline on light */
--gray-medium:   #bbbbbb;   /* Decorative marks on light */
--gray-mid:      #808080;   /* Tertiary on light - large text only */
--gray-dark:     #666666;   /* Labels and small text on light */
```

On light, text inverts: primary is `--void` `#000`, secondary is
`--surface-3`, labels and small text are `--gray-dark` (~5:1 on
eggshell). `--gray-mid` sits at ~3.6:1 on eggshell, so it is reserved
for large text and decoration. `--eggshell` is cool-toned (green-blue
undertone); do not warm it.

The same mapping runs a full light screen page
(`templates/landing-page-light.html`): `--paper` cards on `--eggshell`
with `--shadow-card`, `--nebula-navy` as the accent (mint/cyan stay off
text), and an inverted dust field (`--edge` + `--gray-medium` dots) in
place of the starfield. Code blocks stay dark on purpose - one
`--surface-1` island per page is allowed.

### Functional accents

```css
--mint: #22e2a8;   /* Growth, success, positive deltas, live status */
--cyan: #40b3ff;   /* Links on dark, informational highlights */
```

Accents appear as dots, ticks, small marks, links, and chart series.
Cyan carries links and info; mint carries status. Neither is body text
on dark - the ladder keeps prose achromatic - and neither fills more
than a chip. On light surfaces use `--nebula-navy` for emphasis
instead; mint/cyan read washed out on eggshell.

### Retired: the nebula gradient

Earlier revisions used a four-stop gradient (`#1a2340 -> #c98bd8 ->
#f2a7b8 -> #f6d6c2`) as a signature sky. It is retired: a blurred
gradient orb reads as generated filler and adds no information. The
`--nebula-*` colors remain registered for code syntax (pink/violet) and
print emphasis (navy); the gradient value itself is not a token and must
not be reintroduced as a `linear-gradient` anywhere.

### Starfield

```css
.starfield {
  background-image:
    radial-gradient(#ffffffcc 1.2px, transparent 1.6px),  /* bright layer */
    radial-gradient(#ffffff66 1px, transparent 1.4px);    /* dense faint  */
  background-size: 130px 130px, 34px 34px;
  background-position: 18px 34px, 0 0;
  opacity: 0.7;
  mask-image: linear-gradient(to bottom, black 40%, transparent 92%);
}
```

Two layers read as a sky where one reads as noise: a sparse bright
layer (130px spacing) over a dense faint layer (34px). White dots on
void, behind hero content only, masked so the field fades before the
next section. One field per page; never tile it behind body sections.

---

## 2. Typography

### Stacks

```css
/* Geometric sans - carries every level of the page */
--sans: "Space Grotesk", "The Future", ui-sans-serif,
        system-ui, -apple-system, "Segoe UI", sans-serif;

/* Mono - eyebrows, labels, code, figures */
--mono: "JetBrains Mono", "The Future Mono", "Space Mono",
        ui-monospace, SFMono-Regular, Menlo, monospace;
```

"Space Grotesk" is the shipped free substitute for the commercial
"The Future" (Klim); if a license exists, move it first in the stack.
Load via Google Fonts (`Space Grotesk: 400,500,700` and
`JetBrains Mono: 400,500`) or self-host. Display text may add
`font-feature-settings: "ss02"` for the geometric alternate shapes.

### Size scale (px, screen-first)

| Role | Size | Weight | Line-height | Use |
|---|---|---|---|---|
| Display | 56-96 fluid | 500 | 1.05 | Hero H1, `clamp(56px, 7vw, 96px)`, -0.035em |
| H1 | 36 | 500 | 1.22 | Page titles, hero on tablet |
| H2 | 32 | 500 | 1.25 | Section titles (site uses 32-36) |
| H3 | 24 | 500 | 1.35 | Card groups, sub-sections |
| Lede | 18-20 | 400 | 1.5 | Section ledes, hero tagline |
| Body | 16 | 400 | 1.5 | Default prose, nav links |
| Body small | 14 | 400 | 1.5 | Secondary prose, card text |
| Label | 12-13 | 500 | 1.6 | Eyebrows, chips, footer labels |
| Micro | 12 | 400 | 1.6 | Metadata, legal |

**Ladder discipline**: sizes land ON the scale, never between steps;
display is the one fluid step (a clamp, not a free value). Audit with
`grep -o 'font-size: [0-9.]*px' file | sort | uniq -c` - every
value should be a step above. Floor is 12px and it carries labels only,
never prose (prose stops at 14).

### Weight

- Headings and display: **500** (medium). The site never uses bold for
  hierarchy.
- Body: **400**. Strong emphasis inside prose is `--ink` + weight 500.
- Mono labels/eyebrows: **500**; mono body/code: **400**.
- **Forbidden**: 100-300 thin weights for text (the family ships them;
  they fail on dark backgrounds), and 900 for anything but a deliberate
  display stunt.

### Line-height

| Tier | Value | Use |
|---|---|---|
| Display | 1.13-1.22 | 60px hero, 36px titles |
| Headline | 1.25-1.35 | H2/H3 |
| Body | 1.5 | All prose, all sizes |
| Label | 1.6 | Eyebrows, captions, legal |

**Forbidden**: 1.7+ (floaty, loses the compact technical feel) and
sub-1.1 (collides at every size this system uses).

### Letter-spacing

- Display: **-0.035em** at 56px+; H1 and below: **-0.01em to 0**
  (Space Grotesk is already wide).
- Prose and long ledes: **0.02em** (the site's body tracking).
- Nav links, buttons: **0.32px** (~0.02em at 16px).
- Eyebrows, labels, legal: **0.48px** (12px labels) with
  `text-transform: uppercase` for the eyebrow form.
- Mono eyebrow may push to **0.06em**; never track body copy wider.

---

## 3. Spacing and layout

### Base unit: 4px

| Tier | Value | Use |
|---|---|---|
| xs | 4-8px | Inline gaps, icon-text pairs |
| sm | 12-16px | Chip padding, dense interiors |
| md | 24-32px | Card padding, component interiors |
| lg | 48-64px | Between components, card groups |
| xl | 96-108px | Between major sections (desktop) |
| 2xl | 150px+ | Hero top offset, page-level air |

**Section rhythm is a ladder, not per-gap**: desktop 96/108px, tablet
72px, phone 56px between major sections. Scale the whole ladder by one
factor when tuning; never nudge a single gap.

**Proximity law**: the gap under a section head is
clearly smaller than the gap above it, ideally 2x+. A head belongs to
what follows it.

### Frame

```css
.container { max-width: 1440px; margin: 0 auto; }
```

- Side padding: `~100px` desktop (`px-25` / `6.24rem` on the site),
  `~30px` phone (`1.88rem`). Content column inside the frame is often
  narrower: hero `w-2/3`, ledes `max-w-3xl`, prose `max-w-4xl`.
- Breakpoints: `sm 640`, `lg 1024`, `xl 1280`, `2xl 1536`. Two working
  breakpoints (1024 and 640) cover nearly all layout changes.
- Hero: `min-height` near `100svh`; the hero *visual* (product mock or
  starfield field) caps at `--layout-hero-max-height: 950px`. Content
  vertically centered against the visual.

### Radius

| Token | Value | Use |
|---|---|---|
| `--radius-sm` | 10px | Chips, code blocks, small frames |
| `--radius-md` | 20px | **The card radius.** Nearly every surface |
| `--radius-lg` | 30px | Large media frames, hero panels |
| `--radius-pill` | 999px | Pills, tags, dots - always fully round |

20px is the workhorse (110+ card instances on the site). Do not introduce
a 14px or a 24px card. Sub-10px radii (2-8px) appear only inside
miniature preview graphics - sheet lines, mock window dots, code chips -
which are illustrations of components, not components.

---

## 4. Components

Two tiers: **primitives** are the atoms (pill, link, field, chip);
**patterns** are the assembled recipes (nav, hero, stat strip, pricing).
The showcase renders both in the same order.

### Nav

Fixed top bar, `--void` background, `z-index: 200`, height ~64-72px.
Wordmark left (sans 500, `--ink`), links `--ink-60` 16px tracking 0.32px
hovering to `--ink`, one pill CTA right. Optional `--stroke-13` bottom
hairline or a backdrop blur after scroll; never both a heavy border and
a shadow.

### Pill buttons

The only button shape. `border-radius: 999px`, height 34px (phone) /
42px (desktop), padding `0 16-20px`, text 12-16px weight 500.

| Variant | Resting | Hover |
|---|---|---|
| `.pill` on dark | `--void`/`--fill-5` fill, `--stroke-20` border, `--ink` text | `--ink` fill, `--void` text (invert) |
| `.pill` on light | `--eggshell` fill, `--void` text, no border | `--surface-2` fill, `--ink` text (invert) |
| `.pill-solid` | `--ink` fill + `--void` text on dark; `--void` + `--ink` on light | drops to `--ink-80` / `--surface-2` |

Hover = inversion or fill-brighten + `transition: all .3s ease-in-out`.
Never lift, never shadow, never recolor to an accent.

### Links

Inline links are `--cyan` on dark, `--nebula-navy` on light. A resting
link carries a quiet underline (`--stroke-20` / `--eggshell-dark` bottom
border); hover tightens it to the accent. `focus-visible` draws a 1px
accent outline with a 3px offset. Body text never borrows the accent to
look like a link.

### Tabs

A segmented control is a pill-shaped container (`999px`, 2px pad,
`--stroke-13` rim) holding mono 10-12px uppercase segments. The active
segment inverts (`--ink` fill, `--void` text); inactive segments sit at
`--ink-50`. The hero theme toggle is this component - same skin,
different state.

### Form fields

```css
.field {
  background: var(--surface-2);          /* --paper on light */
  border: 1px solid var(--stroke-13);    /* --edge-light on light */
  border-radius: var(--radius-sm);       /* 10px */
  padding: 10px 14px; font-size: 14px;
}
```

Focus moves the rim to the mode's accent; no shadow, no floating labels.
Placeholders sit at `--ink-50` / `--gray-dark`. Checkboxes and radios
take `accent-color` from the accent. Selects keep the native arrow -
the skin is the border and the fill, nothing more.

### Alert

A hairline band, not a fill: `--stroke-13` rim, 10px radius, 13-14px
`--ink-80` text, and a 7px status dot as the only signal. `--mint` = ok,
`--nebula-pink` = error. No tinted backgrounds, no icon set beyond the
dot.

### Eyebrow

```css
.eyebrow {
  font-family: var(--mono);
  font-size: 12px; font-weight: 500;
  letter-spacing: 0.48px; text-transform: uppercase;
  color: var(--ink-50);
}
```

Left-aligned above the H2, one line, optionally `NN -` numbered. On
light: `--gray-dark`.

### Section head

`eyebrow` + `h2` (32px/500, `--ink`) + optional lede (18px, `--ink-60`,
`max-w-3xl`). 14-20px between eyebrow and title; the section's outer
margin creates the pause. No decorative rule, no accent bar.

### Cards

```css
.card {
  background: var(--surface-2);
  border: 1px solid var(--stroke-13);
  border-radius: var(--radius-md);   /* 20px */
  padding: 24px 28px;
}
```

Flat, hairline-rimmed, 20px radius. Hover on a linked card: fill steps
to `--surface-3` or the rim brightens to `--stroke-20`; text stays put.
On light: `--paper` fill, `--edge-light` rim, and *only here* the one
sanctioned shadow may appear (`0 2px 10px rgba(30,31,32,.10)`).

### Chips / tags

```css
.chip {
  font-family: var(--mono);
  font-size: 12px; font-weight: 500;
  letter-spacing: 0.48px; text-transform: uppercase;
  color: var(--ink-60);
  background: var(--fill-10);
  border: 1px solid var(--stroke-13);
  border-radius: 999px;
  padding: 4px 12px;
}
```

A chip row states *qualities*, not an inventory; about three, middot or
gap separated. Status chips may carry a 6px `--mint`/`--cyan` dot - the
dot is the only accent that small.

### Stat strip

The canonical metrics pattern: a 4-column grid where each cell is value
(32-36px sans 500, `--ink`, `tabular-nums`) over label (12px mono
uppercase, `--ink-50`), separated by `--stroke-13` hairlines, the whole
strip framed top and bottom by `--stroke-13` rules. Two columns on
phone, with the top hairline restored between rows.

```css
.stats { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr));
         border-top: 1px solid var(--stroke-13);
         border-bottom: 1px solid var(--stroke-13); }
.stat { padding: 28px 24px; min-width: 0; }
.stat + .stat { border-left: 1px solid var(--stroke-13); }
```

Never box metrics in cards; numbers carry themselves. A looser variant
for hero footers is the inline bumper: one running sentence at 20-24px
in `--ink-50` with each number wrapped in `--ink`.

### Feature list

Two-column grid (name column ~200px + description `1fr`), rows separated
by `--stroke-13` hairlines, 36px gap. Feature name 20-24px `--ink`
weight 500; description 15-16px `--ink-60`, line-height 1.5. A `--cyan`
link inside the description is the only color beyond the ladder.

### Marker list

A plain `ul` where a mono `+` in `--mint` marks included and `–` in
`--ink-40` marks excluded; excluded rows dim to `--ink-50`. For plan
contents and comparisons, not prose.

### Blockquote

One `--stroke-20` left rule, 20px indent, the quote at 16-18px
`--ink-80`, and the attribution in the mono label voice. No quotation
marks, no oversized quote glyph - the rule is enough.

### Divider

The hairline is the only divider: `--stroke-13` (dark) / `--edge-light`
(light) inside a section, `--stroke-20` / `--eggshell-dark` between
chapters. Never a thicker rule, never a gradient fade.

### Code block

```css
.code-block {
  background: var(--surface-1);
  border: 1px solid var(--stroke-13);
  border-radius: var(--radius-sm);
  padding: 18px 22px;
  font-family: var(--mono);
  font-size: 13.5px; line-height: 1.55;
  color: var(--ink-80);
}
```

Dark surface, mono, `tabular-nums`. Optional macOS-style three-dot
header in `--fill-10`. Syntax palette on dark (restrained, one token
per role):

| Token | Hex | Role |
|---|---|---|
| Comment | `#ffffff4d` | `--ink-30` |
| Keyword | `#40b3ff` | `--cyan` |
| String | `#22e2a8` | `--mint` |
| Number | `#f2a7b8` | `--nebula-pink` |
| Function | `#c98bd8` | `--nebula-violet` |
| Operator/text | `#ffffffcc` | `--ink-80` |

### Logo wall / marquee

Grayscale partner marks (`filter: grayscale(1)`, `--ink-40` or
`opacity: .4`), one row, `animate-scroll` linear-infinite marquee that
pauses on hover. Label above: mono eyebrow. No card frames around
marks.

### Table

```css
table { width: 100%; border-collapse: collapse; font-size: 14px; }
th { text-align: left; font-weight: 500; color: var(--ink-50);
     font-family: var(--mono); font-size: 12px; letter-spacing: 0.48px;
     text-transform: uppercase;
     padding: 8px 12px; border-bottom: 1px solid var(--stroke-20); }
td { padding: 10px 12px; border-bottom: 1px solid var(--stroke-13);
     color: var(--ink-60); }
```

Hairline rules only, no verticals, no filled header, no frame. Numeric
columns right-aligned with `tabular-nums`. On light: `--edge-light`
rules, `--gray-dark` header.

### FAQ

Native `<details>`/`<summary>` accordion: rows separated by
`--stroke-13` hairlines, question 16px 500 `--ink`, a mono `+` marker in
`--ink-50` that rotates 45deg when open, answer 14px `--ink-60` capped
at ~660px. No JS required. Questions never take accent color (reads as
a link).

### Product mock

A landing hero may carry a pure-CSS product window instead of a
screenshot: `--surface-1` frame at 20px radius with a `--stroke-13` rim,
three-dot title bar (`--fill-10` dots + mono 11px title in `--ink-30`),
and inside it the same primitives (sidebar lines in `--fill-10`,
task rows with `--mint`/`--cyan` status). It demonstrates the system
rather than faking a UI; keep every element a real token.

### Pricing

Three cards max (`--surface-2`, 20px, `--stroke-13`). Plan name mono
uppercase `--ink-50` (the highlighted plan uses `--mint` and a
`--stroke-50` rim, nothing more). Amount 40px sans 500 with a 14px
`--ink-50` per-unit suffix. Feature list: 14px `--ink-60` rows with a
mint check glyph. CTA is a pill, `pill-solid` on the highlighted plan
only. Never invent discounts, countdowns, or "most popular" badges
beyond the one highlighted card.

### Media frame

Large media gets `--radius-lg` (30px) and a `--stroke-13` rim. The frame
holds imagery or a live island (starfield, product mock); captions live
outside it in the mono label voice.

### CTA band

A flat `--nebula-navy` band - the one place a saturated fill carries a
section. Centered headline, one pill CTA in `--eggshell` with navy text.
The band keeps its navy in every mode; it is a fixed-color island, like
the code block.

### Footer

One baseline row with a `--stroke-13` top hairline: mark left, inline
links right (`--ink-60` -> `--ink` on hover), mono legal line. A pattern
library's footer is a signature line, not a sitemap.

---

## 5. Depth and motion

**Core rule**: surfaces are flat. Hierarchy comes from the alpha ladder,
hairlines, spacing, and the gradient. The only shadows in the system are
the two registered light-card shadows:

```css
--shadow-card:  0 2px 10px rgba(30,31,32,0.10);
--shadow-lift:  0 8px 24px rgba(30,31,32,0.12);
```

They belong to `--paper` cards on `--eggshell` and nowhere else. Dark
surfaces never cast a shadow - elevation is `--surface-2` over `--void`.

### Motion tokens

| Token | Value | Use |
|---|---|---|
| `--ease-out` | `cubic-bezier(0, 0, 0.2, 1)` | Entrances, hovers |
| `--ease-in-out` | `cubic-bezier(0.4, 0, 0.2, 1)` | Inversions, pills |
| `--dur-fast` | 150ms | Micro feedback |
| `--dur-med` | 300ms | Pill invert, fills |
| `--dur-slow` | 700ms | Scroll entrances |
| `--dur-flow` | 5s | Gradient-flow lines |

- **Entrance**: `opacity: 0; translateY(32px)` -> visible, 700ms
  `ease-out`, once. Never on the hero title - it is readable at t=0.
- **Gradient-flow** (`gradient-animate-*`): a white vertical beam
  (`linear-gradient(#fff0, #fff 50%, #fff0)`, `background-size: 100%
  200%`) travels a hairline or card edge, 5s `ease-in-out` infinite,
  `opacity` pulsing 0 -> 1. It marks a *live* connection or data path;
  it is not ambient decoration.
- **Marquee**: `animate-scroll` linear infinite; pause on hover.
- `prefers-reduced-motion`: kill flow, marquee, and entrances entirely.

---

## 6. Print (eggshell mode)

Print output uses the light palette on A4. The canonical print artifact
is the eggshell one-pager; a dark page remaps its register to print
solids under `@media print` rather than shipping alpha to paper
(site/index.html does this).
WeasyPrint-class constraints apply: **no alpha anywhere** - every
`--ink-*` / `--fill-*` / `--stroke-*` token flattens to a solid
registered `--print-ink-*` value:

| Dark token | Print solid | Hex |
|---|---|---|
| `--ink-80` | `--print-ink-80` | `#cccccc` |
| `--ink-60` | `--print-ink-60` | `#999999` |
| `--ink-50` | `--print-ink-50` | `#808080` |
| `--ink-40` | `--print-ink-40` | `#666666` |
| `--ink-30` | `--print-ink-30` | `#4d4d4d` |

- Paper: `--eggshell` `#f1f4f4` (`@page` background, extends past the
  margin box). Cards: `--paper`, hairlines `--edge-light`.
- Text: `--void` primary, `--surface-3` secondary, `--gray-dark` labels.
- Emphasis color: `--nebula-navy` `#1a2340` - the only chromatic text
  color in print (tags, links, key figures). Mint/cyan survive only as
  chart series and status dots.
- No starfield, no gradient-flow, no marquee in print. The cover band
  uses flat `--nebula-navy`, never a gradient.
- Page margins: one-pager `15/18mm`, long doc `20/22mm`, letter `25mm`.
  Print type scale = screen px / 1.33, with the same ladder discipline.

---

## 7. Quick decisions

| Need | Use |
|---|---|
| Page background | `--void` (dark) or `--eggshell` (light section) |
| Big headline | sans 500, 36-60px, line-height 1.13-1.22, `--ink` |
| Body | sans 400, 16px, `--ink-60`, line-height 1.5 |
| Quiet label | mono 12px 500, 0.48px tracking, uppercase, `--ink-50` |
| Emphasize a number | `--ink` (brighten) or `--nebula-navy` in print; never bold-900 |
| Interactive element | pill, invert on hover, `--dur-med` |
| Container | `--surface-2` card, 20px radius, `--stroke-13` rim |
| Divider | `--stroke-13` hairline (dark) / `--edge-light` (light) |
| Celebration / sky moment | the starfield, in the hero only |
| Status mark | 6px `--mint` (ok) or `--cyan` (info) dot + label |

Nothing fits -> return to first principles: **the void is flat,
starlight is hierarchy, the starfield is the sky, pills are round**.
Add the smallest thing that works, prefer an existing class, and
register any new hex in `tokens.json` before it ships.

---

## 8. Acceptance checks

- `python3 scripts/check_tokens.py` - every `var(--*)` in templates
  resolves to `tokens.json`, and every hex in templates is registered.
- Dark-page audit: text colors are only `--ink*`; borders only
  `--stroke-*`; fills only `--surface-*`/`--fill-*`.
- Gradient audit: `grep -c 'linear-gradient(160deg'` == 0 per page.
  The only gradients are the starfield's `radial-gradient` dots and the
  white gradient-flow beam.
- Radius audit: only 10/20/30/999 values.
- Motion audit: no animation outside the registered set;
  `prefers-reduced-motion` handled.
- Interaction audit: every interactive element has `:focus-visible`
  (2px `--cyan` outline, 3px offset); anchor targets carry
  `scroll-margin-top` >= 80px under a fixed nav; the nav CTA pill stays
  visible at mobile widths.
- Theme audit: the showcase toggles dark/light in place by remapping the
  register under `html.light` (dark page) or `html.dark` (light page);
  the choice persists in `localStorage`. Islands - code blocks, dark
  panels, template previews - pin explicit hexes so they keep their
  native canvas in either theme.
- Orientation audit: the section rail (fixed mono numerals, 1560px+)
  highlights the section in view; it is hidden in print and under
  reduced motion.
- Contrast audit: `--ink-50` is the floor for text that carries
  information on dark; `--ink-40`/`--ink-30` are decorative or
  large-display only. On light, small text floors at `--gray-dark`;
  `--gray-mid` is for large text and decoration.
