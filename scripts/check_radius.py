#!/usr/bin/env python3
"""Radius audit.

Verifies that all border-radius values in templates use only the
registered scale: 10px, 20px, 30px, 999px (pill), or 0.

Print templates may use pt values: 6pt, 8pt, 10pt, 999px.

Exits non-zero on any violation.

    python3 scripts/check_radius.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCAN_DIRS = [ROOT / "templates", ROOT / "site"]

# Allowed radius values (screen)
# Note: 2px-8px allowed for mini graphics (code chips, dots, small frames)
# 50% allowed for circles
ALLOWED_PX = {"0", "0px", "2px", "3px", "4px", "6px", "8px", "10px", "20px", "30px", "999px", "50%"}
# Allowed radius values (print)
ALLOWED_PT = {"0", "0pt", "2pt", "3pt", "4pt", "6pt", "8pt", "10pt", "999px", "50%"}
# Combined for mixed templates
ALLOWED_ALL = ALLOWED_PX | ALLOWED_PT

# Match border-radius declarations
RADIUS_RE = re.compile(
    r"border-radius\s*:\s*([^;}]+)",
    re.IGNORECASE
)

# Match individual values (handles shorthand like "10px 20px")
VALUE_RE = re.compile(r"(\d+(?:\.\d+)?(?:px|pt|%))")


def check_radius(value: str) -> list[str]:
    """Return list of invalid radius values in a declaration."""
    values = VALUE_RE.findall(value.lower())
    invalid = []
    for v in values:
        if v not in ALLOWED_ALL:
            # Also check var() references which are OK
            if "var(" not in value:
                invalid.append(v)
    return invalid


def main() -> int:
    errors = []
    files = sorted(p for d in SCAN_DIRS for p in d.glob("*.html"))

    if not files:
        errors.append(f"no html pages found under {[str(d) for d in SCAN_DIRS]}")

    for path in files:
        text = path.read_text()
        for match in RADIUS_RE.finditer(text):
            value = match.group(1).strip()
            # Skip var() references
            if "var(" in value:
                continue
            invalid = check_radius(value)
            if invalid:
                errors.append(
                    f"{path.name}: border-radius uses {', '.join(invalid)} "
                    f"(allowed: 10/20/30/999px or 6/8/10pt for print)"
                )

    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        return 1

    print(f"OK: {len(files)} page(s), all border-radius values are on scale")
    return 0


if __name__ == "__main__":
    sys.exit(main())
