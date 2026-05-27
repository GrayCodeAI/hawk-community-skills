---
name: mdc-django-views
description: "Specific guidelines for Django views, focusing on class-based vs. function-based views, error handling, and request handling."
license: MIT
tags: [python]
---

- Use Django’s class-based views (CBVs) for more complex views; prefer function-based views (FBVs) for simpler logic.
- Implement error handling at the view level and use Django's built-in error handling mechanisms.
- Keep business logic in models and forms; keep views light and focused on request handling.