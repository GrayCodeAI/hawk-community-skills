---
name: cursor-go
description: Cursor IDE rules for go
domain: engineering
tags: [cursor, ide-rules]
version: "1.0"
author: cursorrules-collection
---

---
description: "Go patterns: error wrapping, goroutines, interfaces"
globs: ["*.go"]
alwaysApply: true
---

# Go Cursor Rules

You are an expert Go developer (1.21+). Follow these rules:

## Code Style
- `gofmt` / `goimports` formatting is mandatory — no style debates, the formatter decides
- Short but descriptive names: `userID` not `theUserIdentifier`. Receiver names are 1-2 letters (`s` for server, `u` for user). Don't name receivers `self` or `this`
- MixedCaps only, never underscores in Go names. Exported = Uppercase, unexported = lowercase — this is access control, not convention
- Package names are lowercase, single word, no underscores: `httputil` not `http_util`. The package name is part of the call site: `httputil.NewClient` not `httputil.NewHTTPUtilClient`

## Error Handling
- Check every error immediately. Never discard with `_` unless you comment why: `_ = conn.Close() // best-effort cleanup`
- Wrap errors with context: `fmt.Errorf("fetching user %d: %w", id, err)` — `%w` wraps (unwrappable), `%v` formats (not unwrappable). Always use `%w` when the caller might need to inspect the cause
- Sentinel errors (`var ErrNotFound = errors.New("not found")`) for expected conditions callers handle differently. Custom error types (`type ValidationError struct{}`) when the error carries structured data
- `errors.Is()` for sentinel comparison, `errors.As()` for type extraction — never `err.Error() == "some string"`, error messages are not API
- Don't log and return the same error — pick one. Logging + returning means the error gets logged at every level of the call stack

## Concurrency
- Every goroutine must have a clear shutdown path — `context.Context` for cancellation, `done` channels for signaling
- Creator of a channel closes it. Never close from the receiver side — it panics if multiple goroutines receive
- `sync.WaitGroup` for fan-out when all goroutines must complete. `errgroup.Group` when you need the first error and want to cancel the rest
- `sync.Mutex` for protecting shared state. Channels for communication between goroutines. Don't use channels as mutexes — it's clever but unreadable
- Watch for goroutine leaks: a goroutine blocked on a channel send/receive with no timeout lives forever. Always pass a context with timeout or deadline
- `sync.Once` for one-time initialization (DB connection, config load) — not `init()` which runs at import time and is hard to test

## Design
- Accept interfaces, return concrete types — lets callers define the abstraction they need, not you
- Keep interfaces small: 1-3 methods max. The bigger the interface, the weaker the abstraction. `io.Reader` has one method and is the most useful interface in the stdlib
- Table-driven tests: `tests := []struct{ name string; input X; want Y }{}` with `t.Run(tt.name, ...)` — descriptive subtest names show up in CI output
- Dependency injection via struct fields, not package globals. `type Server struct { db Database; logger Logger }` — testable, no init() surprises

## Packages
- One package = one responsibility. Name packages for what they provide: `auth`, `storage`, `email` — not `util`, `helpers`, `common`
- `internal/` packages for code that shouldn't be imported by other modules — compiler-enforced, not just convention
- Avoid package-level `var` for state — initialize in `main()` or a constructor and pass explicitly. Package-level state makes testing painful and creates hidden dependencies

## Common Traps
- `defer` runs at function exit, not block exit — `defer` in a loop doesn't clean up each iteration, it queues them all for function return
- `range` over a slice copies the value: `for _, v := range items { go func() { use(v) }() }` captures the loop variable, not the value. Go 1.22+ fixes this, but for older versions, shadow it: `v := v`
- `nil` interface vs nil pointer: `var p *MyType = nil; var i interface{} = p; i != nil` is true — the interface holds a typed nil, which is not a nil interface
- Slice append may or may not create a new backing array — if you pass a slice to a function and it appends, the caller may or may not see the change. Return the new slice or use a pointer to a slice
- `context.Background()` only in `main()` or top-level tests. Everywhere else, accept and propagate the context from the caller
