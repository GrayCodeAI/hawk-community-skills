---
name: ghcp-winui3-migration-guide-skill
description: UWP-to-WinUI 3 migration reference. Maps legacy UWP APIs to correct Windows
  App SDK equivalents with before/after code snippets. Covers namespace changes, threading
  (CoreDispatcher to DispatcherQue...
license: MIT
tags:
- general
---

## Migration Checklist

1. [ ] Replace all `Windows.UI.Xaml.*` using directives with `Microsoft.UI.Xaml.*`
2. [ ] Replace `Windows.UI.Colors` with `Microsoft.UI.Colors`
3. [ ] Replace `CoreDispatcher.RunAsync` with `DispatcherQueue.TryEnqueue`
4. [ ] Replace `Window.Current` with `App.MainWindow` static property
5. [ ] Add `XamlRoot` to all `ContentDialog` instances
6. [ ] Initialize all pickers with `InitializeWithWindow.Initialize(picker, hwnd)`
7. [ ] Replace `MessageDialog` with `ContentDialog`
8. [ ] Replace `ApplicationView`/`CoreWindow` with `AppWindow`
9. [ ] Replace `CoreApplicationViewTitleBar` with `AppWindowTitleBar`
10. [ ] Replace all `GetForCurrentView()` calls with `AppWindow` equivalents
11. [ ] Update interop for Share and Print managers
12. [ ] Replace `IBackgroundTask` with `AppLifecycle` activation
13. [ ] Update project file: TFM to `net10.0-windows10.0.22621.0`, add `<UseWinUI>true</UseWinUI>`
14. [ ] Migrate unit tests to **Unit Test App (WinUI in Desktop)** project; use `[UITestMethod]` for XAML tests
15. [ ] Test both packaged and unpackaged configurations
