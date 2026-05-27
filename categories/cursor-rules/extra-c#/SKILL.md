---
name: extra-c#
description: C# 开发规则与最佳实践
license: MIT
tags:
- cursor-rules
alwaysApply: false
---

## 6. 错误处理与日志 (Error & Logging)

- **Try-Catch 策略**：不要用 try-catch 包裹整个方法体。仅捕获特定的、预期的异常。
- **日志规范**：
  - 使用 `ILogger<T>`。
  - 异常日志 **必须** 包含异常对象：`_logger.LogError(ex, "Message")`，不能仅记录 `ex.Message`。
