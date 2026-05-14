#!/usr/bin/env python3
"""Regenerate registry.json from all skill directories."""

import json
import os
import sys
from pathlib import Path

try:
    import yaml
    from rich.console import Console
except ImportError:
    print("Missing dependencies. Install with: pip install -r tools/requirements.txt")
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parent.parent
CATEGORIES_DIR = REPO_ROOT / "categories"
REGISTRY_PATH = REPO_ROOT / "registry.json"

console = Console()


def parse_frontmatter(content: str) -> dict | None:
    """Extract YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return None
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None
    try:
        fm = yaml.safe_load(parts[1])
        return fm if isinstance(fm, dict) else None
    except yaml.YAMLError:
        return None


def count_files(path: Path) -> int:
    """Count files in a directory recursively."""
    return sum(len(files) for _, _, files in os.walk(path))


def has_scripts_dir(path: Path) -> bool:
    """Check if skill has a scripts/ directory with files."""
    scripts_dir = path / "scripts"
    if not scripts_dir.exists():
        return False
    return any(scripts_dir.iterdir())


def build_registry() -> list[dict]:
    """Walk all categories and build registry entries."""
    entries = []

    if not CATEGORIES_DIR.exists():
        console.print("[yellow]No categories/ directory found[/yellow]")
        return entries

    for category_dir in sorted(CATEGORIES_DIR.iterdir()):
        if not category_dir.is_dir():
            continue
        category_name = category_dir.name

        for skill_dir in sorted(category_dir.iterdir()):
            if not skill_dir.is_dir():
                continue

            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                continue

            try:
                content = skill_md.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                continue
            frontmatter = parse_frontmatter(content)

            if frontmatter is None:
                continue

            # Build entry
            name = frontmatter.get("name", skill_dir.name)
            description = frontmatter.get("description", "")
            # Truncate multi-line descriptions for registry
            if isinstance(description, str):
                description = " ".join(description.split())[:200]

            tags = frontmatter.get("tags", [])
            if isinstance(tags, str):
                tags = [t.strip() for t in tags.split(",")]

            entry = {
                "name": name,
                "description": description,
                "category": category_name,
                "tags": tags,
                "path": f"categories/{category_name}/{skill_dir.name}",
                "file_count": count_files(skill_dir),
                "has_scripts": has_scripts_dir(skill_dir),
            }
            entries.append(entry)

    # Sort alphabetically by name
    entries.sort(key=lambda e: e["name"].lower())
    return entries


def main():
    console.print("[dim]Scanning categories for skills...[/dim]")
    entries = build_registry()

    if not entries:
        console.print("[yellow]No valid skills found.[/yellow]")
        sys.exit(0)

    # Write registry
    REGISTRY_PATH.write_text(
        json.dumps(entries, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    console.print(f"[bold green]Registry updated![/bold green]")
    console.print(f"  Skills indexed: [cyan]{len(entries)}[/cyan]")
    console.print(f"  Output: [cyan]{REGISTRY_PATH.relative_to(REPO_ROOT)}[/cyan]")

    # Summary by category
    categories = {}
    for entry in entries:
        cat = entry["category"]
        categories[cat] = categories.get(cat, 0) + 1
    console.print("\n[bold]By category:[/bold]")
    for cat in sorted(categories):
        console.print(f"  {cat}: {categories[cat]}")


if __name__ == "__main__":
    main()
