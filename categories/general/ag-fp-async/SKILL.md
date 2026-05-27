---
name: ag-fp-async
description: Practical async patterns using TaskEither - clean pipelines instead of
  try/catch hell, with real API examples
license: MIT
tags:
- general
risk: unknown
source: community
version: 1.0.0
author: kadu
---

## Before/After Summary

### Fetching Data

```typescript
// BEFORE
async function getUser(id: string) {
  try {
    const res = await fetch(`/api/users/${id}`)
    if (!res.ok) throw new Error('Not found')
    return await res.json()
  } catch (e) {
    console.error(e)
    return null
  }
}

// AFTER
const getUser = (id: string) =>
  TE.tryCatch(
    async () => {
      const res = await fetch(`/api/users/${id}`)
      if (!res.ok) throw new Error('Not found')
      return res.json()
    },
    E.toError
  )
```

### Chained Operations

```typescript
// BEFORE
async function processOrder(orderId: string) {
  const order = await fetchOrder(orderId)
  if (!order) throw new Error('No order')
  const user = await fetchUser(order.userId)
  if (!user) throw new Error('No user')
  const result = await chargePayment(user, order.total)
  return result
}

// AFTER
const processOrder = (orderId: string) =>
  pipe(
    TE.Do,
    TE.bind('order', () => fetchOrder(orderId)),
    TE.bind('user', ({ order }) => fetchUser(order.userId)),
    TE.chain(({ user, order }) => chargePayment(user, order.total))
  )
```

### Error Recovery

```typescript
// BEFORE
async function getData(id: string) {
  try {
    return await fetchFromApi(id)
  } catch {
    try {
      return await fetchFromCache(id)
    } catch {
      return defaultValue
    }
  }
}

// AFTER
const getData = (id: string) =>
  pipe(
    fetchFromApi(id),
    TE.orElse(() => fetchFromCache(id)),
    TE.getOrElse(() => T.of(defaultValue))
  )
```

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
