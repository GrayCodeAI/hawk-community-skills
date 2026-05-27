---
name: mdc-windows-compatibility
description: "Specifies guidelines for Windows compatibility, including providing PowerShell commands and avoiding Unix-specific commands. This rule ensures cross-platform compatibility for Windows users."
license: MIT
tags: [cursor-rules]
---

- |-
  12. Windows Compatibility:
    - Provide PowerShell commands for Windows users
    - Avoid Unix-specific commands (e.g., use `Remove-Item` instead of `rm`)
    - Use cross-platform Node.js commands when possible