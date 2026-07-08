#!/usr/bin/env python3
"""Shared list of plugin manifests that carry a copy of VERSION.

Single source of truth for bump_version.py and check_version_sync.py so the
two scripts can't drift out of sync with each other.
"""

# (repo-relative path, dotted/indexed JSON path to the version field)
MANIFEST_VERSION_PATHS: list[tuple[str, str]] = [
    (".claude-plugin/plugin.json", "version"),
    (".claude-plugin/marketplace.json", "plugins[0].version"),
    (".codex-plugin/plugin.json", "version"),
    (".cursor-plugin/plugin.json", "version"),
]

# Plain list of manifest paths, for callers that only need the paths.
MANIFEST_PATHS: list[str] = [path for path, _ in MANIFEST_VERSION_PATHS]
