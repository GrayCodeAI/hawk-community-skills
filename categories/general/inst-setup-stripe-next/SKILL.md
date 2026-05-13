---
description: Stripe integration standards and practicesfor Next.js applications
globs: **/*.ts, **/*.js
---

# Stripe Setup Guide for NextJS

## 1. Prerequisites

- Stripe account
- Next.js project
- PostgreSQL database (using Drizzle ORM)
- Node.js
- Stripe CLI

## 2. Environment Variables

Add these to your `.env` file:

```
# Stripe API keys
STRIPE_SECRET_KEY=sk_test_xxxx (replace with your Stripe secret key)
STRIPE_WEBHOOK_SECRET=whsec_xxxx (replace with your webhook signing secret)
STRIPE_PUBLISHABLE_KEY=pk_test_xxxx (for client-side operations)

# Subscription price IDs from Stripe Dashboard
STRIPE_MONTHLY_PRICE_ID=price_xxxx
STRIPE_YEARLY_PRICE_ID=price_xxxx

# Application URL (ensure no trailing slash)
NEXT_PUBLIC_URL=http://localhost:3000 (update for production)
```

## 3. Database Schema

The project uses the following Stripe-related tables:

```typescript
// Users table with Stripe fields
export const users = pgTable("users", {
  uuid: text("uuid").notNull().primaryKey(),
  email: text("email").unique(),
  pro_access: boolean("pro_access").default(false),
  stripeCustomerId: text("stripe_customer_id").unique(),
  stripeSubscriptionId: text("stripe_subscription_id").unique(),
  subscriptionStatus: text("subscription_status"),
  subscriptionPriceId: text("subscription_price_id"),
  subscriptionCurrentPeriodEnd: timestamp("subscription_current_period_end"),
  cancelAtPeriodEnd: boolean("cancel_at_period_end").default(false),
  lastInvoiceStatus: text("last_invoice_status"),
  lastPaymentError: text("last_payment_error"),
});

// Stripe events table for webhook processing
export const stripeEvents = pgTable("stripe_events", {
  stripeEventId: text("stripe_event_id").primaryKey(),
  type: text("type").notNull(),
  data: jsonb("data").notNull(),
  createdAt: timestamp("created_at").defaultNow(),
  processedAt: timestamp("processed_at"),
});
```

## 4. API Routes Setup

### 4.1 Create Checkout Session (`/api/stripe/create-checkout/route.js`)

```javascript
import Stripe from "stripe";
const stripe = new Stripe(process.env.STRIPE_SECRET_KEY);

export async function POST(request) {
  // Create or retrieve Stripe customer
  let stripeCustomerId = user?.stripeCustomerId;

  // Create checkout session
  const session = await stripe.checkout.sessions.create({
    mode: "subscription",
    payment_method_types: ["card"],
    line_items: [
      {
        price: priceId,
        quantity: 1,
      },
    ],
    success_url: `${process.env.NEXT_PUBLIC_URL}/settings?success=true`,
    cancel_url: `${process.env.NEXT_PUBLIC_URL}/settings?canceled=true`,
    customer: stripeCustomerId,
  });

  return { url: session.url };
}
```

### 4.2 Customer Portal (`/api/stripe/create-portal/route.js`)

```javascript
export async function POST(request) {
  // Create Stripe Portal session
  const session = await stripe.billingPortal.sessions.create({
    customer: user.stripeCustomerId,
    return_url: `${process.env.NEXT_PUBLIC_URL}/settings?portal_return=true`,
  });

  return { url: session.url };
}
```

### 4.3 Webhook Handler (`/api/stripe/webhook/route.js`)

```javascript
export const config = {
  api: { bodyParser: false },
};

export async function POST(request) {
  // Verify webhook signature
  const sig = headers().get("stripe-signature");
  const event = stripe.webhooks.constructEvent(body, sig, webhookSecret);

  // Handle various webhook events
  switch (event.type) {
    case "customer.subscription.created":
      // Handle new subscription
      break;
    case "customer.subscription.updated":
      // Handle subscription updates
      break;
    case "customer.subscription.deleted":
      // Handle subscription cancellation
      break;
    case "payment_intent.succeeded":
      // Handle successful payments
      break;
    case "payment_intent.payment_failed":
      // Handle failed payments
      break;
  }
}
```

## 5. Frontend Implementation

### 5.1 Subscription Management Component

```javascript
// In your settings or subscription page
const handleUpgrade = async () => {
  const response = await fetch("/api/stripe/create-checkout", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify({
      priceId:
        selectedPlan === "monthly"
          ? process.env.STRIPE_MONTHLY_PRICE_ID
          : process.env.STRIPE_YEARLY_PRICE_ID,
    }),
  });

  const { url } = await response.json();
  window.location.href = url;
};

const handleManageSubscription = async () => {
  const response = await fetch("/api/stripe/create-portal", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  const { url } = await response.json();
  window.location.href = url;
};
```

## 6. Webhook Setup

1. Install the Stripe CLI
2. Forward webhooks locally:

```bash
stripe listen --forward-to localhost:3000/api/stripe/webhook
```

3. Configure webhook endpoints in Stripe Dashboard with these events:

- customer.subscription.created
- customer.subscription.updated
- customer.subscription.deleted
- customer.subscription.trial_will_end
- payment_intent.succeeded
- payment_intent.payment_failed

## 7. Testing

1. Use Stripe test mode and test cards
2. Test webhook handling using the Stripe CLI
3. Verify subscription lifecycle:
   - Creation
   - Updates
   - Cancellation
   - Failed payments
   - Successful payments

## 8. Security Considerations

1. Always verify webhook signatures
2. Store Stripe customer IDs securely
3. Never log complete payment details
4. Use environment variables for sensitive data
5. Implement proper error handling
6. Verify user authentication before subscription management

## 9. Monitoring and Maintenance

1. Monitor webhook processing
2. Track failed payments
3. Handle subscription status changes
4. Maintain customer portal sessions
5. Keep Stripe libraries updated

This setup provides a complete subscription system with:

- Monthly and yearly subscription options
- Customer portal for subscription management
- Webhook handling for subscription lifecycle events
- Proper error handling and security measures
- Database tracking of subscription status

Remember to test thoroughly in Stripe's test mode before going live with real payments.
