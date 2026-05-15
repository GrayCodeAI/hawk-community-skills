#!/usr/bin/env python3
"""Ensure no skill uses ../ parent references — skills must be portable."""
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CATEGORIES_DIR = REPO_ROOT / "categories"

def main():
    violations = []
    for cat in sorted(CATEGORIES_DIR.iterdir()):
        if not cat.is_dir():
            continue
        for skill_dir in sorted(cat.iterdir()):
            if not skill_dir.is_dir():
                continue
            for f in skill_dir.rglob("*.md"):
                content = f.read_text(encoding="utf-8", errors="ignore")
                if "../" in content:
                    violations.append(str(f.relative_to(REPO_ROOT)))

    if violations:
        print(f"✗ {len(violations)} file(s) contain '../' references:")
        for v in violations:
            print(f"  - {v}")
        sys.exit(1)
    print("✓ All skills are self-contained")

if __name__ == "__main__":
    main()
