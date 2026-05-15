#!/usr/bin/env python3
"""Generate marketplace.json skills array from categories/ directory."""
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CATEGORIES_DIR = REPO_ROOT / "categories"
MARKETPLACE = REPO_ROOT / ".claude-plugin" / "marketplace.json"

def extract_frontmatter(skill_md):
    content = skill_md.read_text(encoding="utf-8", errors="ignore")
    if not content.startswith("---"):
        return {}
    end = content.index("---", 3)
    fm = {}
    for line in content[3:end].strip().split("\n"):
        if ":" in line:
            key, val = line.split(":", 1)
            fm[key.strip()] = val.strip().strip('"').strip("'")
    return fm

def main():
    skills = []
    for cat in sorted(CATEGORIES_DIR.iterdir()):
        if not cat.is_dir():
            continue
        for skill_dir in sorted(cat.iterdir()):
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                continue
            fm = extract_frontmatter(skill_md)
            name = fm.get("name", skill_dir.name)
            invoke = fm.get("invoke", f"/hawk:{name}")
            skills.append({
                "name": name,
                "path": str(skill_dir.relative_to(REPO_ROOT)),
                "invoke": invoke,
            })

    data = json.loads(MARKETPLACE.read_text())
    data["plugins"][0]["skills"] = skills
    MARKETPLACE.write_text(json.dumps(data, indent=2) + "\n")
    print(f"✓ Synced {len(skills)} skills to marketplace.json")

if __name__ == "__main__":
    main()
