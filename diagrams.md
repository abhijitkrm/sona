# Diagram System

Specifications for charts, diagrams, and visual data.

---

## 1. Core Principles

### Constraint-Based

- **One accent color** per diagram (navy or mint)
- **Coordinates divisible by 4** for alignment
- **Maximum complexity budget** per diagram type
- **No decorative elements** - every mark encodes data

### Color Palette

```css
/* Diagram tokens */
--diagram-bg:      #f1f4f4;  /* eggshell canvas */
--diagram-fg:      #000000;  /* void - primary marks */
--diagram-line:    #212121;  /* surface-3 - connecting lines */
--diagram-accent:  #1a2340;  /* nebula-navy - emphasis */
--diagram-muted:   #666666;  /* gray-dark - labels */
--diagram-surface: #ffffff;  /* paper - node fills */
--diagram-border:  #e1e1e1;  /* edge-light - borders */
--diagram-mint:    #22e2a8;  /* positive/success */
--diagram-cyan:    #40b3ff;  /* informational */
```

### On Dark Backgrounds

```css
--diagram-bg:      #000000;  /* void */
--diagram-fg:      #ffffff;  /* ink */
--diagram-line:    #ffffff80; /* ink-50 */
--diagram-accent:  #22e2a8;  /* mint */
--diagram-muted:   #ffffff66; /* ink-40 */
--diagram-surface: #1e1f20;  /* surface-2 */
--diagram-border:  #ffffff21; /* stroke-13 */
```

---

## 2. Diagram Types

### 2.1 Flowchart

Process flows with decision points.

**Complexity budget**: 8-12 nodes max
**Direction**: Top-to-bottom or left-to-right

```
┌─────────┐     ┌─────────┐     ┌─────────┐
│  Start  │────▶│ Process │────▶│   End   │
└─────────┘     └─────────┘     └─────────┘
                    │
                    ▼
               ◇─────────◇
              ╱ Decision? ╲
             ◇─────────────◇
              Yes │    │ No
                  ▼    ▼
```

**Node styles**:
- Rectangle: Process step
- Diamond: Decision
- Rounded: Start/End
- Parallelogram: I/O

### 2.2 Architecture

System component diagrams.

**Complexity budget**: 6-15 components
**Grouping**: Use containers for logical grouping

```
┌─────────────────────────────────────┐
│           Frontend                  │
│  ┌─────────┐  ┌─────────┐          │
│  │   App   │  │  Admin  │          │
│  └────┬────┘  └────┬────┘          │
└───────┼────────────┼────────────────┘
        │            │
        ▼            ▼
┌─────────────────────────────────────┐
│             API Gateway             │
└─────────────────┬───────────────────┘
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
    ┌───────┐ ┌───────┐ ┌───────┐
    │Service│ │Service│ │Service│
    └───────┘ └───────┘ └───────┘
```

### 2.3 Sequence

Interaction timelines between actors.

**Complexity budget**: 4-6 participants, 8-15 messages

```
 User          App          Server        DB
  │             │              │           │
  │──Request───▶│              │           │
  │             │──Validate───▶│           │
  │             │              │──Query───▶│
  │             │              │◀──Data────│
  │             │◀──Response───│           │
  │◀──Result────│              │           │
  │             │              │           │
```

### 2.4 Timeline

Chronological events.

**Complexity budget**: 5-10 events

```
2022 ────●──────────●──────────●──────── 2024
         │          │          │
      Founded    Series A   10K Users
```

### 2.5 Hierarchy / Org Chart

Tree structures.

**Complexity budget**: 15-25 nodes
**Depth**: 3-4 levels max

```
                  ┌─────────┐
                  │   CEO   │
                  └────┬────┘
         ┌─────────────┼─────────────┐
         ▼             ▼             ▼
    ┌─────────┐   ┌─────────┐   ┌─────────┐
    │   CTO   │   │   CFO   │   │   COO   │
    └────┬────┘   └─────────┘   └─────────┘
    ┌────┼────┐
    ▼    ▼    ▼
```

### 2.6 Comparison Matrix

2x2 or larger grids.

**Complexity budget**: 2-4 columns, 3-8 rows

```
           Feature A    Feature B    Feature C
Product X      ●            ○            ●
Product Y      ○            ●            ●
Product Z      ●            ●            ○

● = Included   ○ = Not included
```

### 2.7 Funnel

Conversion stages.

**Complexity budget**: 3-6 stages

```
     ╱─────────────────────────────╲   Visitors: 100K
    ╱───────────────────────────────╲
   ╱─────────────────────────────────╲
  ├───────────────────────────────────┤  Signups: 10K
  │                                   │
  ├───────────────────────────────────┤  Active: 4K
  │                                   │
  └───────────────────────────────────┘  Paid: 1K
```

---

## 3. Chart Types

### 3.1 Bar Chart

Category comparisons.

**Max categories**: 8
**Orientation**: Horizontal for long labels, vertical for time series

```css
.bar {
  fill: var(--diagram-accent);
  border-radius: 2px;
}
.bar:hover {
  fill: var(--diagram-mint);
}
```

### 3.2 Line Chart

Trends over time.

**Max data points**: 12 per series
**Max series**: 3

```css
.line {
  stroke: var(--diagram-accent);
  stroke-width: 2px;
  fill: none;
}
.dot {
  fill: var(--diagram-accent);
  r: 4px;
}
```

### 3.3 Donut/Pie

Proportions of a whole.

**Max segments**: 6
**Always include**: Labels or legend

```css
.segment {
  stroke: var(--diagram-bg);
  stroke-width: 2px;
}
```

**Color sequence**:
1. `--nebula-navy`
2. `--mint`
3. `--cyan`
4. `--gray-dark`
5. `--gray-mid`
6. `--edge-light`

### 3.4 Sparkline

Inline trend indicator.

**Max points**: 20
**Size**: 60-100px wide, 16-24px tall

```css
.sparkline {
  stroke: var(--diagram-accent);
  stroke-width: 1.5px;
  fill: none;
}
```

---

## 4. Styling Rules

### Typography

| Element | Font | Size | Weight |
|---------|------|------|--------|
| Title | sans | 14pt | 500 |
| Labels | mono | 9pt | 500 |
| Axis | mono | 8pt | 400 |
| Legend | sans | 10pt | 400 |

### Spacing

- **Node padding**: 12-16px
- **Node gap**: 24-40px
- **Label offset**: 8px from element
- **Grid lines**: every 4px

### Lines and Arrows

```css
/* Connection lines */
.connector {
  stroke: var(--diagram-line);
  stroke-width: 1px;
  fill: none;
}

/* Arrows */
.arrow {
  fill: var(--diagram-line);
}

/* Dashed for optional/async */
.connector--dashed {
  stroke-dasharray: 4 4;
}
```

### Nodes

```css
.node {
  fill: var(--diagram-surface);
  stroke: var(--diagram-border);
  stroke-width: 1px;
  rx: 4px; /* border-radius */
}

.node--emphasis {
  stroke: var(--diagram-accent);
  stroke-width: 2px;
}
```

---

## 5. SVG Best Practices

### Accessibility

```html
<svg role="img" aria-labelledby="title desc">
  <title id="title">System Architecture</title>
  <desc id="desc">Shows data flow from frontend to database</desc>
  <!-- diagram content -->
</svg>
```

### Responsive

```html
<svg viewBox="0 0 800 400" preserveAspectRatio="xMidYMid meet">
  <!-- content scales to container -->
</svg>
```

### Print Optimization

- Embed fonts or convert text to paths
- Use solid fills, no gradients
- Test at 300 DPI

---

## 6. Mermaid Integration

Sona includes a Mermaid theme for quick diagrams.

### Usage

```html
<div class="mermaid">
graph TD
    A[Start] --> B{Decision}
    B -->|Yes| C[Process]
    B -->|No| D[End]
</div>
```

### Theme Configuration

See `mermaid-theme.json`:

```json
{
  "theme": "base",
  "themeVariables": {
    "primaryColor": "#1a2340",
    "primaryTextColor": "#ffffff",
    "primaryBorderColor": "#cfdadc",
    "lineColor": "#212121",
    "secondaryColor": "#f1f4f4",
    "tertiaryColor": "#ffffff"
  }
}
```

---

## 7. Anti-Patterns

### Never Do

- 3D effects on charts
- Gradients in bars/segments
- More than 3 colors per diagram
- Legends inside the chart area
- Vertical text on arrows
- Decorative icons that don't encode data
- Pie charts for >6 segments
- Line charts for <4 data points

### Watch For

- Truncated axes that exaggerate differences
- Missing units on axes
- Inconsistent scales across charts
- Color-only encoding (add patterns for accessibility)

---

## 8. Checklist

Before including a diagram:

- [ ] Complexity within budget for type
- [ ] Colors from diagram palette only
- [ ] Labels use mono font
- [ ] All text is legible at final size
- [ ] Accessible (title, desc, or caption)
- [ ] Renders correctly in print
- [ ] No decorative elements
- [ ] Data source cited if external
