#!/usr/bin/env python3
"""Run all quality gate checks.

Runs each check script and reports overall status.
Exits non-zero if any check fails.

    python3 scripts/check_all.py
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = ROOT / "scripts"

CHECKS = [
    "check_tokens.py",
    "check_radius.py",
    "check_print.py",
    "check_motion.py",
]


def main() -> int:
    print("=" * 60)
    print("SONA QUALITY GATES")
    print("=" * 60)

    results = []

    for script in CHECKS:
        script_path = SCRIPTS_DIR / script
        if not script_path.exists():
            print(f"\n[SKIP] {script} - not found")
            continue

        print(f"\n[RUN] {script}")
        print("-" * 40)

        result = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=ROOT,
            capture_output=False
        )
        results.append((script, result.returncode))

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    failed = []
    for script, code in results:
        status = "PASS" if code == 0 else "FAIL"
        symbol = "✓" if code == 0 else "✗"
        print(f"  {symbol} {script}: {status}")
        if code != 0:
            failed.append(script)

    print()
    if failed:
        print(f"FAILED: {len(failed)} check(s) failed")
        return 1
    else:
        print(f"ALL CHECKS PASSED ({len(results)} checks)")
        return 0


if __name__ == "__main__":
    sys.exit(main())
