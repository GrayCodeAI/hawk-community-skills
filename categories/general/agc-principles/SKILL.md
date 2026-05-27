---
name: agc-principles
description: 'Skill: agc-principles'
license: MIT
tags:
- general
---

## Explanation: Understanding-Oriented Documentation

### What Explanation Is

Explanation provides context and background. It helps users understand and see the bigger picture.

**Key characteristic**: Explanation permits reflection. It serves study (like tutorials), but through theoretical knowledge (like reference).

### Detailed Principles

#### 1. Talk *About* the Subject

Explanation approaches topics from multiple directions. It circles around the subject, providing different perspectives.

You're not documenting *for* action (like tutorials or how-to guides). You're documenting to illuminate understanding.

Even titles should reflect this: "About user authentication", "About database connection policies".

#### 2. Answer "Why"

Explanation is uniquely positioned to address "why" questions:
- Why is it designed this way?
- Why choose this over alternatives?
- Why did this evolve historically?
- Why does this constraint exist?

These questions have no place in tutorials, how-to guides, or reference. Explanation is where they belong.

#### 3. Make Connections

Help weave a web of understanding:
- Connect to related concepts
- Show how parts interact
- Link to things outside the immediate topic
- Draw parallels to familiar ideas

Understanding means seeing relationships. Explanation makes those relationships visible.

#### 4. Provide Context

Give background that helps users understand:
- Historical context: How did we get here?
- Design context: What constraints shaped this?
- Technical context: What trade-offs were made?
- Social context: How do others approach this?

Context transforms isolated facts into meaningful understanding.

#### 5. Permit Opinion and Perspective

Unlike reference (which must be neutral), explanation can and should include:
- Opinions about approaches
- Discussion of trade-offs
- Counter-examples
- Alternative perspectives

Understanding is richer than pure facts. Discussion can consider and weigh contrary opinions.

But keep it bounded - don't let opinion turn into advocacy or marketing.

#### 6. Keep Boundaries Clear

The risk with explanation is that it tends to absorb other things. You feel the urge to include instruction or reference.

But those have their own places. Keep explanation focused on understanding. If you need to instruct, link to a how-to guide. If you need technical details, link to reference.

#### 7. Take a Higher Perspective

Explanation doesn't take the user's eye-level view (like how-to guides) or the close-up view of machinery (like reference).

Its scope is a topic - "an area of knowledge" with reasonable boundaries. It looks at things from above and across, showing the bigger picture.

### Explanation Examples

**Good explanation**:
```markdown
# About Authentication Strategies

Our authentication system uses JWT tokens rather than session cookies. This decision
reflects several trade-offs in our architecture.

## Session-based vs Token-based Authentication

Session-based authentication stores state on the server. This simplifies some security
concerns - invalidating a session is just deleting a server-side record. However, it
complicates horizontal scaling. Every server needs access to session state, requiring
either sticky sessions (which limit load balancing) or a shared session store (which
becomes a single point of failure).

JWT tokens are stateless. The token itself contains all authentication information,
cryptographically signed. This makes them ideal for distributed systems - any server
can validate any token without coordinating with others.

## The Token Revocation Problem

Stateless tokens create a challenge: how do you revoke a token before it expires?
With sessions, you delete the session record. With JWTs, the token remains valid
until expiration regardless of server-side actions.

We address this through short token lifetimes (15 minutes) combined with refresh
tokens. This limits the exposure window while allowing long-lived sessions. It's a
compromise between security and user experience.

Some teams maintain a token blocklist, but this partially defeats the stateless
benefit and introduces the coordination problem we were trying to avoid.

## Historical Context

We initially used session-based authentication. As we moved to a microservices
architecture with multiple API gateways, session management became increasingly
complex. The shift to JWTs in version 2.0 was driven by these scaling requirements.

For more on implementing JWT authentication, see the authentication how-to guide.
For JWT token reference, see the security reference.
```

**Bad explanation** (too much instruction):
```markdown
# JWT Authentication

To implement JWT authentication, first install the JWT library:

```bash
pip install pyjwt
```

Then create a token like this:

[Code instructions continue...]
```

This should be in a how-to guide, not explanation.
