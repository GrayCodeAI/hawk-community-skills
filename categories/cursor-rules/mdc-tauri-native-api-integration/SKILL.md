---
name: mdc-tauri-native-api-integration
description: "Rules for integrating Tauri's native APIs in the frontend application."
license: MIT
tags: [cursor-rules]
---

- Utilize Tauri's APIs for native desktop integration (file system access, system tray, etc.).
- Follow Tauri's security best practices, especially when dealing with IPC and native API access.
- Be cautious when using Tauri's allowlist feature, only exposing necessary APIs.