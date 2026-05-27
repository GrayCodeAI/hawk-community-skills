---
name: ghcp-references-source-generators
description: 'Skill: ghcp-references-source-generators'
license: MIT
tags:
- general
---

## `[INotifyPropertyChanged]` (class-level)

Use only when you can't inherit from `ObservableObject` (e.g., the type
already inherits from a different base). Generates the
`INotifyPropertyChanged` plumbing on the type itself.

```csharp
using CommunityToolkit.Mvvm.ComponentModel;

[INotifyPropertyChanged]
public partial class MyControl : UserControl
{
    [ObservableProperty]
    private string? caption;
}
```

Prefer `ObservableObject` (or `ObservableValidator` /
`ObservableRecipient`) inheritance whenever possible. The class-level
attribute exists primarily for inheritance-locked scenarios such as
custom controls and platform base types.

There is also `[ObservableObject]` (class-level) for the same purpose if
you want the full `SetProperty<T>` API surface generated onto the type
without inheritance.
