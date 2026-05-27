---
name: copilot-winmd-api-search
description: Find and explore Windows desktop APIs. Use when building features that
  need platform capabilities — camera, file access, notifications, UI controls, AI/ML,
  sensors, networking, etc. Discovers the r...
license: Complete terms in LICENSE.txt
tags:
- general
---

### Other Commands

```powershell
# List cached projects
.\.github\skills\winmd-api-search\scripts\Invoke-WinMdQuery.ps1 -Action projects

# List packages for a project
.\.github\skills\winmd-api-search\scripts\Invoke-WinMdQuery.ps1 -Action packages

# Show stats
.\.github\skills\winmd-api-search\scripts\Invoke-WinMdQuery.ps1 -Action stats
```

> If only one project is cached, `-Project` is auto-selected.
> If multiple projects exist, add `-Project <name>` (use `-Action projects` to see available names).
> In scan mode, manifest names include a short hash suffix to avoid collisions; you can pass the base project name without the suffix if it's unambiguous.

## Search Scoring

The search ranks type names and member names against your query:

| Score | Match type | Example |
|-------|-----------|---------|
| 100 | Exact name | `Button` → `Button` |
| 80 | Starts with | `Navigation` → `NavigationView` |
| 60 | Contains | `Dialog` → `ContentDialog` |
| 50 | PascalCase initials | `ASB` → `AutoSuggestBox` |
| 40 | Multi-keyword AND | `navigation item` → `NavigationViewItem` |
| 20 | Fuzzy character match | `NavVw` → `NavigationView` |

Results are grouped by namespace. Higher-scored namespaces appear first.

## Troubleshooting

| Issue | Fix |
|-------|-----|
| "Cache not found" | Run `Update-WinMdCache.ps1` |
| "Multiple projects cached" | Add `-Project <name>` |
| "Namespace not found" | Use `-Action namespaces` to list available ones |
| "Type not found" | Use fully qualified name (e.g., `Microsoft.UI.Xaml.Controls.Button`) |
| Stale after NuGet update | Re-run `Update-WinMdCache.ps1` |
| Cache in git history | Add `Generated Files/` to `.gitignore` |

## References

- [Windows Platform SDK API reference](https://learn.microsoft.com/uwp/api/) — documentation for `Windows.*` namespaces
- [Windows App SDK API reference](https://learn.microsoft.com/windows/windows-app-sdk/api/winrt/) — documentation for `Microsoft.*` WinAppSDK namespaces
