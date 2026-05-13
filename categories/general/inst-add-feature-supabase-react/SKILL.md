---
description: Guidelines for adding new features with Supabase in React applications
globs: **/*.ts, **/*.tsx, **/*.js, **/*.jsx
---

# Adding Features with Supabase in React

## Authentication Features

### Social Authentication
```typescript
import { supabase } from './supabaseClient'

export const signInWithGithub = async () => {
  const { data, error } = await supabase.auth.signInWithOAuth({
    provider: 'github',
    options: {
      redirectTo: window.location.origin
    }
  })
  if (error) throw error
  return data
}
```

### Magic Link Authentication
```typescript
import { supabase } from './supabaseClient'

export const sendMagicLink = async (email: string) => {
  const { data, error } = await supabase.auth.signInWithOtp({
    email,
    options: {
      emailRedirectTo: window.location.origin
    }
  })
  if (error) throw error
  return data
}
```

## Real-time Features

### Real-time Subscriptions
```typescript
import { useEffect, useState } from 'react'
import { supabase } from './supabaseClient'
import { RealtimeChannel } from '@supabase/supabase-js'

export function useRealtimeSubscription<T>(
  table: string,
  schema = 'public'
) {
  const [data, setData] = useState<T[]>([])
  const [channel, setChannel] = useState<RealtimeChannel | null>(null)

  useEffect(() => {
    const channel = supabase
      .channel('table_db_changes')
      .on(
        'postgres_changes',
        { event: '*', schema, table },
        (payload) => {
          // Handle different change types
          switch (payload.eventType) {
            case 'INSERT':
              setData(prev => [...prev, payload.new as T])
              break
            case 'UPDATE':
              setData(prev => prev.map(item => 
                item.id === payload.new.id ? payload.new : item
              ))
              break
            case 'DELETE':
              setData(prev => prev.filter(item => item.id !== payload.old.id))
              break
          }
        }
      )
      .subscribe()

    setChannel(channel)

    return () => {
      channel.unsubscribe()
    }
  }, [table, schema])

  return { data }
}
```

## Database Features

### Row Level Security
```typescript
// Example RLS policy in your Supabase dashboard
create policy "Users can only access their own data"
on public.profiles
for all
using (auth.uid() = user_id);

// React component using RLS-protected data
export function UserProfile() {
  const { user } = useAuth()
  const [profile, setProfile] = useState(null)

  useEffect(() => {
    if (user) {
      const fetchProfile = async () => {
        const { data, error } = await supabase
          .from('profiles')
          .select('*')
          .eq('user_id', user.id)
          .single()
        
        if (error) throw error
        setProfile(data)
      }
      
      fetchProfile()
    }
  }, [user])

  return profile ? <div>{profile.username}</div> : null
}
```

### Full Text Search
```typescript
export function SearchProducts() {
  const [query, setQuery] = useState('')
  const [results, setResults] = useState([])

  const searchProducts = async (searchQuery: string) => {
    const { data, error } = await supabase
      .from('products')
      .select('*')
      .textSearch('description', searchQuery, {
        type: 'websearch',
        config: 'english'
      })
    
    if (error) throw error
    setResults(data)
  }

  return (
    <div>
      <input
        type="text"
        value={query}
        onChange={e => {
          setQuery(e.target.value)
          searchProducts(e.target.value)
        }}
      />
      {results.map(product => (
        <div key={product.id}>{product.name}</div>
      ))}
    </div>
  )
}
```

## Storage Features

### File Upload
```typescript
export function FileUpload() {
  const uploadFile = async (file: File) => {
    const { data, error } = await supabase.storage
      .from('bucket-name')
      .upload(`folder/${file.name}`, file, {
        cacheControl: '3600',
        upsert: true
      })
    
    if (error) throw error
    return data
  }

  return (
    <input
      type="file"
      onChange={async (e) => {
        if (!e.target.files?.[0]) return
        try {
          const data = await uploadFile(e.target.files[0])
          console.log('File uploaded:', data)
        } catch (error) {
          console.error('Error uploading file:', error)
        }
      }}
    />
  )
}
```

## Edge Functions

### Invoking Edge Functions
```typescript
export async function processData(inputData: any) {
  const { data, error } = await supabase.functions.invoke(
    'process-data',
    {
      body: { data: inputData },
      headers: {
        'Custom-Header': 'value'
      }
    }
  )
  
  if (error) throw error
  return data
}
```

## Error Handling

### Proper Error Handling Pattern
```typescript
export function ErrorBoundary({ children }: { children: React.ReactNode }) {
  const [error, setError] = useState<Error | null>(null)

  if (error) {
    return (
      <div role="alert">
        <p>Something went wrong:</p>
        <pre>{error.message}</pre>
        <button onClick={() => setError(null)}>Try again</button>
      </div>
    )
  }

  return (
    <ErrorBoundary
      fallback={({ error }) => (
        <div role="alert">
          <p>Something went wrong:</p>
          <pre>{error.message}</pre>
        </div>
      )}
    >
      {children}
    </ErrorBoundary>
  )
}
```

## Development Tools

### Using Supabase CLI
```bash
# Install Supabase CLI
npm install -g supabase-cli

# Start local development
supabase start

# Generate types from your database schema
supabase gen types typescript --local > src/types/supabase.ts

# Deploy database changes
supabase db push
``` 