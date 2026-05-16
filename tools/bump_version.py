#!/usr/bin/env python3
"""Bump VERSION and propagate to all plugin manifests."""
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
VERSION_FILE = REPO_ROOT / "VERSION"

MANIFEST_PATHS = [
    ".claude-plugin/plugin.json",
    ".claude-plugin/marketplace.json",
    ".codex-plugin/plugin.json",
    ".cursor-plugin/plugin.json",
]

def bump(version, part):
    major, minor, patch = [int(x) for x in version.split(".")]
    if part == "major":
        return f"{major+1}.0.0"
    elif part == "minor":
        return f"{major}.{minor+1}.0"
    else:
        return f"{major}.{minor}.{patch+1}"

def update_json_version(path, new_version):
    if not path.exists():
        return
    data = json.loads(path.read_text())
    if "version" in data:
        data["version"] = new_version
    if "plugins" in data and len(data["plugins"]) > 0:
        data["plugins"][0]["version"] = new_version
    path.write_text(json.dumps(data, indent=2) + "\n")

def main():
    if len(sys.argv) < 2:
        print("Usage: bump_version.py [major|minor|patch|<version>]")
        sys.exit(1)

    current = VERSION_FILE.read_text().strip() if VERSION_FILE.exists() else "0.0.0"
    arg = sys.argv[1]

    if arg in ("major", "minor", "patch"):
        new_version = bump(current, arg)
    else:
        new_version = arg

    VERSION_FILE.write_text(new_version + "\n")

    for rel in MANIFEST_PATHS:
        update_json_version(REPO_ROOT / rel, new_version)

    print(f"✓ Bumped {current} → {new_version}")

if __name__ == "__main__":
    main()
