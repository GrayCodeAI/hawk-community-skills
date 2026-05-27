---
name: minimax-minimax-multimodal-toolkit
description: Use mmx to generate text, images, video, speech, and music via the MiniMax
  AI platform. Use when the user wants to create media content, chat with MiniMax
  models, perform web search, or manage Mini...
license: MIT
tags:
- general
---

## Configuration Precedence

CLI flags → environment variables → `~/.mmx/config.json` → defaults.

```bash
# Persistent config
mmx config set --key region --value cn
mmx config show

# Environment
export MINIMAX_API_KEY=sk-xxxxx
export MINIMAX_REGION=cn
```
