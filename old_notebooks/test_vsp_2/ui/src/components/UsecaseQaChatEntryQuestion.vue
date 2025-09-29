<script setup lang="ts">
import { AaButton, AaProfileIcon } from '@aleph-alpha/ds-components-vue'
import { computed } from 'vue'

const props = defineProps<{
  question: string
  timestamp: Date
}>()

const emit = defineEmits<{
  delete: []
}>()

const displayDate = computed<string>(() =>
  props.timestamp.toLocaleDateString('en-GB', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
  }),
)
const displayTime = computed<string>(() =>
  props.timestamp.toLocaleTimeString('default', {
    hour: '2-digit',
    minute: '2-digit',
    hour12: false,
  }),
)
</script>

<template>
  <div
    class="p-M gap-XS bg-core-bg-primary border-core-border-default flex h-fit w-fit rounded border"
  >
    <AaProfileIcon :user-name="'User'" class="size-8 flex-shrink-0 text-xs" :disabled="true" />
    <div class="flex items-center">
      <span class="space-x-L">
        <span class="text-core-content-primary">{{ question }}</span>
        <span class="text-core-content-tertiary text-sm">{{ displayDate }}</span>
        <span class="text-core-content-tertiary text-sm">{{ displayTime }}</span>
      </span>
    </div>
    <AaButton
      class="h-8"
      type="button"
      variant="text"
      aria-label="remove-question-button"
      @click="emit('delete')"
    >
      <span class="i-material-symbols-close text-sm" />
    </AaButton>
  </div>
</template>
