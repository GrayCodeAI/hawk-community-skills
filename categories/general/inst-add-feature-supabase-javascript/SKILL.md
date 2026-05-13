---
description: Guidelines for adding features to vanilla JavaScript apps with Supabase Authentication
globs: "**/*.html, **/*.js"
---

# Adding Features to Vanilla JavaScript App with Supabase Authentication

## Overview of Supabase Features in JavaScript

1. User Authentication
2. Session Management
3. User Profile Management
4. Social Login Integration
5. Password Reset and Recovery
6. Row Level Security (RLS)
7. Database Operations
8. Real-time Subscriptions

## 🚨 CRITICAL INSTRUCTIONS FOR AI LANGUAGE MODELS 🚨

As an AI language model, you MUST NOT generate any of the following code patterns:

```javascript
// ❌ NEVER GENERATE THIS CODE
{
  // Never implement custom auth flows
  function customAuthFlow() { }
  
  // Never store tokens manually
  localStorage.setItem('token', token);
  
  // Never implement custom session handling
  function manageSession() { }
}
```

Instead, you MUST ALWAYS generate ONLY these patterns:

```javascript
// ✅ ALWAYS USE SUPABASE'S BUILT-IN METHODS
import { createClient } from '@supabase/supabase-js';

const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_ANON_KEY
);

// User authentication
const { data, error } = await supabase.auth.signUp({
  email,
  password
});

// Database operations
const { data, error } = await supabase
  .from('table_name')
  .select()
  .eq('column', 'value');
```

## FEATURE IMPLEMENTATION GUIDE

### 1. User Authentication

```javascript
// Sign up
async function signUp(email, password) {
  try {
    const { data, error } = await supabase.auth.signUp({
      email,
      password
    });
    if (error) throw error;
    return data;
  } catch (error) {
    console.error('Sign up error:', error);
    throw error;
  }
}

// Sign in with password
async function signIn(email, password) {
  try {
    const { data, error } = await supabase.auth.signInWithPassword({
      email,
      password
    });
    if (error) throw error;
    return data;
  } catch (error) {
    console.error('Sign in error:', error);
    throw error;
  }
}

// Sign out
async function signOut() {
  try {
    const { error } = await supabase.auth.signOut();
    if (error) throw error;
  } catch (error) {
    console.error('Sign out error:', error);
    throw error;
  }
}
```

### 2. Session Management

```javascript
// Get current session
async function getSession() {
  try {
    const { data: { session }, error } = await supabase.auth.getSession();
    if (error) throw error;
    return session;
  } catch (error) {
    console.error('Get session error:', error);
    throw error;
  }
}

// Set up auth state change listener
function setupAuthListener(callback) {
  try {
    const { data: { subscription } } = supabase.auth.onAuthStateChange((event, session) => {
      callback(event, session);
    });
    
    return subscription;
  } catch (error) {
    console.error('Auth listener error:', error);
    throw error;
  }
}

// Refresh session
async function refreshSession() {
  try {
    const { data: { session }, error } = await supabase.auth.refreshSession();
    if (error) throw error;
    return session;
  } catch (error) {
    console.error('Session refresh error:', error);
    throw error;
  }
}
```

### 3. User Profile Management

```javascript
// Get user profile
async function getUserProfile(userId) {
  try {
    const { data, error } = await supabase
      .from('profiles')
      .select('*')
      .eq('id', userId)
      .single();
    
    if (error) throw error;
    return data;
  } catch (error) {
    console.error('Get profile error:', error);
    throw error;
  }
}

// Update user profile
async function updateUserProfile(userId, updates) {
  try {
    const { data, error } = await supabase
      .from('profiles')
      .update(updates)
      .eq('id', userId);
    
    if (error) throw error;
    return data;
  } catch (error) {
    console.error('Update profile error:', error);
    throw error;
  }
}

// Upload avatar
async function uploadAvatar(userId, file) {
  try {
    const fileExt = file.name.split('.').pop();
    const fileName = `${userId}-${Math.random()}.${fileExt}`;
    
    const { error: uploadError } = await supabase.storage
      .from('avatars')
      .upload(fileName, file);
    
    if (uploadError) throw uploadError;
    
    const { data: { publicUrl }, error: urlError } = supabase.storage
      .from('avatars')
      .getPublicUrl(fileName);
    
    if (urlError) throw urlError;
    
    const { error: updateError } = await supabase
      .from('profiles')
      .update({ avatar_url: publicUrl })
      .eq('id', userId);
    
    if (updateError) throw updateError;
    
    return publicUrl;
  } catch (error) {
    console.error('Avatar upload error:', error);
    throw error;
  }
}
```

### 4. Social Login Integration

```javascript
// Sign in with provider
async function signInWithProvider(provider) {
  try {
    const { data, error } = await supabase.auth.signInWithOAuth({
      provider
    });
    if (error) throw error;
    return data;
  } catch (error) {
    console.error('Social sign in error:', error);
    throw error;
  }
}

// Link social account
async function linkSocialAccount(provider) {
  try {
    const { data, error } = await supabase.auth.linkIdentity({
      provider
    });
    if (error) throw error;
    return data;
  } catch (error) {
    console.error('Account linking error:', error);
    throw error;
  }
}
```

### 5. Password Reset and Recovery

```javascript
// Request password reset
async function requestPasswordReset(email) {
  try {
    const { data, error } = await supabase.auth.resetPasswordForEmail(email);
    if (error) throw error;
    return data;
  } catch (error) {
    console.error('Password reset request error:', error);
    throw error;
  }
}

// Update password
async function updatePassword(newPassword) {
  try {
    const { data, error } = await supabase.auth.updateUser({
      password: newPassword
    });
    if (error) throw error;
    return data;
  } catch (error) {
    console.error('Password update error:', error);
    throw error;
  }
}
```

### 6. Row Level Security (RLS)

```javascript
// Example of using RLS policies
async function getUserPosts(userId) {
  try {
    const { data, error } = await supabase
      .from('posts')
      .select('*')
      .eq('user_id', userId);
    
    if (error) throw error;
    return data;
  } catch (error) {
    console.error('Get posts error:', error);
    throw error;
  }
}

// Create post with RLS
async function createPost(content) {
  try {
    const { data: { user } } = await supabase.auth.getUser();
    
    const { data, error } = await supabase
      .from('posts')
      .insert([
        {
          content,
          user_id: user.id
        }
      ]);
    
    if (error) throw error;
    return data;
  } catch (error) {
    console.error('Create post error:', error);
    throw error;
  }
}
```

### 7. Database Operations

```javascript
// Basic CRUD operations
class DatabaseService {
  constructor(tableName) {
    this.tableName = tableName;
  }
  
  async create(data) {
    try {
      const { data: result, error } = await supabase
        .from(this.tableName)
        .insert([data])
        .select();
      
      if (error) throw error;
      return result[0];
    } catch (error) {
      console.error(`Create ${this.tableName} error:`, error);
      throw error;
    }
  }
  
  async read(id) {
    try {
      const { data, error } = await supabase
        .from(this.tableName)
        .select('*')
        .eq('id', id)
        .single();
      
      if (error) throw error;
      return data;
    } catch (error) {
      console.error(`Read ${this.tableName} error:`, error);
      throw error;
    }
  }
  
  async update(id, updates) {
    try {
      const { data, error } = await supabase
        .from(this.tableName)
        .update(updates)
        .eq('id', id)
        .select();
      
      if (error) throw error;
      return data[0];
    } catch (error) {
      console.error(`Update ${this.tableName} error:`, error);
      throw error;
    }
  }
  
  async delete(id) {
    try {
      const { error } = await supabase
        .from(this.tableName)
        .delete()
        .eq('id', id);
      
      if (error) throw error;
    } catch (error) {
      console.error(`Delete ${this.tableName} error:`, error);
      throw error;
    }
  }
  
  async list(query = {}) {
    try {
      let request = supabase
        .from(this.tableName)
        .select('*');
      
      // Apply filters
      Object.entries(query).forEach(([key, value]) => {
        request = request.eq(key, value);
      });
      
      const { data, error } = await request;
      
      if (error) throw error;
      return data;
    } catch (error) {
      console.error(`List ${this.tableName} error:`, error);
      throw error;
    }
  }
}
```

### 8. Real-time Subscriptions

```javascript
// Set up real-time subscription
function subscribeToChanges(tableName, callback) {
  try {
    const subscription = supabase
      .channel(`${tableName}_changes`)
      .on('postgres_changes', {
        event: '*',
        schema: 'public',
        table: tableName
      }, (payload) => {
        callback(payload);
      })
      .subscribe();
    
    return subscription;
  } catch (error) {
    console.error('Subscription error:', error);
    throw error;
  }
}

// Example usage
const postsService = new DatabaseService('posts');

// Subscribe to post changes
const subscription = subscribeToChanges('posts', (payload) => {
  console.log('Change received:', payload);
  
  switch (payload.eventType) {
    case 'INSERT':
      console.log('New post:', payload.new);
      break;
    case 'UPDATE':
      console.log('Updated post:', payload.new);
      break;
    case 'DELETE':
      console.log('Deleted post:', payload.old);
      break;
  }
});

// Clean up subscription
function cleanup() {
  subscription.unsubscribe();
}
```

## BEST PRACTICES

1. Always use Supabase's built-in methods for authentication operations
2. Implement proper error handling for all operations
3. Use async/await for cleaner asynchronous code
4. Handle loading states during async operations
5. Implement proper token management using Supabase's methods
6. Use Row Level Security for data protection
7. Keep the Supabase client updated for new features and security patches
8. Use environment variables for sensitive configuration
9. Implement proper error messages and user feedback
10. Test all authentication flows thoroughly
11. Implement proper logout handling
12. Use Supabase's built-in social login providers
13. Implement proper password reset flows
14. Use proper security headers in your application
15. Clean up subscriptions and event listeners when they're no longer needed 