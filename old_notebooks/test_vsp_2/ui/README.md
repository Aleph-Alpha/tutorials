# My Application UI

## Core Development Guidelines

### Store Management

> [!WARNING]
> 🔑 Always use `createStoreId` from [createStoreId.ts](../../base/ui/src/stores/createStoreId.ts)
> to generate unique Pinia store IDs and prevent collisions.

### Notifications System

✨ Trigger notifications using the `notificationEventBus` from [eventBus.ts](../../base/ui/src/@core/utils/eventBus.ts):

```ts
notificationEventBus.emit({
  type: 'success',
  message: 'Action completed',
  timeout: 5000,
  action: {
    label: 'Undo',
    callback: () => console.log('Undo triggered'),
  },
})
```

### Localization

🌍 Leverage Assistant's built-in [vue-i18n](https://kazupon.github.io/vue-i18n/) integration for translations.

## 🛠 Development Commands

Ensure the environment variables listed in the [.env](.env) file are set before running any commands.

### Development Essentials

```sh
# Install dependencies
pnpm install

# Start dev server
pnpm run dev

# Production build
pnpm run build
```

### Testing & Linting

```sh
# Unit tests (Vitest)
pnpm run test:unit

# First-time browser setup for E2E tests
npx playwright install

# E2E tests (Playwright)
pnpm run test:e2e
# Interactive mode
pnpm run test:e2e --ui

# Lint & format
pnpm run lint
pnpm run format
```
