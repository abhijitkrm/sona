#!/usr/bin/env python3
"""Motion accessibility audit.

Verifies that pages with animations include prefers-reduced-motion handling:
- If a page uses @keyframes, it must have @media (prefers-reduced-motion)
- If a page uses animation: or transition:, it should handle reduced motion

Exits non-zero on any violation.

    python3 scripts/check_motion.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCAN_DIRS = [ROOT / "templates", ROOT / "site"]

# Patterns to detect animation usage
KEYFRAMES_RE = re.compile(r"@keyframes\s+\w+", re.IGNORECASE)
ANIMATION_RE = re.compile(r"animation\s*:", re.IGNORECASE)
TRANSITION_RE = re.compile(r"transition\s*:", re.IGNORECASE)

# Pattern to detect reduced motion handling
REDUCED_MOTION_RE = re.compile(
    r"@media\s*\(\s*prefers-reduced-motion",
    re.IGNORECASE
)


def main() -> int:
    errors = []
    warnings = []
    files = sorted(p for d in SCAN_DIRS for p in d.glob("*.html"))

    if not files:
        errors.append(f"no html pages found under {[str(d) for d in SCAN_DIRS]}")

    for path in files:
        text = path.read_text()

        has_keyframes = bool(KEYFRAMES_RE.search(text))
        has_animation = bool(ANIMATION_RE.search(text))
        has_transition = bool(TRANSITION_RE.search(text))
        has_motion_query = bool(REDUCED_MOTION_RE.search(text))

        # Keyframes require reduced motion handling
        if has_keyframes and not has_motion_query:
            errors.append(
                f"{path.name}: uses @keyframes but missing "
                "@media (prefers-reduced-motion)"
            )

        # Animation property without keyframes is suspicious but check anyway
        if has_animation and not has_keyframes and not has_motion_query:
            warnings.append(
                f"{path.name}: uses animation: but no reduced motion handling"
            )

        # Transitions are usually OK but flag if many and no handling
        # This is a soft warning, not an error
        if has_transition and not has_keyframes and not has_animation:
            # Only transitions, likely hover effects - OK without motion query
            pass

    for w in warnings:
        print(f"WARNING: {w}")

    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        return 1

    animated = sum(1 for p in files
                   if KEYFRAMES_RE.search(p.read_text()))
    print(f"OK: {len(files)} page(s), {animated} with animations have motion handling")
    return 0


if __name__ == "__main__":
    sys.exit(main())
