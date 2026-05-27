---
name: ag-avalonia-layout-zafiro
description: Guidelines for modern Avalonia UI layout using Zafiro.Avalonia, emphasizing
  shared styles, generic components, and avoiding XAML redundancy.
license: MIT
tags:
- general
risk: unknown
source: community
date_added: 2026-02-27
---

## ❌ Anti-Patterns

**DON'T:**
- Use hardcoded colors or sizes (literals) in views.
- Create deep nesting of `Grid` and `StackPanel`.
- Repeat visual properties across multiple elements (use Styles).
- Use `IValueConverter` for simple logic that belongs in the ViewModel.

**DO:**
- Use `DynamicResource` for colors and brushes.
- Extract repeated layouts into generic components.
- Leverage `Zafiro.Avalonia` specific panels like `EdgePanel` for common UI patterns.

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
