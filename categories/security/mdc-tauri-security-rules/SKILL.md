---
name: mdc-tauri-security-rules
description: "Security-related rules for Tauri application development."
license: MIT
tags: [security]
---

- Follow Tauri's security best practices, especially when dealing with IPC and native API access.
- Implement proper input validation and sanitization on the frontend.
- Use HTTPS for all communications with external services.
- Implement proper authentication and authorization mechanisms if required.
- Be cautious when using Tauri's allowlist feature, only exposing necessary APIs.