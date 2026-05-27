---
name: ghcp-references-wrap-api
description: 'Skill: ghcp-references-wrap-api'
license: MIT
tags:
- general
---

## Trace File Utilities

Pydantic model for wrap log entries and JSONL loading utilities.

`WrapLogEntry` is the typed representation of a single `wrap()` event
as recorded in a JSONL trace file. Multiple places in the codebase load
these objects — the `pixie trace filter` CLI, the dataset loader, and
the verification scripts — so they share this single model.

### `pixie.WrapLogEntry`

```python
pixie.WrapLogEntry(*, type: str = 'wrap', name: str, purpose: str, data: Any, description: str | None = None, trace_id: str | None = None, span_id: str | None = None) -> None
```

A single wrap() event as logged to a JSONL trace file.

Attributes:
type: Always `"wrap"` for wrap events.
name: The wrap point name (matches `wrap(name=...)`).
purpose: One of `"input"`, `"output"`, `"state"`.
data: The serialized data (jsonpickle string).
description: Optional human-readable description.
trace_id: OTel trace ID (if available).
span_id: OTel span ID (if available).

### `pixie.load_wrap_log_entries`

```python
pixie.load_wrap_log_entries(jsonl_path: 'str | Path') -> 'list[WrapLogEntry]'
```

Load all wrap log entries from a JSONL file.

Skips non-wrap lines (e.g. `type=llm_span`) and malformed lines.

Args:
jsonl_path: Path to a JSONL trace file.

Returns:
List of :class:`WrapLogEntry` objects.

### `pixie.filter_by_purpose`

```python
pixie.filter_by_purpose(entries: 'list[WrapLogEntry]', purposes: 'set[str]') -> 'list[WrapLogEntry]'
```

Filter wrap log entries by purpose.

Args:
entries: List of wrap log entries.
purposes: Set of purpose values to include.

Returns:
Filtered list.
