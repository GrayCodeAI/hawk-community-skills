---
name: mdc-backend-communication-rules
description: "Rules for communicating with the external backend from the Tauri frontend."
license: MIT
tags: [cursor-rules]
---

- Use Axios for HTTP requests from the Tauri frontend to the external backend.
- Implement proper error handling for network requests and responses.
- Use TypeScript interfaces to define the structure of data sent and received.
- Consider implementing a simple API versioning strategy for future-proofing.
- Handle potential CORS issues when communicating with the backend.
- Ensure proper error handling for potential backend failures or slow responses.
- Consider implementing retry mechanisms for failed requests.
- Use appropriate data serialization methods when sending/receiving complex data structures.