---
name: ghcp-references-relaycommand-cookbook
description: 'Skill: ghcp-references-relaycommand-cookbook'
license: MIT
tags:
- general
---

## Common mistakes

1. **`async void` instead of `async Task`.** The generator only wraps
   `Task`-returning methods as `IAsyncRelayCommand`. `async void` becomes a
   sync `RelayCommand` and exceptions are unobserved.
2. **Forgetting `[NotifyCanExecuteChangedFor]`.** The button stays disabled
   even though `CanX()` would now return `true`.
3. **Calling `Cancel()` on a non-cancellable command.** Only commands whose
   wrapped method accepts a `CancellationToken` honor `Cancel()`.
4. **Catching `OperationCanceledException` and rethrowing as a different
   type.** Loses cancellation semantics; `ExecutionTask.IsCanceled` will be
   `false`. Let `OperationCanceledException` propagate (or return).
5. **Awaiting `IAsyncRelayCommand.ExecuteAsync()` from inside another
   `[RelayCommand]`.** Prefer calling the underlying method directly to
   avoid double-wrapping the cancellation/concurrency semantics.
