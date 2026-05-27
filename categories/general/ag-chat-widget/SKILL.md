---
name: ag-chat-widget
description: Build a real-time support chat system with a floating widget for users
  and an admin dashboard for support staff. Use when the user wants live chat, customer
  support chat, real-time messaging, or in...
license: MIT
tags:
- general
risk: unknown
source: community
---

## Real-Time Technology Options

| Technology | Best For | Serverless? |
|------------|----------|-------------|
| ActionCable (Rails) | Rails apps | No |
| Socket.IO | Node.js apps | No |
| Pusher | Any stack | Yes |
| Ably | Any stack | Yes |
| Supabase Realtime | Supabase users | Yes |
| Firebase RTDB | Firebase users | Yes |
| Server-Sent Events | Simple one-way | Yes |

### Fallback Strategy
If WebSocket unavailable, implement polling:
```pseudo
// Poll every 5 seconds when disconnected
if (!websocket.connected) {
  setInterval(() => {
    fetch('/api/support-chat/messages?since=' + lastMessageTime)
      .then(newMessages => appendMessages(newMessages))
  }, 5000)
}
```

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
