---
name: inst-setup-firebase-astro
description: 'Skill: inst-setup-firebase-astro'
license: MIT
tags:
- general
---

<div>
  <form method="post" enctype="multipart/form-data">
    <input
      type="file"
      name="file"
      accept="image/*"
      required
    />
    <input type="hidden" name="action" value="upload" />
    <button type="submit">Upload</button>
  </form>

  {error && <p class="error">{error}</p>}

  <ul>
    {files.map((file) => (
      <li>
        <a href={file.url} target="_blank" rel="noopener noreferrer">
          {file.name}
        </a>
        <form method="post" style="display: inline">
          <input type="hidden" name="filename" value={file.name} />
          <input type="hidden" name="action" value="delete" />
          <button type="submit">Delete</button>
        </form>
      </li>
    ))}
  </ul>
</div>
```

## Security Considerations
1. Never expose Firebase configuration in client-side code without proper security measures
2. Use environment variables for sensitive configuration
3. Implement proper session management
4. Set up appropriate Firebase security rules
5. Use Firebase Admin SDK for server-side operations
6. Implement proper CSRF protection
7. Validate all user input server-side
8. Use secure session cookies

## Best Practices
1. Use TypeScript for better type safety
2. Separate client and server-side Firebase configurations
3. Implement proper error handling
4. Use Astro's built-in form handling
5. Implement proper loading states
6. Use Firebase emulators for local development
7. Follow Astro's patterns for data mutations
8. Implement proper data validation
9. Use Firebase indexes for complex queries

## Troubleshooting
1. Check Firebase console for errors
2. Verify security rules configuration
3. Check network requests in browser developer tools
4. Use Firebase debugging tools
5. Monitor Firebase usage and quotas
6. Check Astro server logs
7. Verify environment variables

## Additional Resources
- [Firebase Documentation](https://firebase.google.com/docs)
- [Astro Documentation](https://docs.astro.build)
- [Firebase Console](https://console.firebase.google.com/)
