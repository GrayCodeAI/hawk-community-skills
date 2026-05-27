---
name: mdc-fastapi-startup-and-shutdown-events
description: "Recommends minimizing the use of startup and shutdown events in favor of lifespan context managers."
license: MIT
tags: [python]
---

- Minimize @app.on_event("startup") and @app.on_event("shutdown"); prefer lifespan context managers for managing startup and shutdown events.