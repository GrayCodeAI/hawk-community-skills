---
name: ghcp-workflows-daily-issues-report
description: "Generates a daily summary of open issues and recent activity as a GitHub issue"
license: MIT
tags: [general]
True: None
schedule: daily on weekdays
permissions: None
contents: read
issues: read
safe-outputs: None
create-issue: None
title-prefix: [daily-report]
labels: [report]
---

## Daily Issues Report

Create a daily summary of open issues for the team.

## What to Include

- New issues opened in the last 24 hours
- Issues closed or resolved
- Stale issues that need attention