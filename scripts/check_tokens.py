#!/usr/bin/env python3
"""Token drift guard.

Three checks over templates/*.html and site/*.html:

1. Every var(--name) referenced in a page must be defined in that
   page's own :root block. tokens.json is a register, not a runtime
   source - the browser only sees the page's own definitions.
2. Every hex literal (#rgb, #rgba, #rrggbb, #rrggbbaa) in a page must
   be a registered token value in tokens.json. A color that is not in
   the register is palette drift; add it to tokens.json first.
3. Every --name defined in a page's :root that also exists in
   tokens.json must carry the identical value. Divergence is drift.

Lines tagged with an inline avoid marker (/* avoid */ or
<!-- avoid -->) are exempt - they are deliberate counter-examples.

Exits non-zero on any violation. Run from the repository root:

    python3 scripts/check_tokens.py
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = ROOT / "tokens.json"
SCAN_DIRS = [ROOT / "templates", ROOT / "site"]

VAR_RE = re.compile(r"var\((--[a-z0-9-]+)\)")
ROOT_BLOCK_RE = re.compile(r":root\s*\{(.*?)\}", re.S)
DEF_RE = re.compile(r"(--[a-z0-9-]+)\s*:\s*([^;}]+)")
HEX_RE = re.compile(r"(?<!&)#[0-9a-fA-F]{3,8}\b")  # (?<!&) skips &#...; HTML entities
AVOID_MARKERS = ("/* avoid */", "<!-- avoid -->")


def strip_print_media(text: str) -> str:
    """Remove @media print blocks before collecting :root definitions.

    A print block may legitimately remap registered tokens to their
    registered solid counterparts (the print doctrine). That is a remap,
    not drift, so check 3 must not compare those values. var() and hex
    checks still run over the full text, so a print remap may only use
    registered hexes and tokens the page already defines."""
    out, i = [], 0
    while True:
        j = text.find("@media print", i)
        if j == -1:
            out.append(text[i:])
            break
        out.append(text[i:j])
        b = text.find("{", j)
        if b == -1:
            i = j + len("@media print")
            continue
        depth, k = 1, b + 1
        while k < len(text) and depth:
            depth += text[k] == "{"
            depth -= text[k] == "}"
            k += 1
        i = k
    return "".join(out)


def norm(h: str) -> str:
    """Normalize a hex literal: lowercase, expand 3/4-digit shorthand."""
    h = h.strip().lower()
    if len(h) == 4:      # #rgb -> #rrggbb
        h = "#" + "".join(c * 2 for c in h[1:])
    elif len(h) == 5:    # #rgba -> #rrggbbaa
        h = "#" + "".join(c * 2 for c in h[1:])
    return h


def main() -> int:
    tokens = json.loads(TOKENS.read_text())
    registered_names = set(tokens)
    registered_hexes = {norm(v) for v in tokens.values() if v.startswith("#")}
    token_values = {k: norm(v) if v.startswith("#") else v.strip()
                    for k, v in tokens.items()}

    errors = []
    files = sorted(p for d in SCAN_DIRS for p in d.glob("*.html"))
    if not files:
        errors.append(f"no html pages found under {[str(d) for d in SCAN_DIRS]}")

    for path in files:
        text = path.read_text()
        root_block = " ".join(ROOT_BLOCK_RE.findall(strip_print_media(text)))
        local_defs = dict(DEF_RE.findall(root_block))

        for name in sorted(set(VAR_RE.findall(text))):
            if name not in local_defs:
                errors.append(
                    f"{path.name}: var({name}) used but not defined in this page's :root")

        for name, raw in local_defs.items():
            if name in registered_names:
                val = norm(raw) if raw.strip().startswith("#") else raw.strip()
                if val != token_values[name]:
                    errors.append(
                        f"{path.name}: {name} is {raw.strip()} here but {tokens[name]} in tokens.json")
            elif raw.strip().startswith("#"):
                errors.append(
                    f"{path.name}: {name} defines an unregistered color {raw.strip()}")

        checked_text = "\n".join(
            line for line in text.splitlines()
            if not any(m in line for m in AVOID_MARKERS)
        )
        for h in sorted(set(HEX_RE.findall(checked_text)), key=str.lower):
            if norm(h) not in registered_hexes:
                errors.append(f"{path.name}: {h} is not a registered token value")

    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        return 1
    print(f"OK: {len(files)} page(s), all var() refs resolve locally and all hexes are registered")
    return 0


if __name__ == "__main__":
    sys.exit(main())
