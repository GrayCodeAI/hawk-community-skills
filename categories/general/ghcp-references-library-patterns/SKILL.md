---
name: ghcp-references-library-patterns
description: 'Skill: ghcp-references-library-patterns'
license: MIT
tags:
- general
---

## 7. Optional Backends (Plugin Pattern)

This pattern lets your package work out-of-the-box (no extra deps) with an in-memory backend,
while letting advanced users plug in Redis, a database, or any custom storage.

### 5.1 Abstract base class — defines the interface

```python
# your_package/backends/__init__.py
from abc import ABC, abstractmethod


class BaseBackend(ABC):
    """Abstract storage backend interface.

    Implement this to add a custom backend (database, cache, etc.).
    """

    @abstractmethod
    async def get(self, key: str) -> str | None:
        """Retrieve a value by key. Returns None if not found."""
        ...

    @abstractmethod
    async def set(self, key: str, value: str, ttl: int | None = None) -> None:
        """Store a value. Optional TTL in seconds."""
        ...

    @abstractmethod
    async def delete(self, key: str) -> None:
        """Delete a key."""
        ...
```

### 5.2 Memory backend — zero extra deps

```python
# your_package/backends/memory.py
from __future__ import annotations

import asyncio
import time
from your_package.backends import BaseBackend


class MemoryBackend(BaseBackend):
    """Thread-safe in-memory backend. Works out of the box — no extra dependencies."""

    def __init__(self) -> None:
        self._store: dict[str, tuple[str, float | None]] = {}
        self._lock = asyncio.Lock()

    async def get(self, key: str) -> str | None:
        async with self._lock:
            entry = self._store.get(key)
            if entry is None:
                return None
            value, expires_at = entry
            if expires_at is not None and time.time() > expires_at:
                del self._store[key]
                return None
            return value

    async def set(self, key: str, value: str, ttl: int | None = None) -> None:
        async with self._lock:
            expires_at = time.time() + ttl if ttl is not None else None
            self._store[key] = (value, expires_at)

    async def delete(self, key: str) -> None:
        async with self._lock:
            self._store.pop(key, None)
```

### 5.3 Redis backend — raises clear ImportError if not installed

The key design: import `redis` lazily inside `__init__`, not at module level. This way,
`import your_package` never fails even if `redis` isn't installed.

```python
# your_package/backends/redis.py
from __future__ import annotations
from your_package.backends import BaseBackend

try:
    import redis.asyncio as aioredis
except ImportError as exc:
    raise ImportError(
        "Redis backend requires the redis extra:\n"
        "  pip install your-package[redis]"
    ) from exc


class RedisBackend(BaseBackend):
    """Redis-backed storage for distributed/multi-process deployments."""

    def __init__(self, url: str = "redis://localhost:6379") -> None:
        self._client = aioredis.from_url(url, decode_responses=True)

    async def get(self, key: str) -> str | None:
        return await self._client.get(key)

    async def set(self, key: str, value: str, ttl: int | None = None) -> None:
        await self._client.set(key, value, ex=ttl)

    async def delete(self, key: str) -> None:
        await self._client.delete(key)
```

### 5.4 How users choose a backend

```python
# Default: in-memory, no extra deps needed
from your_package import YourClient
client = YourClient(api_key="sk-...")

# Redis: pip install your-package[redis]
from your_package.backends.redis import RedisBackend
client = YourClient(api_key="sk-...", backend=RedisBackend(url="redis://localhost:6379"))
```
