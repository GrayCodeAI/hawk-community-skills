# Changelog

## v0.5 - 2026-05-04

Commit: [`01d1fab`](https://github.com/ciembor/agent-rules-books/commit/01d1fab)

- Added compatibility check in `_rule-workbench/CHECK_COMPATIBILITY.md`.
- Added compatibility matrix in `docs/COMPATIBILITY.md`.
- Each compatibility comparison has now its own `.md` file in `docs/compatibility`.

## v0.4 - 2026-05-03

Commit: [`63cbe8c`](https://github.com/ciembor/agent-rules-books/commit/63cbe8c)

- Added a new `Refactoring.Guru` rule set based on the public Refactoring.Guru refactoring process, code smell catalog, and refactoring technique catalog.
- Added full, `mini`, and `nano` releases for `refactoring-guru`, plus workbench traceability and a canonical workbench `full.md` symlink.
- Standardized all released and workbench rule headings to the `# OBEY {name} by {author}` format, omitting `by` when no clear author exists.
- Removed `Mini`, `Nano`, and `Traceability` suffixes from rule-file H1 headings while keeping version context in filenames and body structure.
- Updated the README release matrix metrics after the heading changes and added `Refactoring.Guru` to the Books section.
- Updated `_rule-workbench/PROCESS.md` so future compression runs preserve the standardized heading format.

## v0.3 - 2026-05-02

Commit: [`bd62818`](https://github.com/ciembor/agent-rules-books/commit/bd62818)

- Revalidated all full rule sets against their original source books.
- Removed cross-contamination of terminology, patterns, and guidance between different book rule sets.
- Added missing rules and clarified rule boundaries and intent consistency.
- Regenerated all `mini` and `nano` variants from the corrected full sources.
- Improved consistency, specificity, and book alignment across the entire library.

### Book-specific updates

- **A Philosophy of Software Design** - refined complexity management, module depth, and interface design guidance.
- **Clean Architecture** - clarified layer boundaries, dependency direction, and infrastructure isolation.
- **Clean Code** - improved naming, function design, and readability-focused rules.
- **Code Complete** - strengthened defensive programming and implementation quality guidance.
- **Designing Data-Intensive Applications** - improved distributed systems, consistency, and data flow guidance.
- **Domain-Driven Design** - clarified bounded contexts, aggregates, and ubiquitous language usage.
- **Domain-Driven Design Distilled** - simplified and sharpened strategic DDD guidance.
- **Implementing Domain-Driven Design** - improved aggregate implementation and context integration guidance.
- **Patterns of Enterprise Application Architecture** - refined layering, persistence, and enterprise pattern boundaries.
- **Refactoring** - strengthened small-step refactoring and behavior-preserving transformation rules.
- **Release It!** - improved resilience, operability, and production-readiness guidance.
- **The Pragmatic Programmer** - refined pragmatic decision-making and feedback-loop heuristics.
- **Working Effectively with Legacy Code** - improved seams, isolation, and legacy-safe change guidance.

## v0.2 - 2026-04-27

Commit: [`bc8ab7e`](https://github.com/ciembor/agent-rules-books/commit/bc8ab7e)

- Finalized the compressed rule set naming as `mini` and `nano`.
- Made `mini` the recommended default rule layer and kept `nano` as the tight-context fallback.
- Completed the compressed release line that introduced tool-agnostic rule files, usage workflow documentation, traceability files, and release process docs.
- Historical commits included in this release line: [`10f71b9`](https://github.com/ciembor/agent-rules-books/commit/10f71b9), [`f216255`](https://github.com/ciembor/agent-rules-books/commit/f216255), [`bef3b39`](https://github.com/ciembor/agent-rules-books/commit/bef3b39), [`3f96a91`](https://github.com/ciembor/agent-rules-books/commit/3f96a91), [`5fb98ad`](https://github.com/ciembor/agent-rules-books/commit/5fb98ad).

## v0.1 - 2026-04-16

Commit: [`3738a8c`](https://github.com/ciembor/agent-rules-books/commit/3738a8c)

- Published the first book-rule library with full rule sets already available.
- Included full rule files for 13 software engineering books.
- Shipped editor-specific layouts for Codex, Claude Code, and Cursor.
- Added the initial README, MIT license, and repository ignore rules.
