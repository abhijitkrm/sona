#!/usr/bin/env python3
"""Print alpha audit.

Verifies that @media print blocks contain no alpha values:
- No rgba() functions
- No 8-digit hex colors (#rrggbbaa)
- No 4-digit hex colors (#rgba shorthand)

WeasyPrint renders alpha fills as double rectangles; all print colors
must be solid hexes.

Exits non-zero on any violation.

    python3 scripts/check_print.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCAN_DIRS = [ROOT / "templates", ROOT / "site"]

# Match @media print blocks
PRINT_BLOCK_RE = re.compile(r"@media\s+print\s*\{", re.IGNORECASE)

# Alpha patterns
RGBA_RE = re.compile(r"rgba\s*\([^)]+\)", re.IGNORECASE)
HSLA_RE = re.compile(r"hsla\s*\([^)]+\)", re.IGNORECASE)
HEX8_RE = re.compile(r"#[0-9a-fA-F]{8}\b")  # #rrggbbaa
HEX4_RE = re.compile(r"#[0-9a-fA-F]{4}\b")  # #rgba


def extract_print_blocks(text: str) -> list[str]:
    """Extract all @media print block contents."""
    blocks = []
    i = 0
    while True:
        match = PRINT_BLOCK_RE.search(text, i)
        if not match:
            break
        start = match.end()
        depth = 1
        j = start
        while j < len(text) and depth > 0:
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
            j += 1
        blocks.append(text[start:j-1])
        i = j
    return blocks


def check_alpha(block: str, filename: str) -> list[str]:
    """Return list of alpha violations in a print block."""
    errors = []

    for match in RGBA_RE.finditer(block):
        errors.append(f"{filename}: rgba() in @media print: {match.group()}")

    for match in HSLA_RE.finditer(block):
        errors.append(f"{filename}: hsla() in @media print: {match.group()}")

    for match in HEX8_RE.finditer(block):
        errors.append(f"{filename}: 8-digit hex in @media print: {match.group()}")

    for match in HEX4_RE.finditer(block):
        # Distinguish from 3-digit hex by checking it's not part of longer hex
        errors.append(f"{filename}: 4-digit hex (alpha) in @media print: {match.group()}")

    return errors


def main() -> int:
    errors = []
    files = sorted(p for d in SCAN_DIRS for p in d.glob("*.html"))

    if not files:
        errors.append(f"no html pages found under {[str(d) for d in SCAN_DIRS]}")

    for path in files:
        text = path.read_text()
        blocks = extract_print_blocks(text)
        for block in blocks:
            errors.extend(check_alpha(block, path.name))

    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        return 1

    print(f"OK: {len(files)} page(s), no alpha values in print blocks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
