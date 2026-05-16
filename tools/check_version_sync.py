#!/usr/bin/env python3
"""Check that VERSION file matches all plugin manifests."""
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
VERSION_FILE = REPO_ROOT / "VERSION"

MANIFEST_PATHS = [
    (".claude-plugin/plugin.json", "version"),
    (".claude-plugin/marketplace.json", "plugins[0].version"),
    (".codex-plugin/plugin.json", "version"),
    (".cursor-plugin/plugin.json", "version"),
]

def get_nested(data, path):
    for part in path.split("."):
        if "[" in part:
            key, idx = part.split("[")
            idx = int(idx.rstrip("]"))
            data = data[key][idx]
        else:
            data = data[part]
    return data

def main():
    if not VERSION_FILE.exists():
        print("✗ VERSION file not found")
        sys.exit(1)

    version = VERSION_FILE.read_text().strip()
    errors = []

    for rel_path, json_path in MANIFEST_PATHS:
        full_path = REPO_ROOT / rel_path
        if not full_path.exists():
            continue
        try:
            data = json.loads(full_path.read_text())
            manifest_version = get_nested(data, json_path)
            if manifest_version != version:
                errors.append(f"{rel_path}: {manifest_version} (expected {version})")
        except (json.JSONDecodeError, KeyError, IndexError) as e:
            errors.append(f"{rel_path}: parse error: {e}")

    if errors:
        print(f"✗ Version mismatch (VERSION = {version}):")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    print(f"✓ All manifests match VERSION ({version})")

if __name__ == "__main__":
    main()
