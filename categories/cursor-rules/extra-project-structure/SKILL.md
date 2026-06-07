---
name: extra-project-structure
description: "项目约定的代码结构规范"
license: MIT
tags: [cursor-rules]
alwaysApply: True
---

# 项目结构规范

> **使用说明：** 将此文件复制到你的项目后，根据实际目录结构填写以下内容。

## 顶层目录

```
<project-root>/
├── src/          # 源代码
├── tests/        # 测试文件
├── docs/         # 文档
└── ...           # 根据项目实际情况补充
```

## 目录职责说明

| 目录 | 说明 |
|------|------|
| `src/` | 主业务代码，按功能模块分层 |
| `tests/` | 单元测试与集成测试 |
| `docs/` | 架构文档、API 说明等 |

## 关键约定

- 按功能域划分子目录，不超过 3-4 层嵌套
- 测试文件与源文件结构镜像，或统一放置于 `tests/`
- 配置文件集中于项目根目录或 `config/`