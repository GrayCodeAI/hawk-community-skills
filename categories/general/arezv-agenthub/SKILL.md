---
name: arezv-agenthub
description: Multi-agent collaboration plugin that spawns N parallel subagents competing
  on the same task via git worktree isolation. Agents work independently, results
  are evaluated by metric or LLM judge, and...
license: MIT
tags:
- general
metadata: None
version: 2.1.2
author: Alireza Rezvani
category: engineering
updated: 2026-03-17
---

## Result Summary

- **Approach**: Replaced O(n²) sort with hash map
- **Files changed**: 3
- **Metric**: 142ms (baseline: 180ms, delta: -38ms)
- **Confidence**: High — all tests pass
```

### Board Rules

- Append-only: never edit or delete posts
- Unique filenames: `{seq:03d}-{author}-{timestamp}.md`
- YAML frontmatter required on all posts

## Evaluation Modes

### Metric-Based

Best for: benchmarks, test pass rates, file sizes, response times.

```bash
python scripts/result_ranker.py --session {id} \
  --eval-cmd "pytest bench.py --json" \
  --metric p50_ms --direction lower
```

The ranker runs the eval command in each agent's worktree directory and parses the metric from stdout.

### LLM Judge

Best for: code quality, readability, architecture decisions.

The coordinator reads each agent's diff (`git diff base...agent-branch`) and ranks by:
1. Correctness (does it solve the task?)
2. Simplicity (fewer lines changed preferred)
3. Quality (clean execution, good structure)

### Hybrid

Run metric first. If top agents are within 10% of each other, use LLM judge to break ties.

## Session Lifecycle

```
init → running → evaluating → merged
                            → archived (if no winner)
```

State transitions managed by `session_manager.py`:

| From | To | Trigger |
|------|----|---------|
| `init` | `running` | `/hub:spawn` completes |
| `running` | `evaluating` | All agents return |
| `evaluating` | `merged` | `/hub:merge` completes |
| `evaluating` | `archived` | No winner / all failed |

## Proactive Triggers

The coordinator should act when:

| Signal | Action |
|--------|--------|
| All agents crashed | Post failure summary, suggest retry with different constraints |
| No improvement over baseline | Archive session, suggest different approaches |
| Orphan worktrees detected | Run `session_manager.py --cleanup {id}` |
| Session stuck in `running` | Check board for progress, consider timeout |

## Installation

```bash
# Copy to your Claude Code skills directory
cp -r engineering/agenthub ~/.claude/skills/agenthub

# Or install via ClawHub
clawhub install agenthub
```

## Scripts

| Script | Purpose |
|--------|---------|
| `hub_init.py` | Initialize `.agenthub/` structure and session |
| `dag_analyzer.py` | Frontier detection, DAG graph, branch status |
| `board_manager.py` | Message board CRUD (channels, posts, threads) |
| `result_ranker.py` | Rank agents by metric or diff quality |
| `session_manager.py` | Session state machine and cleanup |

## Related Skills

- **autoresearch-agent** — Single-agent optimization loop (use AgentHub when you want N agents competing)
- **self-improving-agent** — Self-modifying agent (use AgentHub when you want external competition)
- **git-worktree-manager** — Git worktree utilities (AgentHub uses worktrees internally)
