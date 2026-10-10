# Production Guide

Technical specifications for rendering, fonts, and print output.

---

## 1. Rendering Pipeline

### PDF Generation

Use WeasyPrint for PDF output:

```bash
weasyprint template.html output.pdf
```

**Requirements**:
- Python 3.8+
- WeasyPrint 59+
- Pango, Cairo, GDK-Pixbuf

**Critical**: WeasyPrint renders alpha fills as double rectangles. All tokens
flatten to solid hexes in print templates. Never ship 8-digit hex to PDF.

### Browser Preview

Templates include `@media screen` rules for browser preview:
- Dark desk background (`--surface-1`)
- Centered sheet with shadow
- Proper padding simulation

---

## 2. Font Loading

### Required Fonts

| Font | Weights | Source |
|------|---------|--------|
| Space Grotesk | 400, 500 | Google Fonts |
| JetBrains Mono | 400, 500 | Google Fonts |

### Google Fonts Embed

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

### Self-Hosting

For offline/print reliability, self-host fonts:

```css
@font-face {
  font-family: 'Space Grotesk';
  font-weight: 400;
  src: url('./fonts/SpaceGrotesk-Regular.woff2') format('woff2');
}
@font-face {
  font-family: 'Space Grotesk';
  font-weight: 500;
  src: url('./fonts/SpaceGrotesk-Medium.woff2') format('woff2');
}
```

**WeasyPrint note**: Use absolute paths or verify CWD. Relative paths resolve
from the working directory, not the HTML file location.

### Font Verification

Before PDF render, verify fonts load:

```python
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

font_config = FontConfiguration()
html = HTML(filename='template.html')
# Check logs for "Cannot load font" warnings
```

---

## 3. Page Setup

### Paper Sizes

| Template | Size | Margins |
|----------|------|---------|
| One-pager | A4 | 15mm × 18mm |
| Resume | A4 | 14mm × 16mm |
| Portfolio | A4 | 12mm × 15mm |
| Letter | A4 | 25mm |
| Long-doc | A4 | 20mm × 22mm |
| Slides | 1920×1080 | 0 |

### @page Rules

```css
@page {
  size: A4;
  margin: 15mm 18mm;
  background: #f1f4f4;  /* eggshell - solid hex only */
}
```

### Page Breaks

```css
/* Prevent orphaned headings */
h2, h3 { break-after: avoid; }

/* Keep cards together */
.card, .project, .job { break-inside: avoid; }

/* Force page break */
.cover { break-after: page; }

/* Widow/orphan control */
p { widows: 3; orphans: 3; }
```

---

## 4. Print Token Flattening

Alpha tokens must flatten to solid hexes for PDF:

| Screen Token | Print Token | Hex |
|--------------|-------------|-----|
| `--ink-80` | `--print-ink-80` | `#cccccc` |
| `--ink-60` | `--print-ink-60` | `#999999` |
| `--ink-50` | `--print-ink-50` | `#808080` |
| `--ink-40` | `--print-ink-40` | `#666666` |
| `--ink-30` | `--print-ink-30` | `#4d4d4d` |

### Implementation

```css
/* Screen uses alpha */
.label { color: var(--ink-50); }

/* Print flattens to solid */
@media print {
  .label { color: var(--print-ink-50); }
}
```

---

## 5. Type Scale Conversion

Screen pixels to print points (factor: 1.33):

| Screen (px) | Print (pt) | Use |
|-------------|-----------|-----|
| 56-96 | 42-72 | Display |
| 36 | 27 | H1 |
| 32 | 24 | H2 |
| 24 | 18 | H3 |
| 16 | 12 | Body |
| 14 | 10.5 | Body small |
| 12 | 9 | Labels |

---

## 6. Color Verification

### Check Contrast

Minimum contrast ratios (WCAG AA):
- Body text: 4.5:1
- Large text (18pt+): 3:1
- UI components: 3:1

| Token | On `--void` | On `--eggshell` |
|-------|-------------|-----------------|
| `--ink-50` | 5.3:1 ✓ | - |
| `--ink-40` | 3.7:1 (large only) | - |
| `--gray-dark` | - | 5.1:1 ✓ |
| `--gray-mid` | - | 3.6:1 (large only) |

### Print Colors

Only these chromatic colors appear in print:
- `--nebula-navy` (`#1a2340`) - emphasis, links, tags
- `--mint` (`#22e2a8`) - status dots only
- `--cyan` (`#40b3ff`) - chart series only

---

## 7. Asset Handling

### Images

```css
/* Responsive images */
img {
  max-width: 100%;
  height: auto;
}

/* Print: ensure images don't break */
figure, .image-frame {
  break-inside: avoid;
}
```

### Image Formats

| Format | Use |
|--------|-----|
| WebP | Screen, with JPEG fallback |
| PNG | Logos, diagrams with transparency |
| SVG | Icons, diagrams (inline preferred) |
| JPEG | Photos in print PDF |

---

## 8. Quality Checklist

Before shipping any template:

- [ ] All `var(--*)` resolve to `tokens.json`
- [ ] No alpha values (`rgba()`, 8-digit hex) in print
- [ ] Fonts load without warnings
- [ ] Page breaks tested at content boundaries
- [ ] Contrast ratios verified
- [ ] Mobile responsive (640px breakpoint)
- [ ] `prefers-reduced-motion` handled
- [ ] PDF renders without warnings

### Automated Checks

```bash
# Token verification
python3 scripts/check_tokens.py templates/*.html

# Find alpha values in print
grep -E '#[0-9a-f]{8}|rgba\(' templates/*.html
```

---

## 9. Browser Support

### Screen Preview

| Browser | Support |
|---------|---------|
| Chrome 90+ | Full |
| Firefox 88+ | Full |
| Safari 14+ | Full |
| Edge 90+ | Full |

### CSS Features Used

- CSS Custom Properties (variables)
- CSS Grid
- Flexbox
- `break-inside`, `break-after`
- `@media print`
- `prefers-reduced-motion`

---

## 10. Troubleshooting

### WeasyPrint Issues

**Double rectangles on fills**: Using `rgba()` - flatten to solid hex.

**Fonts not loading**: Check paths are absolute or CWD is correct.

**Page overflow**: Content exceeds margins - add `break-inside: avoid`.

**Blank pages**: Margin + content exceeds page height - reduce margins.

### Browser Issues

**Fonts flash**: Add `font-display: swap` to @font-face.

**Print cuts off**: Browser print margins conflict - use `@page` margins.
