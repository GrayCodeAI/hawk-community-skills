#!/usr/bin/env python3
"""Regenerate registry.json from all skill directories."""

import json
import os
import sys
from pathlib import Path

try:
    from rich.console import Console
except ImportError:
    print("Missing dependencies. Install with: pip install -r tools/requirements.txt")
    sys.exit(1)

# Add tools directory to path for shared imports
sys.path.insert(0, str(Path(__file__).resolve().parent))
from frontmatter import parse_frontmatter
from registry_schema import validate_registry_entry

REPO_ROOT = Path(__file__).resolve().parent.parent
CATEGORIES_DIR = REPO_ROOT / "categories"
REGISTRY_PATH = REPO_ROOT / "registry.json"

console = Console()


# parse_frontmatter is now imported from frontmatter module


def count_files(path: Path) -> int:
    """Count files in a directory recursively."""
    return sum(len(files) for _, _, files in os.walk(path))


def has_scripts_dir(path: Path) -> bool:
    """Check if skill has a scripts/ directory with files."""
    scripts_dir = path / "scripts"
    if not scripts_dir.exists():
        return False
    return any(scripts_dir.iterdir())


def build_registry() -> tuple[list[dict], list[tuple[str, str, str]]]:
    """Walk all categories and build registry entries.

    Returns (entries, duplicates) where duplicates is a list of
    (name, winning_path, losing_path) tuples for skipped duplicate names.
    """
    entries = []
    seen_names: dict[str, str] = {}  # name -> path that won
    duplicates: list[tuple[str, str, str]] = []

    if not CATEGORIES_DIR.exists():
        console.print("[yellow]No categories/ directory found[/yellow]")
        return entries, duplicates

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
            except (UnicodeDecodeError, OSError) as exc:
                print(
                    f"⚠ Skipping unreadable skill "
                    f"{skill_md.relative_to(REPO_ROOT)}: {exc}",
                    file=sys.stderr,
                )
                continue
            frontmatter, _ = parse_frontmatter(content)

            if frontmatter is None:
                continue

            # Build entry. Prefer the directory name as the canonical skill ID
            # (validate_skill.py errors when frontmatter name differs), but
            # warn on mismatch so drift is visible.
            fm_name = frontmatter.get("name")
            if fm_name and fm_name != skill_dir.name:
                print(
                    f"⚠ {skill_md.relative_to(REPO_ROOT)}: frontmatter name "
                    f"'{fm_name}' does not match directory name "
                    f"'{skill_dir.name}'; using directory name",
                    file=sys.stderr,
                )
            name = skill_dir.name
            description = frontmatter.get("description", "")
            # Truncate multi-line descriptions for registry
            if isinstance(description, str):
                description = " ".join(description.split())[:200]

            tags = frontmatter.get("tags", [])
            if isinstance(tags, str):
                tags = [t.strip() for t in tags.split(",") if t.strip()]
            # Generate a default tag from category if tags are empty
            if not tags:
                tags = [category_name.lower().replace(" ", "-")]

            path = f"categories/{category_name}/{skill_dir.name}"

            # Skip duplicate names (keep first occurrence), but record them
            if name in seen_names:
                duplicates.append((name, seen_names[name], path))
                continue
            seen_names[name] = path

            entry = {
                "name": name,
                "description": description,
                "category": category_name,
                "tags": tags,
                "path": path,
                "file_count": count_files(skill_dir),
                "has_scripts": has_scripts_dir(skill_dir),
            }
            entries.append(entry)

    # Sort alphabetically by name
    entries.sort(key=lambda e: e["name"].lower())
    return entries, duplicates


def report_duplicates(duplicates: list[tuple[str, str, str]]) -> None:
    """Print a summary of duplicate skill names to stderr."""
    if not duplicates:
        return
    print(
        f"⚠ {len(duplicates)} duplicate skill name(s) skipped "
        "(first occurrence wins):",
        file=sys.stderr,
    )
    for name, won, lost in duplicates:
        print(f"  - '{name}': kept {won}, skipped {lost}", file=sys.stderr)


def validate_entries(entries: list[dict]) -> list[str]:
    """Validate each registry entry against the schema.

    Returns a list of human-readable violation strings (empty when valid).
    """
    violations: list[str] = []
    for entry in entries:
        label = entry.get("path") or entry.get("name") or "<unknown entry>"
        for err in validate_registry_entry(entry, path=str(label)):
            violations.append(f"{err.path}: {err.message}")
    return violations


def main():
    console.print("[dim]Scanning categories for skills...[/dim]")
    entries, duplicates = build_registry()

    if not entries:
        console.print("[yellow]No valid skills found.[/yellow]")
        sys.exit(0)

    # Enforce the registry schema before writing anything
    violations = validate_entries(entries)
    if violations:
        console.print(
            f"[bold red]Schema validation failed "
            f"({len(violations)} violation(s)); registry.json not written:[/bold red]"
        )
        for v in violations:
            print(f"  - {v}", file=sys.stderr)
        sys.exit(1)

    # Write registry
    REGISTRY_PATH.write_text(
        json.dumps(entries, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    console.print("[bold green]Registry updated![/bold green]")
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

    report_duplicates(duplicates)


if __name__ == "__main__":
    main()
