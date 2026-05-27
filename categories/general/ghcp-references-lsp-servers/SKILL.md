---
name: ghcp-references-lsp-servers
description: 'Skill: ghcp-references-lsp-servers'
license: MIT
tags:
- general
---

## Bash / Shell

**Server**: [bash-language-server](https://github.com/bash-lsp/bash-language-server)

### Install

| OS      | Command                                       |
|---------|-----------------------------------------------|
| Any     | `npm install -g bash-language-server`         |

### Config snippet

```json
{
  "bash": {
    "command": "bash-language-server",
    "args": ["start"],
    "fileExtensions": {
      ".sh": "shellscript",
      ".bash": "shellscript",
      ".zsh": "shellscript"
    }
  }
}
```
