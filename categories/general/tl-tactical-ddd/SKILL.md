---
name: tl-tactical-ddd
description: 'Skill: tl-tactical-ddd'
license: MIT
tags:
- general
---

## Domain Events

**Naming**: Past tense + Ubiquitous Language. `OrderConfirmed`, `BacklogItemCommitted`, `UserRegistered`.

```typescript
interface DomainEvent {
  readonly occurredOn: Date;
  readonly eventVersion: number;
}

class OrderConfirmed implements DomainEvent {
  readonly occurredOn = new Date();
  readonly eventVersion = 1;
  constructor(
    readonly orderId: OrderId,
    readonly confirmedBy: UserId,
  ) {}
}
```

**Publication pattern**:
1. Complete state change
2. Publish event (state is already consistent)
3. Subscribers run in separate transactions for cross-Aggregate consistency

**Checklist**:
- [ ] Named in past tense?
- [ ] All fields `readonly`?
- [ ] Published after (not during) state change?
- [ ] Carries only data the Aggregate already owns?
- [ ] Cross-Aggregate handlers run in separate transactions?
