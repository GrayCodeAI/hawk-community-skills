---
name: ghcp-references-messenger-patterns
description: 'Skill: ghcp-references-messenger-patterns'
license: MIT
tags:
- general
---

## Multiple messengers

A common architecture is one messenger per window or per scope:

```csharp
services.AddSingleton<IMessenger>(WeakReferenceMessenger.Default);  // app-wide
services.AddScoped<WindowScopedMessenger>();                        // per-window
```

Inject the appropriate `IMessenger` into the ViewModel constructor:

```csharp
public sealed partial class WindowViewModel(IMessenger messenger)
    : ObservableRecipient(messenger) { /* ... */ }
```

This isolates broadcasts to a single window — useful for multi-window
desktop apps (WinUI 3, WPF, MAUI desktop, Avalonia).
