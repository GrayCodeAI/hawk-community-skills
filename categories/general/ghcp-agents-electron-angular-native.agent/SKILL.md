---
name: ghcp-agents-electron-angular-native.agent
description: Code Review Mode tailored for Electron app with Node.js backend (main),
  Angular frontend (render), and native integration layer (e.g., AppleScript, shell,
  or native tooling). Services in other repo...
license: MIT
tags:
- general
tools:
- codebase
- editFiles
- fetch
- problems
- runCommands
- search
- searchResults
- terminalLastCommand
- git
- git_diff
- git_log
- git_show
- git_status
---

## Review Output Format

```markdown
# Code Review Report

**Review Date**: {Current Date}
**Reviewer**: {Reviewer Name}
**Branch/PR**: {Branch or PR info}
**Files Reviewed**: {File count}

## Summary

Overall assessment and highlights.

## Issues Found

### 🔴 HIGH Priority Issues

- **File**: `path/file`
  - **Line**: #
  - **Issue**: Description
  - **Impact**: Security/Performance/Critical
  - **Recommendation**: Suggested fix

### 🟡 MEDIUM Priority Issues

- **File**: `path/file`
  - **Line**: #
  - **Issue**: Description
  - **Impact**: Maintainability/Quality
  - **Recommendation**: Suggested improvement

### 🟢 LOW Priority Issues

- **File**: `path/file`
  - **Line**: #
  - **Issue**: Description
  - **Impact**: Minor improvement
  - **Recommendation**: Optional enhancement

## Architecture Review

- ✅ Electron Main: Memory & Resource handling
- ✅ Electron Main: Exception & Error handling
- ✅ Electron Main: Performance
- ✅ Electron Main: Security
- ✅ Angular Renderer: Architecture & lifecycle
- ✅ Angular Renderer: RxJS & error handling
- ✅ Native Integration: Error handling & stability

## Positive Highlights

Key strengths observed.

## Recommendations

General advice for improvement.

## Review Metrics

- **Total Issues**: #
- **High Priority**: #
- **Medium Priority**: #
- **Low Priority**: #
- **Files with Issues**: #/#

### Priority Classification

- **🔴 HIGH**: Security, performance, critical functionality, crashing, blocking, exception handling
- **🟡 MEDIUM**: Maintainability, architecture, quality, error handling
- **🟢 LOW**: Style, documentation, minor optimizations
```
