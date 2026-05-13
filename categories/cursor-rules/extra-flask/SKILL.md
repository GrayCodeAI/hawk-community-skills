---
description: Flask 轻量级 Python Web 应用程序的约定和最佳实践。
globs: **/*.py
alwaysApply: false
---

# Flask 规则

- 使用 Blueprints 按功能或资源组织路由
- 使用 Flask-SQLAlchemy 处理数据库模型和 ORM
- 使用应用工厂（application factories）实现灵活的应用初始化
- 使用 Flask 扩展实现常见功能（Flask-Login、Flask-WTF 等）
- 在环境变量中存储配置
- 使用 Flask-Migrate 进行数据库迁移
- 使用错误处理器实现适当的错误处理
- 使用 Flask-RESTful 或类似工具构建 API