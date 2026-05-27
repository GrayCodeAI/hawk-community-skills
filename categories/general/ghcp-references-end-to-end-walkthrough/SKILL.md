---
name: ghcp-references-end-to-end-walkthrough
description: 'Skill: ghcp-references-end-to-end-walkthrough'
license: MIT
tags:
- general
---

## What to internalize from this sample

1. **VMs go in a UI-free class library.** The toolkit's only dependency
   is `netstandard2.0+`, so VMs are testable without a UI host.
2. **Constructor injection everywhere.** The composition root knows how
   to build everything; ViewModels and services receive their
   dependencies via parameters.
3. **`IMessenger` is the cross-VM glue.** `WeakReferenceMessenger.Default`
   is the right default. The list VM listens via `IRecipient<T>`; the
   editor VM publishes via `Messenger.Send`.
4. **`[NotifyCanExecuteChangedFor]` keeps Save/Delete buttons in sync**
   with text input — no manual wiring needed.
5. **`ObservableRecipient.IsActive`** controls subscription lifetime —
   set it from `OnNavigatedTo` / `OnNavigatedFrom` (or an equivalent
   activation hook in your framework).
