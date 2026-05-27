---
name: ghcp-assets-2d-maze-game
description: 'Skill: ghcp-assets-2d-maze-game'
license: MIT
tags:
- general
---

## Phaser API Quick Reference

| Function | Purpose |
|----------|---------|
| `this.add.sprite(x, y, key)` | Create a game object |
| `this.add.group()` | Create a container for objects |
| `this.add.button(x, y, key, cb, ctx, over, out, down)` | Create interactive button |
| `this.add.text(x, y, text, style)` | Create text display |
| `this.physics.enable(obj, system)` | Enable physics on object |
| `this.physics.arcade.collide(a, b, cb)` | Detect collision with bounce |
| `this.physics.arcade.overlap(a, b, cb)` | Detect overlap without bounce |
| `this.load.image(key, path)` | Load image asset |
| `this.load.spritesheet(key, path, w, h)` | Load sprite animation sheet |
| `this.load.audio(key, paths[])` | Load audio with format fallbacks |
| `this.game.add.audio(key)` | Instantiate audio object |
| `this.time.events.loop(interval, cb, ctx)` | Create repeating timer |
