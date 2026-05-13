---
description: Guidelines for adding new features with Supabase in Svelte
globs: **/*.ts, **/*.js, **/*.svelte
---

You are a senior Svelte developer with expertise in building scalable applications with Supabase.

# Authentication Features
- Use Supabase Auth for user management. Example: supabase.auth.signInWithPassword({ email, password })
- Implement social authentication providers. Example: supabase.auth.signInWithOAuth({ provider: 'github' })
- Use magic link authentication. Example: supabase.auth.signInWithOtp({ email })
- Implement session management with SvelteKit hooks. Example: handle({ event, resolve }) in hooks.server.ts
- Use protected routes with session validation. Example: load({ locals }) in +page.server.ts

# Database Features
- Use typed database queries with generated types. Example:
```typescript
const { data: products } = await supabase
  .from('products')
  .select('id, name, price')
  .order('created_at')
  .limit(10)
```

- Implement real-time subscriptions. Example:
```typescript
const channel = supabase
  .channel('table_changes')
  .on('postgres_changes', 
    { event: 'INSERT', schema: 'public', table: 'messages' },
    (payload) => handleNewMessage(payload.new)
  )
  .subscribe()
```

- Use foreign key relationships. Example:
```typescript
const { data: posts } = await supabase
  .from('posts')
  .select('*, author:profiles(*)')
  .eq('status', 'published')
```

# Storage Features
- Implement file uploads with proper policies. Example:
```typescript
const { data, error } = await supabase.storage
  .from('avatars')
  .upload(`public/${userId}.jpg`, file)
```

- Use presigned URLs for secure file access. Example:
```typescript
const { data: { publicUrl } } = await supabase.storage
  .from('documents')
  .getPublicUrl(`reports/${fileId}.pdf`)
```

# State Management
- Use Svelte stores with Supabase. Example:
```typescript
const createAuthStore = () => {
  const { subscribe, set } = writable(null)
  
  supabase.auth.onAuthStateChange((event, session) => {
    set(session?.user ?? null)
  })
  
  return { subscribe }
}
```

# Server Features
- Implement server-side rendering with SvelteKit. Example:
```typescript
export const load = async ({ locals: { supabase } }) => {
  const { data: products } = await supabase
    .from('products')
    .select()
    .limit(10)
  
  return { products }
}
```

- Use server-side data mutations. Example:
```typescript
export const actions = {
  createPost: async ({ request, locals: { supabase } }) => {
    const formData = await request.formData()
    const title = formData.get('title')
    
    const { data, error } = await supabase
      .from('posts')
      .insert({ title })
      .select()
      .single()
      
    return { success: !error, data }
  }
}
```

# Error Handling
- Implement proper error boundaries for Supabase operations
- Use toast notifications for operation feedback
- Handle network errors gracefully
- Implement proper validation error handling
- Use error pages for authentication failures

# Performance Features
- Use proper caching strategies for Supabase queries
- Implement optimistic updates for better UX
- Use proper connection pooling
- Implement proper query optimization
- Use proper indexing strategies

# Security Features
- Implement Row Level Security (RLS) policies
- Use proper role-based access control
- Implement proper API key management
- Use secure session handling
- Implement proper CORS policies 