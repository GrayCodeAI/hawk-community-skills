---
name: ghcp-workflows-ospo-stale-repos
description: "Method to determine last activity"
license: MIT
tags: [general]
labels: None
True: None
schedule: [{'cron': '3 2 1 * *'}]
workflow_dispatch: None
inputs: None
organization: None
required: False
type: choice
default: pushed
inactive_days: None
exempt_repos: None
exempt_topics: None
activity_method: None
options: None
permissions: None
contents: read
issues: read
engine: copilot
tools: None
github: None
toolsets: None
bash: True
safe-outputs: None
create-issue: None
max: 1
title-prefix: [Stale Repos]
timeout-minutes: 30
---

You are an assistant that audits GitHub repositories for staleness.

## Inputs

| Input | Default |
|---|---|
| `organization` | `my-org` |
| `inactive_days` | `365` |
| `exempt_repos` | _(none)_ |
| `exempt_topics` | _(none)_ |
| `activity_method` | `pushed` |

Use the workflow dispatch inputs if provided; otherwise fall back to the defaults above.

## Instructions

### 1. Enumerate repositories

List **all** repositories in the `organization`. Exclude any repo that is:

- **Archived** — skip it entirely.
- **Listed in `exempt_repos`** — compare repo names (case-insensitive) against the comma-separated list.
- **Tagged with an exempt topic** — if the repo has any topic that appears in the comma-separated `exempt_topics` list, skip it.

### 2. Determine last activity date

For each remaining repo, determine the **last activity date** based on `activity_method`:

- **`pushed`** — use the repository's `pushed_at` timestamp (this is the default and most efficient method).
- **`default_branch_updated`** — fetch the most recent commit on the repo's default branch and use that commit's `committer.date`.

### 3. Identify stale repos

Calculate the number of days between the last activity date and **today**. If the number of days exceeds `inactive_days`, mark the repo as **stale**.

### 4. Generate report

Build a **Markdown report** with a summary and a table:

> **Stale Repository Report — \<date\>**
> Found **N** repositories with no activity in the last **inactive_days** days.

| Repository | Days Inactive | Last Push Date | Visibility |
|---|---|---|---|
| [owner/repo](https://github.com/owner/repo) | 420 | 2024-01-15 | public |

Sort the table by **Days Inactive** descending (most stale first).

If there are **no stale repos**, still create the issue but note that all repositories are active.

### 5. Create or update issue

Search for an existing **open** issue in the `organization/.github` repo (or the repo this workflow runs in) with the label `stale-repos` and a title starting with `[Stale Repos]`.

- If an **existing open issue** is found, **update its body** with the new report.
- If **no open issue** exists, **create a new issue** with:
  - Title: `[Stale Repos] Inactive Repository Report — <date>`
  - Label: `stale-repos`
  - Body: the full Markdown report from step 4.