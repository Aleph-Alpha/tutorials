<script lang="ts" setup>
withDefaults(
  defineProps<{
    hasError?: boolean
  }>(),
  {
    hasError: false,
  },
)
</script>

<template>
  <section
    :class="[
      'gap-XL p-3XL bg-core-bg-tertiary flex flex-1 flex-col self-stretch border',
      hasError
        ? 'border-semantic-border-error'
        : 'border-core-border-default hover:border-core-content-secondary [&:has(textarea:focus)]:border-core-border-focus [&:has(textarea:focus)]:border-2 [&:has(textarea:focus)]:p-[calc(theme(spacing.3XL)-1px)]',
    ]"
  >
    <div v-if="$slots.header" class="flex h-6 w-full justify-between">
      <slot name="header" />
    </div>
    <div class="flex grow gap-3 self-stretch">
      <slot name="main" />
    </div>
    <div class="flex h-8 items-center">
      <slot name="footer" />
    </div>
  </section>
</template>
