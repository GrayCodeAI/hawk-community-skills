---
description: Django 后端开发的约定和最佳实践。
globs: **/*.py
alwaysApply: false
---

# Django 规则

- 使用 `python manage.py startapp` 在项目中创建新应用
- 在 `models.py` 中保存模型，并在 `admin.py` 中注册以使用管理界面
- 使用 Django 的 ORM 而非原始 SQL 查询
- 使用 `select_related` 和 `prefetch_related` 避免 N+1 查询问题：

```python
# 良好模式
users = User.objects.select_related('profile')
posts = Post.objects.prefetch_related('tags')
```

- 使用 Django 表单进行验证：

```python
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
```

- 为常见查询创建自定义模型管理器：

```python
class ActiveUserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
```

- 使用 Django 内置的身份验证系统
- 在环境变量中存储设置并通过 `settings.py` 访问