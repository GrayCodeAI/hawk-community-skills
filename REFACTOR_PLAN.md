# hawk-community-skills/categories/general/ — bucketing plan

> Status: **plan only**. No directories are moved by this document. Execution
> needs a coordinated change to `registry.json`, `tools/update_registry.py`,
> and any downstream consumer of the registry — out of scope for a side-task.

## The problem

```
categories/general/   9,842 entries (all directories, no loose files)
```

That's an order of magnitude over what filesystems and tooling handle
gracefully. Concrete pain it creates today:

- **`ls categories/general/` is slow** and produces unreadable output.
- **IDE / editor file-tree views stall** trying to render the tree.
- **`git status` and `git ls-files` are measurably slower** when many
  files in one directory get touched.
- **Filesystem-level operations** (rsync, find, fzf-style navigation)
  scale linearly with directory size, not with what you're trying to do.

## What's actually in there

Walking the directory names reveals a strong, mechanical naming convention:
each entry is prefixed with its **source** (which tool / generator produced
the skill). Top prefixes:

| Prefix     | Count | Source                                   |
| ---------- | ----: | ---------------------------------------- |
| `ag-`      | 1,453 | `ag` tool                                |
| `ghcp-`    | 1,398 | GitHub Copilot                           |
| `ls-`      | 1,230 | `ls` tool                                |
| `gpt-`     | 1,230 | OpenAI / GPT                             |
| `composio` | 864   | composio                                 |
| `cpa-`     | 391   | cpa                                      |
| `copilot-` | 376   | (older) Copilot variant                  |
| `arezv-`   | 338   | arezv                                    |
| `std-`     | 265   | std                                      |
| `flow-`    | 240   | flow                                     |
| (other)    | 2,057 | mixed long tail                          |

So the right shape is **bucket by source**, not by alphabet.

## Proposed layout

```
categories/general/
├── ag/             (1,453 entries)
├── ghcp/           (1,398)
├── ls/             (1,230)
├── gpt/            (1,230)
├── composio/         (864)
├── cpa/              (391)
├── copilot/          (376)
├── arezv/            (338)
├── std/              (265)
├── flow/             (240)
└── _misc/          (2,057)   # long tail — keep flat here
```

Net effect: ~11 directories with 240–1,453 entries each, instead of one
directory with 9,842. Every directory is now within the range filesystems
and tools handle without measurable lag.

## Migration steps (all-or-nothing — must land as one PR)

The directory rename, registry regeneration, and script update have to
land atomically because they reference each other.

1. **Update `tools/update_registry.py`** to walk the new layout:
   - Replace the single-level loop over `category/<skill>` with a
     two-level walk that descends one extra step under `general/`.
   - Emit registry paths as either `categories/general/<bucket>/<skill>`
     (faithful to disk) or keep the legacy flat path
     `categories/general/<skill>` and resolve the bucket implicitly
     (depends on what registry consumers expect).
2. **Move the directories.** A one-time script:
   ```bash
   #!/usr/bin/env bash
   cd categories/general
   for d in */; do
     prefix=$(echo "$d" | sed -E 's/^([a-z]+)-.*/\1/' | tr -d '/')
     case "$prefix" in
       ag|ghcp|ls|gpt|composio|cpa|copilot|arezv|std|flow)
         mkdir -p "$prefix"
         git mv "$d" "$prefix/" ;;
       *) ;;  # leave in _misc bucket
     esac
   done
   mkdir -p _misc
   for d in */; do
     case "$d" in
       ag/|ghcp/|ls/|gpt/|composio/|cpa/|copilot/|arezv/|std/|flow/|_misc/) ;;
       *) git mv "$d" _misc/ ;;
     esac
   done
   ```
3. **Regenerate `registry.json`** by running the updated tool:
   `python3 tools/update_registry.py`.
4. **Verify the diff** — the registry should change ~9,800 path entries
   in a single mechanical pattern; nothing else should change.
5. **Update consumers** — any consumer that expects flat
   `categories/general/<skill>` paths needs to either:
   - Apply the new path scheme.
   - Or be insulated by keeping the registry's `path` field unchanged
     and adding a parallel `dir` field that records the bucket.
6. **CI**: add a sanity job that asserts no
   `categories/general/<top-level dir>` has more than ~2,000 entries.
   Re-introducing the bloat is then auto-flagged on PRs.

## Effort

- Script + registry tool update: ~2 hours.
- Move + regenerate + diff review: ~1 hour.
- Consumer audit + fixes: ~2 hours (depends on how many consumers exist).
- **Total: half a day**, but blocking for everyone using the registry
  while it lands.

## Why I didn't execute it now

- `registry.json` is 2.8 MB of auto-generated data; regenerating it
  requires running the tool and confirming output, which is reviewing a
  large diff.
- I haven't traced who consumes `registry.json` (likely hawk's skill
  loader, but possibly external tools too).
- Mixed-content directories (ones that don't fit a clear prefix) need a
  judgement call about which bucket they belong to — should be a human
  decision, not regex.

When you do this, do it as a single coordinated PR with a CI green run
across hawk + this repo so consumers don't break in the meantime.
