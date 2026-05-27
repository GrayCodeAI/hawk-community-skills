---
name: ag-electron-development
description: Master Electron desktop app development with secure IPC, contextIsolation,
  preload scripts, multi-process architecture, electron-builder packaging, code signing,
  and auto-update.
license: MIT
tags:
- general
risk: safe
source: community
date_added: 2026-03-12
---

## Best Practices

- ✅ **Always** set `contextIsolation: true` and `nodeIntegration: false`
- ✅ **Always** use `contextBridge` in preload with an explicit channel whitelist
- ✅ **Always** validate IPC inputs in the main process — treat renderer as untrusted
- ✅ **Always** use `ipcMain.handle()` / `ipcRenderer.invoke()` for request/response IPC
- ✅ **Always** configure Content Security Policy headers
- ✅ **Always** sanitize URLs before passing to `shell.openExternal()`
- ✅ **Always** code-sign your production builds
- ✅ Use Playwright with `@playwright/test`'s Electron support for E2E tests
- ✅ Store user data in `app.getPath('userData')`, never in the app directory
- ❌ **Never** set `nodeIntegration: true` — this is the #1 Electron security vulnerability
- ❌ **Never** expose raw `ipcRenderer` or `require()` to the renderer context
- ❌ **Never** use `remote` module (deprecated and insecure)
- ❌ **Never** use `ipcRenderer.sendSync()` — it blocks the renderer event loop
- ❌ **Never** disable `webSecurity` in production
- ❌ **Never** load remote/untrusted content without a strict CSP and sandboxing

## Limitations

- Electron bundles Chromium + Node.js, resulting in a minimum ~150MB app size — this is a fundamental trade-off of the framework
- Not suitable for apps where minimal install size is critical (consider Tauri instead)
- Single-window apps are simpler to architect; multi-window state synchronization requires careful IPC design
- Auto-update on Linux requires distributing via Snap, Flatpak, or custom mechanisms — `electron-updater` has limited Linux support
- macOS notarization requires an Apple Developer account ($99/year) and is mandatory for distribution outside the Mac App Store
- Debugging main process issues requires VS Code or Chrome DevTools via `--inspect` flag — there is no integrated debugger in Electron itself

## Related Skills

- `chrome-extension-developer` — When building browser extensions instead of desktop apps (shares multi-process model concepts)
- `docker-expert` — When containerizing Electron's build pipeline or CI/CD
- `react-patterns` / `react-best-practices` — When using React for the renderer UI
- `typescript-pro` — When setting up advanced TypeScript configurations for multi-target builds
- `nodejs-backend-patterns` — When the main process needs complex backend logic
- `github-actions-templates` — When setting up CI/CD for cross-platform Electron builds
