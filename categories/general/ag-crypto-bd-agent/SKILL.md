---
name: ag-crypto-bd-agent
description: Production-tested patterns for building AI agents that autonomously discover,
  > evaluate, and acquire token listings for cryptocurrency exchanges.
license: MIT
tags:
- general
risk: safe
source: community
date_added: 2026-02-27
---

## Reference Implementation

Buzz BD Agent (SolCex Exchange):
- 13 intelligence sources (11 free + 2 paid)
- 23 automated cron jobs, 4 experience memory tracks
- ERC-8004: ETH #25045 | Base #17483
- x402 micropayments ($0.30/day)
- LLM cascade: MiniMax M2.5 → Llama 70B → Haiku 4.5 → Opus 4.5
- 24/7 live stream: retake.tv/BuzzBD
- Verify: 8004scan.io
- GitHub: https://github.com/buzzbysolcex/buzz-bd-agent

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
