#!/usr/bin/env python3
"""Package a skill directory into a distributable .tar.gz archive."""

import hashlib
import json
import os
import subprocess
import sys
import tarfile
import tempfile
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
    from rich.console import Console
except ImportError:
    print("Missing dependencies. Install with: pip install -r tools/requirements.txt")
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parent.parent
DIST_DIR = REPO_ROOT / "dist"

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


def validate_before_package(skill_path: Path) -> bool:
    """Run validate_skill internally before packaging."""
    validate_script = Path(__file__).parent / "validate_skill.py"
    result = subprocess.run(
        [sys.executable, str(validate_script), str(skill_path)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        console.print(f"[red]Validation failed:[/red]")
        console.print(result.stdout)
        if result.stderr:
            console.print(result.stderr)
        return False
    return True


def compute_checksum(filepath: Path) -> str:
    """Compute SHA256 checksum of a file."""
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Package a skill into a .tar.gz archive")
    parser.add_argument("path", help="Path to the skill directory")
    parser.add_argument("--skip-validate", action="store_true", help="Skip validation step")
    parser.add_argument("--output-dir", type=str, default=None, help="Output directory (default: dist/)")
    args = parser.parse_args()

    skill_path = Path(args.path).resolve()

    if not skill_path.is_dir():
        console.print(f"[red]Not a directory: {args.path}[/red]")
        sys.exit(1)

    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        console.print(f"[red]No SKILL.md found in {args.path}[/red]")
        sys.exit(1)

    # Validate
    if not args.skip_validate:
        console.print("[dim]Validating skill...[/dim]")
        if not validate_before_package(skill_path):
            console.print("[red]Fix validation errors before packaging.[/red]")
            sys.exit(1)
        console.print("[green]Validation passed.[/green]")

    # Read frontmatter for metadata
    content = skill_md.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(content) or {}
    skill_name = frontmatter.get("name", skill_path.name)
    version = frontmatter.get("version", "1.0")

    # Prepare output
    output_dir = Path(args.output_dir) if args.output_dir else DIST_DIR
    output_dir.mkdir(parents=True, exist_ok=True)

    archive_name = f"{skill_name}-{version}.tar.gz"
    archive_path = output_dir / archive_name

    # Create archive
    console.print(f"[dim]Packaging {skill_name} v{version}...[/dim]")
    with tarfile.open(archive_path, "w:gz") as tar:
        for dirpath, dirnames, filenames in os.walk(skill_path):
            for filename in filenames:
                filepath = Path(dirpath) / filename
                arcname = f"{skill_name}/{filepath.relative_to(skill_path)}"
                tar.add(filepath, arcname=arcname)

    # Compute checksum
    checksum = compute_checksum(archive_path)

    # Write metadata
    metadata = {
        "name": skill_name,
        "version": version,
        "packaged_at": datetime.now(timezone.utc).isoformat(),
        "archive": archive_name,
        "sha256": checksum,
        "file_count": sum(len(files) for _, _, files in os.walk(skill_path)),
    }

    meta_path = output_dir / f"{skill_name}-{version}.meta.json"
    meta_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")

    console.print()
    console.print(f"[bold green]Package created successfully![/bold green]")
    console.print(f"  Archive: [cyan]{archive_path.relative_to(REPO_ROOT)}[/cyan]")
    console.print(f"  Metadata: [cyan]{meta_path.relative_to(REPO_ROOT)}[/cyan]")
    console.print(f"  SHA256: [dim]{checksum}[/dim]")
    console.print(f"  Files: {metadata['file_count']}")


if __name__ == "__main__":
    main()
