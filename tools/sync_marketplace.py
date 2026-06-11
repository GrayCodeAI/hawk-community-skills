#!/usr/bin/env python3
"""Generate marketplace.json skills array from categories/ directory."""

import json
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
CATEGORIES_DIR = REPO_ROOT / "categories"
MARKETPLACE = REPO_ROOT / ".claude-plugin" / "marketplace.json"

# Add tools directory to path for shared imports
sys.path.insert(0, str(Path(__file__).resolve().parent))
from frontmatter import parse_frontmatter_dict  # noqa: E402


def extract_frontmatter(skill_md: Path) -> dict[str, Any]:
    """Extract YAML frontmatter from a skill markdown file."""
    content = skill_md.read_text(encoding="utf-8", errors="ignore")
    fm = parse_frontmatter_dict(content)
    return fm if fm else {}


def build_skills() -> list[dict[str, str]]:
    """Scan categories/ and return the marketplace skills array."""
    skills = []
    for cat in sorted(CATEGORIES_DIR.iterdir()):
        if not cat.is_dir():
            continue
        for skill_dir in sorted(cat.iterdir()):
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                continue
            try:
                fm = extract_frontmatter(skill_md)
            except (UnicodeDecodeError, OSError) as exc:
                print(
                    f"⚠ Skipping unreadable skill {skill_md.relative_to(REPO_ROOT)}: {exc}",
                    file=sys.stderr,
                )
                continue
            fm_name = fm.get("name")
            if fm_name and fm_name != skill_dir.name:
                print(
                    f"⚠ {skill_md.relative_to(REPO_ROOT)}: frontmatter name "
                    f"'{fm_name}' does not match directory name "
                    f"'{skill_dir.name}'; using directory name",
                    file=sys.stderr,
                )
            # Prefer the directory name: it is the canonical skill ID
            # (validate_skill.py errors when frontmatter name differs).
            name = skill_dir.name
            invoke = fm.get("invoke", f"/hawk:{name}")
            skills.append(
                {
                    "name": name,
                    "path": str(skill_dir.relative_to(REPO_ROOT)),
                    "invoke": invoke,
                }
            )
    return skills


def render(skills: list[dict[str, str]]) -> str:
    """Return the marketplace.json text with skills populated."""
    try:
        raw = MARKETPLACE.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise SystemExit(
            f"✗ Marketplace template not found: {MARKETPLACE.relative_to(REPO_ROOT)}"
        ) from None
    except OSError as exc:
        raise SystemExit(
            f"✗ Cannot read {MARKETPLACE.relative_to(REPO_ROOT)}: {exc}"
        ) from None
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise SystemExit(
            f"✗ {MARKETPLACE.relative_to(REPO_ROOT)} is not valid JSON: {exc}"
        ) from None

    plugins = data.get("plugins") if isinstance(data, dict) else None
    if (
        not isinstance(plugins, list)
        or not plugins
        or not isinstance(plugins[0], dict)
    ):
        raise SystemExit(
            f"✗ {MARKETPLACE.relative_to(REPO_ROOT)} has unexpected structure: "
            "expected a top-level object with a non-empty 'plugins' array of objects"
        )
    plugins[0]["skills"] = skills
    return json.dumps(data, indent=2) + "\n"


def main() -> None:
    check_only = "--check" in sys.argv[1:]
    skills = build_skills()
    rendered = render(skills)

    if check_only:
        current = MARKETPLACE.read_text() if MARKETPLACE.exists() else ""
        if current != rendered:
            print(
                f"✗ marketplace.json is out of sync with categories/ "
                f"({len(skills)} skills). Run: python3 tools/sync_marketplace.py"
            )
            sys.exit(1)
        print(f"✓ marketplace.json in sync ({len(skills)} skills)")
        return

    MARKETPLACE.write_text(rendered)
    print(f"✓ Synced {len(skills)} skills to marketplace.json")


if __name__ == "__main__":
    main()
