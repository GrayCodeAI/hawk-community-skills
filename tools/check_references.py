#!/usr/bin/env python3
"""Validate reference integrity: no orphans, no broken @ref() links."""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from skill_discovery import CATEGORIES_DIR, iter_skills

REPO_ROOT = Path(__file__).resolve().parent.parent


def main():
    errors = []
    ref_pattern = re.compile(r"@ref\(([^)]+)\)")

    for skill_dir in iter_skills(CATEGORIES_DIR):
        skill_md = skill_dir / "SKILL.md"
        content = skill_md.read_text(encoding="utf-8", errors="ignore")
        declared_refs = set(ref_pattern.findall(content))
        ref_dir = skill_dir / "references"

        if not ref_dir.exists():
            if declared_refs:
                for r in declared_refs:
                    errors.append(f"{skill_dir.name}: @ref({r}) but no references/ dir")
            continue

        actual_files = {f.name for f in ref_dir.iterdir() if f.is_file()}
        for r in declared_refs:
            if r not in actual_files:
                errors.append(f"{skill_dir.name}: broken @ref({r})")
        for f in actual_files:
            if f not in declared_refs:
                errors.append(f"{skill_dir.name}: orphaned references/{f}")

    if errors:
        print(f"✗ {len(errors)} reference issue(s):")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    print("✓ All references valid")


if __name__ == "__main__":
    main()
