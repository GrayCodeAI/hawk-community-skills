---
name: ghcp-assets-gamebase-template-repo
description: 'Skill: ghcp-assets-gamebase-template-repo'
license: MIT
tags:
- general
---

## Entity Lifecycle

```
Constructor  -->  init()  -->  [game loop: fixedUpdate/update/postUpdate]  -->  dispose()
```

- **Constructor:** Set initial position, create sprite, register in global entity list
- **fixedUpdate():** Physics step (velocity, friction, gravity, collision)
- **update():** AI, state machine, animation triggers
- **postUpdate():** Sync sprite position to grid coordinates, apply visual effects
- **dispose():** Remove from entity list, destroy sprite, clean up references
