---
name: ghcp-assets-2d-platform-game
description: 'Skill: ghcp-assets-2d-platform-game'
license: MIT
tags:
- general
---

## Moving Forward

Congratulations -- you have built a complete 2D platformer. Here are ideas for extending the game further:

### Suggested Improvements

- **Mobile / touch controls:** Add on-screen buttons or swipe gestures using `game.input.onDown` for touch-enabled devices.
- **More levels:** Create additional JSON level files with new platform layouts, coin placements, and enemy configurations.
- **Menu screen:** Add a `MenuState` with a title screen and start button before entering `PlayState`.
- **Game over screen:** Instead of instantly restarting, show a "Game Over" screen with the score.
- **Lives system:** Give the hero multiple lives instead of instant restart.
- **Power-ups:** Add items like speed boosts, double jump, or invincibility.
- **Moving platforms:** Create platforms that travel along a path using tweens.
- **Different enemy types:** Add flying enemies, enemies that shoot projectiles, or enemies with different movement patterns.
- **Parallax scrolling:** Add multiple background layers that scroll at different speeds for depth.
- **Camera scrolling:** For levels wider than the screen, use `game.camera.follow(this.hero)` to scroll with the hero.
- **Sound and music:** Add background music and additional sound effects for a more polished experience.
- **Particle effects:** Use Phaser's particle emitter for coin collection sparkles, enemy death effects, or dust when landing.

### Full Game Source Reference

Below is the complete `main.js` file combining all steps for reference. This represents the final state of the game with all features:

```javascript
// =============================================================================
// Constants
// =============================================================================

const SPEED = 200;
const JUMP_SPEED = 600;
const LEVEL_COUNT = 2;
const Spider = { SPEED: 100 };

// =============================================================================
// Game State: PlayState
// =============================================================================

PlayState = {};

// -----------------------------------------------------------------------------
// init
// -----------------------------------------------------------------------------

PlayState.init = function (data) {
    this.game.renderer.renderSession.roundPixels = true;

    this.keys = this.game.input.keyboard.addKeys({
        left: Phaser.KeyCode.LEFT,
        right: Phaser.KeyCode.RIGHT,
        up: Phaser.KeyCode.UP
    });

    this.game.physics.startSystem(Phaser.Physics.ARCADE);
    this.game.physics.arcade.gravity.y = 1200;

    this.level = (data.level || 0) % LEVEL_COUNT;
};

// -----------------------------------------------------------------------------
// preload
// -----------------------------------------------------------------------------

PlayState.preload = function () {
    // Background
    this.game.load.image('background', 'images/background.png');

    // Level data
    this.game.load.json('level:0', 'data/level00.json');
    this.game.load.json('level:1', 'data/level01.json');

    // Platform tiles
    this.game.load.image('ground', 'images/ground.png');
    this.game.load.image('grass:8x1', 'images/grass_8x1.png');
    this.game.load.image('grass:6x1', 'images/grass_6x1.png');
    this.game.load.image('grass:4x1', 'images/grass_4x1.png');
    this.game.load.image('grass:2x1', 'images/grass_2x1.png');
    this.game.load.image('grass:1x1', 'images/grass_1x1.png');

    // Characters
    this.game.load.spritesheet('hero', 'images/hero.png', 36, 42);
    this.game.load.spritesheet('spider', 'images/spider.png', 42, 32);
    this.game.load.image('invisible-wall', 'images/invisible_wall.png');

    // Collectibles
    this.game.load.spritesheet('coin', 'images/coin_animated.png', 22, 22);
    this.game.load.spritesheet('key', 'images/key.png', 20, 22);
    this.game.load.spritesheet('door', 'images/door.png', 42, 66);

    // HUD
    this.game.load.image('icon:coin', 'images/coin_icon.png');
    this.game.load.image('icon:key', 'images/key_icon.png');
    this.game.load.image('font:numbers', 'images/numbers.png');

    // Audio
    this.game.load.audio('sfx:jump', 'audio/sfx/jump.wav');
    this.game.load.audio('sfx:coin', 'audio/sfx/coin.wav');
    this.game.load.audio('sfx:stomp', 'audio/sfx/stomp.wav');
    this.game.load.audio('sfx:key', 'audio/sfx/key.wav');
    this.game.load.audio('sfx:door', 'audio/sfx/door.wav');
};

// -----------------------------------------------------------------------------
// create
// -----------------------------------------------------------------------------

PlayState.create = function () {
    // Sound effects
    this.sfx = {
        jump: this.game.add.audio('sfx:jump'),
        coin: this.game.add.audio('sfx:coin'),
        stomp: this.game.add.audio('sfx:stomp'),
        key: this.game.add.audio('sfx:key'),
        door: this.game.add.audio('sfx:door')
    };

    // Background
    this.game.add.image(0, 0, 'background');

    // Load level
    this._loadLevel(this.game.cache.getJSON('level:' + this.level));

    // HUD
    this._createHud();
};

// -----------------------------------------------------------------------------
// update
// -----------------------------------------------------------------------------

PlayState.update = function () {
    this._handleCollisions();
    this._handleInput();

    // Update hero sprite direction and animation
    if (this.hero.body.velocity.x < 0) {
        this.hero.scale.x = -1;
    } else if (this.hero.body.velocity.x > 0) {
        this.hero.scale.x = 1;
    }
    this.hero.animations.play(this._getAnimationName());

    // Update spider directions when hitting walls
    this.spiders.forEach(function (spider) {
        if (spider.body.touching.right || spider.body.blocked.right) {
            spider.body.velocity.x = -Spider.SPEED;
        } else if (spider.body.touching.left || spider.body.blocked.left) {
            spider.body.velocity.x = Spider.SPEED;
        }
    }, this);

    // Update key icon in HUD
    this.keyIcon.frame = this.hasKey ? 1 : 0;
};

// -----------------------------------------------------------------------------
// Level Loading
// -----------------------------------------------------------------------------

PlayState._loadLevel = function (data) {
    // Create groups (order matters for rendering layers)
    this.bgDecoration = this.game.add.group();
    this.platforms = this.game.add.group();
    this.coins = this.game.add.group();
    this.spiders = this.game.add.group();
    this.enemyWalls = this.game.add.group();

    // Spawn entities from level data
    data.platforms.forEach(this._spawnPlatform, this);
    data.coins.forEach(this._spawnCoin, this);
    data.spiders.forEach(this._spawnSpider, this);

    this._spawnDoor(data.door.x, data.door.y);
    this._spawnKey(data.key.x, data.key.y);
    this._spawnCharacters({ hero: data.hero });

    // Hide invisible walls
    this.enemyWalls.visible = false;

    // Initialize game state
    this.coinPickupCount = 0;
    this.hasKey = false;
};

// -----------------------------------------------------------------------------
// Spawn Methods
// -----------------------------------------------------------------------------

PlayState._spawnPlatform = function (platform) {
    let sprite = this.platforms.create(platform.x, platform.y, platform.image);
    this.game.physics.enable(sprite);
    sprite.body.allowGravity = false;
    sprite.body.immovable = true;

    // Add invisible walls at both edges for enemy AI
    this._spawnEnemyWall(platform.x, platform.y, 'left');
    this._spawnEnemyWall(platform.x + sprite.width, platform.y, 'right');
};

PlayState._spawnEnemyWall = function (x, y, side) {
    let sprite = this.enemyWalls.create(x, y, 'invisible-wall');
    sprite.anchor.set(side === 'left' ? 1 : 0, 1);
    this.game.physics.enable(sprite);
    sprite.body.immovable = true;
    sprite.body.allowGravity = false;
};

PlayState._spawnCharacters = function (data) {
    this.hero = this.game.add.sprite(data.hero.x, data.hero.y, 'hero');
    this.hero.anchor.set(0.5, 1);
    this.game.physics.enable(this.hero);
    this.hero.body.collideWorldBounds = true;

    // Hero animations
    this.hero.animations.add('stop', [0]);
    this.hero.animations.add('run', [1, 2], 8, true);
    this.hero.animations.add('jump', [3]);
    this.hero.animations.add('fall', [4]);
};

PlayState._spawnCoin = function (coin) {
    let sprite = this.coins.create(coin.x, coin.y, 'coin');
    sprite.anchor.set(0.5, 0.5);
    this.game.physics.enable(sprite);
    sprite.body.allowGravity = false;

    sprite.animations.add('rotate', [0, 1, 2, 1], 6, true);
    sprite.animations.play('rotate');
};

PlayState._spawnSpider = function (spider) {
    let sprite = this.spiders.create(spider.x, spider.y, 'spider');
    sprite.anchor.set(0.5, 1);
    this.game.physics.enable(sprite);

    sprite.animations.add('crawl', [0, 1, 2], 8, true);
    sprite.animations.add('die', [0, 4, 0, 4, 0, 4, 3, 3, 3, 3, 3, 3], 12);
    sprite.animations.play('crawl');

    sprite.body.velocity.x = Spider.SPEED;
};

PlayState._spawnDoor = function (x, y) {
    this.door = this.bgDecoration.create(x, y, 'door');
    this.door.anchor.setTo(0.5, 1);
    this.game.physics.enable(this.door);
    this.door.body.allowGravity = false;
};

PlayState._spawnKey = function (x, y) {
    this.key = this.bgDecoration.create(x, y, 'key');
    this.key.anchor.set(0.5, 0.5);
    this.game.physics.enable(this.key);
    this.key.body.allowGravity = false;

    // Bobbing tween
    this.key.y -= 3;
    this.game.add.tween(this.key)
        .to({ y: this.key.y + 6 }, 800, Phaser.Easing.Sinusoidal.InOut)
        .yoyo(true)
        .loop()
        .start();
};

// -----------------------------------------------------------------------------
// Input
// -----------------------------------------------------------------------------

PlayState._handleInput = function () {
    if (!this.hero.alive) { return; }

    if (this.keys.left.isDown) {
        this.hero.body.velocity.x = -SPEED;
    } else if (this.keys.right.isDown) {
        this.hero.body.velocity.x = SPEED;
    } else {
        this.hero.body.velocity.x = 0;
    }

    if (this.keys.up.isDown) {
        this._jump();
    }
};

PlayState._jump = function () {
    let canJump = this.hero.body.touching.down;
    if (canJump) {
        this.hero.body.velocity.y = -JUMP_SPEED;
        this.sfx.jump.play();
    }
    return canJump;
};

// -----------------------------------------------------------------------------
// Collisions
// -----------------------------------------------------------------------------

PlayState._handleCollisions = function () {
    // Physical collisions
    this.game.physics.arcade.collide(this.hero, this.platforms);
    this.game.physics.arcade.collide(this.spiders, this.platforms);
    this.game.physics.arcade.collide(this.spiders, this.enemyWalls);

    // Overlap detection (no physical push)
    this.game.physics.arcade.overlap(
        this.hero, this.coins, this._onHeroVsCoin, null, this
    );
    this.game.physics.arcade.overlap(
        this.hero, this.spiders, this._onHeroVsEnemy, null, this
    );
    this.game.physics.arcade.overlap(
        this.hero, this.key, this._onHeroVsKey, null, this
    );
    this.game.physics.arcade.overlap(
        this.hero, this.door, this._onHeroVsDoor,
        function (hero, door) {
            return this.hasKey && hero.body.touching.down;
        }, this
    );
};

// -----------------------------------------------------------------------------
// Collision Callbacks
// -----------------------------------------------------------------------------

PlayState._onHeroVsCoin = function (hero, coin) {
    this.sfx.coin.play();
    coin.kill();
    this.coinPickupCount++;
    this.coinFont.text = 'x' + this.coinPickupCount;
};

PlayState._onHeroVsEnemy = function (hero, enemy) {
    if (hero.body.velocity.y > 0) {
        // Stomp: hero is falling onto the enemy
        enemy.body.velocity.x = 0;
        enemy.body.enable = false;
        enemy.animations.play('die');
        enemy.events.onAnimationComplete.addOnce(function () {
            enemy.kill();
        });
        hero.body.velocity.y = -JUMP_SPEED / 2;
        this.sfx.stomp.play();
    } else {
        // Hero dies
        this._killHero();
    }
};

PlayState._onHeroVsKey = function (hero, key) {
    this.sfx.key.play();
    key.kill();
    this.hasKey = true;
};

PlayState._onHeroVsDoor = function (hero, door) {
    this.sfx.door.play();
    hero.body.velocity.x = 0;
    hero.body.velocity.y = 0;
    hero.body.enable = false;

    door.frame = 1; // Open door

    this.game.time.events.add(500, this._goToNextLevel, this);
};

// -----------------------------------------------------------------------------
// Death and Level Transitions
// -----------------------------------------------------------------------------

PlayState._killHero = function () {
    this.hero.alive = false;
    this.hero.body.velocity.y = -JUMP_SPEED / 2;
    this.hero.body.velocity.x = 0;
    this.hero.body.allowGravity = true;
    this.hero.body.collideWorldBounds = false;

    this.game.time.events.add(1000, function () {
        this.game.state.restart(true, false, { level: this.level });
    }, this);
};

PlayState._goToNextLevel = function () {
    this.camera.fade('#000');
    this.camera.onFadeComplete.addOnce(function () {
        this.game.state.restart(true, false, {
            level: this.level + 1
        });
    }, this);
};

// -----------------------------------------------------------------------------
// Animations
// -----------------------------------------------------------------------------

PlayState._getAnimationName = function () {
    let name = 'stop';

    if (!this.hero.alive) {
        name = 'stop';
    } else if (this.hero.body.velocity.y < 0) {
        name = 'jump';
    } else if (this.hero.body.velocity.y > 0 && !this.hero.body.touching.down) {
        name = 'fall';
    } else if (this.hero.body.velocity.x !== 0 && this.hero.body.touching.down) {
        name = 'run';
    }

    return name;
};

// -----------------------------------------------------------------------------
// HUD
// -----------------------------------------------------------------------------

PlayState._createHud = function () {
    this.keyIcon = this.game.make.image(0, 19, 'icon:key');
    this.keyIcon.anchor.set(0, 0.5);

    let coinIcon = this.game.make.image(
        this.keyIcon.width + 7, 0, 'icon:coin'
    );

    let scoreStyle = { font: '24px monospace', fill: '#fff' };
    this.coinFont = this.game.add.text(
        coinIcon.x + coinIcon.width + 7, 0, 'x0', scoreStyle
    );

    this.hud = this.game.add.group();
    this.hud.add(this.keyIcon);
    this.hud.add(coinIcon);
    this.hud.add(this.coinFont);
    this.hud.position.set(10, 10);
    this.hud.fixedToCamera = true;
};

// =============================================================================
// Entry Point
// =============================================================================

window.onload = function () {
    let game = new Phaser.Game(960, 600, Phaser.AUTO, 'game');
    game.state.add('play', PlayState);
    game.state.start('play', true, false, { level: 0 });
};
```

### Key Concepts Summary

| Concept | Phaser API | Purpose |
|---------|-----------|---------|
| Game instance | `new Phaser.Game(w, h, renderer, container)` | Creates the game canvas and engine |
| Game states | `game.state.add()` / `game.state.start()` | Organizes code into init/preload/create/update lifecycle |
| Loading images | `game.load.image(key, path)` | Loads a static image asset |
| Loading spritesheets | `game.load.spritesheet(key, path, fw, fh)` | Loads an animated spritesheet |
| Loading JSON | `game.load.json(key, path)` | Loads JSON data (level definitions) |
| Loading audio | `game.load.audio(key, path)` | Loads a sound effect |
| Sprite groups | `game.add.group()` | Container for related sprites; enables batch collision detection |
| Physics bodies | `game.physics.enable(sprite)` | Adds an Arcade Physics body to a sprite |
| Gravity | `game.physics.arcade.gravity.y` | Global downward acceleration |
| Collision | `arcade.collide(a, b)` | Physical collision resolution (sprites push each other) |
| Overlap | `arcade.overlap(a, b, callback)` | Detection without physical push (for pickups) |
| Velocity | `sprite.body.velocity.x/y` | Movement speed in pixels per second |
| Immovable | `sprite.body.immovable = true` | Prevents sprite from being pushed by collisions |
| Animations | `sprite.animations.add(name, frames, fps, loop)` | Defines a frame animation |
| Tweens | `game.add.tween(target).to(props, duration, easing)` | Smooth property animation |
| Keyboard input | `game.input.keyboard.addKeys({...})` | Captures specific keyboard keys |
| Camera | `this.camera.fade()` | Screen transition effects |
| Anchor | `sprite.anchor.set(x, y)` | Sets the origin point for positioning and rotation |
| Sprite flipping | `sprite.scale.x = -1` | Horizontally mirrors the sprite |
