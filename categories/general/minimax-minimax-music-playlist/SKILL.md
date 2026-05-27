---
name: minimax-minimax-music-playlist
description: 'Skill: minimax-minimax-music-playlist'
license: MIT
tags:
- general
metadata: None
version: 2.0
category: creative
---

## Notes

- **Agent vs user invocation**: The theme/scene question (Step 3) is the single
  interactive touchpoint. If the theme is already provided in the invocation,
  skip the question. Everything else runs autonomously.
- **No hardcoded scripts**: Write scanning/analysis scripts on the fly as needed.
  Use Python stdlib only. Cache results to avoid redundant work.
- **Skill directory**: `<SKILL_DIR>` = the directory containing this SKILL.md file.
  Data/cache files go in `<SKILL_DIR>/data/`.
- **All mmx prompts in English** for best generation quality.
