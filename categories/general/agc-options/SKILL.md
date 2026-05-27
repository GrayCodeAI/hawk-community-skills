---
name: agc-options
description: 'Skill: agc-options'
license: MIT
tags:
- general
---

## Colour Format Reference

All colour options accept:
- `#RRGGBB` - Hex with hash
- `RRGGBB` - Hex without hash
- X11 colour names (e.g., `red`, `steelblue`, `coral`)
- Special values for cursor/selection: `cell-foreground`, `cell-background`

## Duration Format Reference

Duration options accept combinations of:
- `y` (years), `d` (days), `h` (hours), `m` (minutes)
- `s` (seconds), `ms` (milliseconds), `us`/`µs` (microseconds), `ns` (nanoseconds)

Examples: `1h30m`, `45s`, `100ms`, `750ms`

## Full Ghostty configuration schema reference

You can find the latest Ghostty configuration schema (including those supported by the tip releases) at: https://raw.githubusercontent.com/sammcj/vscode-ghostty-config-syntax/refs/heads/main/schema/ghostty-config-syntax.schema.json - this can be quite large, so it's best to pass it programmatically to avoid having to read it in full.
