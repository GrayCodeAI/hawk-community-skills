---
name: ghcp-assets-paddle-game-template
description: 'Skill: ghcp-assets-paddle-game-template'
license: MIT
tags:
- general
---

## Quick Reference: All Game Variables

| Variable | Type | Purpose |
|----------|------|---------|
| `canvas` | const | Reference to the HTML canvas element |
| `ctx` | const | 2D rendering context |
| `ballRadius` | const | Radius of the ball (10) |
| `x`, `y` | let | Current ball position |
| `dx`, `dy` | let | Ball velocity (pixels per frame) |
| `paddleHeight` | const | Height of the paddle (10) |
| `paddleWidth` | const | Width of the paddle (75) |
| `paddleX` | let | Current horizontal position of the paddle |
| `rightPressed` | let | Whether the right arrow key is held down |
| `leftPressed` | let | Whether the left arrow key is held down |
| `brickRowCount` | const | Number of brick rows (3) |
| `brickColumnCount` | const | Number of brick columns (5) |
| `brickWidth` | const | Width of each brick (75) |
| `brickHeight` | const | Height of each brick (20) |
| `brickPadding` | const | Space between bricks (10) |
| `brickOffsetTop` | const | Distance from top of canvas to first brick row (30) |
| `brickOffsetLeft` | const | Distance from left of canvas to first brick column (30) |
| `bricks` | const | 2D array holding all brick objects |
| `score` | let | Current player score |
| `lives` | let | Remaining lives (starts at 3) |

## Quick Reference: All Functions

| Function | Purpose |
|----------|---------|
| `keyDownHandler(e)` | Sets `rightPressed` or `leftPressed` to `true` on key press |
| `keyUpHandler(e)` | Sets `rightPressed` or `leftPressed` to `false` on key release |
| `mouseMoveHandler(e)` | Moves paddle to follow mouse horizontal position |
| `collisionDetection()` | Checks ball against all active bricks; destroys hit bricks, increments score, checks win |
| `drawBall()` | Renders the ball at current `(x, y)` position |
| `drawPaddle()` | Renders the paddle at current `paddleX` position |
| `drawBricks()` | Renders all bricks with `status === 1` |
| `drawScore()` | Renders the score text in the top-left corner |
| `drawLives()` | Renders the lives text in the top-right corner |
| `draw()` | Main game loop: clears canvas, draws everything, handles collisions, updates positions |
