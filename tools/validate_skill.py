#!/usr/bin/env python3
"""Validate one or all skills against hawk-community-skills quality standards."""

import os
import re
import sys
import stat
from pathlib import Path

try:
    import yaml
    from rich.console import Console
    from rich.table import Table
except ImportError:
    print("Missing dependencies. Install with: pip install -r tools/requirements.txt")
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parent.parent
CATEGORIES_DIR = REPO_ROOT / "categories"

REQUIRED_FIELDS = {"name", "description", "license"}
MAX_DESCRIPTION_LEN = 200
MAX_FILE_SIZE = 100 * 1024  # 100KB
ASSET_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ico", ".pdf"}

console = Console()


class ValidationResult:
    def __init__(self, skill_path: Path):
        self.skill_path = skill_path
        self.errors: list[str] = []
        self.warnings: list[str] = []

    @property
    def passed(self) -> bool:
        return len(self.errors) == 0

    def error(self, msg: str):
        self.errors.append(msg)

    def warn(self, msg: str):
        self.warnings.append(msg)


def parse_frontmatter(content: str) -> tuple[dict | None, str]:
    """Extract YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return None, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, content
    try:
        fm = yaml.safe_load(parts[1])
        return fm if isinstance(fm, dict) else None, parts[2]
    except yaml.YAMLError:
        return None, content


def validate_skill(skill_path: Path) -> ValidationResult:
    """Run all validation checks on a single skill directory."""
    result = ValidationResult(skill_path)
    skill_name = skill_path.name

    # Check SKILL.md exists
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        result.error("SKILL.md not found")
        return result

    # Read and parse SKILL.md
    try:
        content = skill_md.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        result.error(f"SKILL.md is not valid UTF-8")
        return result
    frontmatter, body = parse_frontmatter(content)

    if frontmatter is None:
        result.error("SKILL.md has no valid YAML frontmatter (must start with ---)")
        return result

    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in frontmatter:
            result.error(f"Missing required frontmatter field: '{field}'")

    # Check description length
    desc = frontmatter.get("description", "")
    if isinstance(desc, str) and len(desc) > MAX_DESCRIPTION_LEN:
        result.warn(f"Description is {len(desc)} chars (max recommended: {MAX_DESCRIPTION_LEN})")

    # Check name matches directory
    fm_name = frontmatter.get("name", "")
    if fm_name and fm_name != skill_name:
        result.error(f"Frontmatter name '{fm_name}' does not match directory name '{skill_name}'")

    # Check for broken internal references (relative links in markdown)
    link_pattern = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')
    for match in link_pattern.finditer(content):
        link_text, link_target = match.groups()
        # Skip external URLs
        if link_target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        # Resolve relative path
        target_path = (skill_path / link_target).resolve()
        if not target_path.exists():
            result.warn(f"Broken internal reference: [{link_text}]({link_target})")

    # Check scripts have shebang and are executable
    scripts_dir = skill_path / "scripts"
    if scripts_dir.exists():
        for script in scripts_dir.iterdir():
            if script.is_file() and script.suffix in (".sh", ".py", ".bash"):
                # Check shebang
                first_line = script.read_text(encoding="utf-8", errors="ignore").split("\n", 1)[0]
                if not first_line.startswith("#!"):
                    result.warn(f"Script {script.name} missing shebang line")
                # Check executable bit
                mode = script.stat().st_mode
                if not (mode & stat.S_IXUSR):
                    result.warn(f"Script {script.name} is not executable (chmod +x)")

    # Also check scripts in services/ subdirectories
    for dirpath, dirnames, filenames in os.walk(skill_path):
        for filename in filenames:
            filepath = Path(dirpath) / filename
            # Check file size (except whitelisted assets)
            if filepath.stat().st_size > MAX_FILE_SIZE:
                if filepath.suffix.lower() not in ASSET_EXTENSIONS:
                    result.warn(f"File {filepath.relative_to(skill_path)} exceeds 100KB")
            # Check shell/python scripts anywhere
            if filepath.suffix in (".sh", ".bash", ".py") and filepath.parent.name in ("scripts", ""):
                pass  # Already checked above for scripts/ dir

    return result


def find_all_skills() -> list[Path]:
    """Find all skill directories under categories/."""
    skills = []
    if not CATEGORIES_DIR.exists():
        return skills
    for category_dir in sorted(CATEGORIES_DIR.iterdir()):
        if category_dir.is_dir():
            for skill_dir in sorted(category_dir.iterdir()):
                if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
                    skills.append(skill_dir)
    return skills


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Validate hawk-community-skills")
    parser.add_argument("path", nargs="?", help="Path to a specific skill directory")
    parser.add_argument("--all", action="store_true", help="Validate all skills")
    args = parser.parse_args()

    if not args.path and not args.all:
        parser.print_help()
        console.print("\n[yellow]Provide a skill path or use --all[/yellow]")
        sys.exit(1)

    if args.all:
        skills = find_all_skills()
        if not skills:
            console.print("[yellow]No skills found in categories/[/yellow]")
            sys.exit(0)
    else:
        skill_path = Path(args.path).resolve()
        if not skill_path.is_dir():
            console.print(f"[red]Not a directory: {args.path}[/red]")
            sys.exit(1)
        skills = [skill_path]

    total = len(skills)
    passed = 0
    failed = 0

    table = Table(title="Validation Results")
    table.add_column("Skill", style="cyan")
    table.add_column("Status", justify="center")
    table.add_column("Errors", style="red")
    table.add_column("Warnings", style="yellow")

    for skill_path in skills:
        result = validate_skill(skill_path)
        if result.passed:
            passed += 1
            status = "[green]PASS[/green]"
        else:
            failed += 1
            status = "[red]FAIL[/red]"

        rel_path = str(skill_path.relative_to(REPO_ROOT)) if str(skill_path).startswith(str(REPO_ROOT)) else skill_path.name
        table.add_row(
            rel_path,
            status,
            str(len(result.errors)) if result.errors else "-",
            str(len(result.warnings)) if result.warnings else "-",
        )

        # Print details for failures
        if not result.passed or result.warnings:
            for err in result.errors:
                console.print(f"  ERROR {rel_path}: {err}", markup=False)
            for warn in result.warnings:
                console.print(f"  WARN  {rel_path}: {warn}", markup=False)

    console.print()
    console.print(table)
    console.print()
    console.print(f"[bold]Total: {total} | Passed: {passed} | Failed: {failed}[/bold]")

    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
