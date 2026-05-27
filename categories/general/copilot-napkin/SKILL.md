---
name: copilot-napkin
description: Visual whiteboard collaboration for Copilot CLI. Creates an interactive
  whiteboard that opens in your browser — draw, sketch, add sticky notes, then share
  everything back with Copilot. Copilot sees...
license: MIT
tags:
- general
---

## Important Notes

- The PNG interpretation is the **primary** channel. Multimodal models can read and interpret the base64 image data returned by the `view` tool.
- The JSON clipboard data is **supplementary** — it provides precise text but does not capture freehand drawings.
- Always check for the PNG first. If it isn't found, prompt the user to click "Share with Copilot."
- If the clipboard doesn't have JSON data, proceed with the PNG alone.
- The HTML template is located at `assets/napkin.html` relative to this SKILL.md file.
- If the noob-mode skill is also active, use its risk indicator format (green/yellow/red) when requesting file or bash permissions.
