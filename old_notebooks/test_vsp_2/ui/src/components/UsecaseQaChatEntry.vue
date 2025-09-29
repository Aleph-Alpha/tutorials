<script lang="ts" setup>
import UsecaseQaChatEntryAnswer from '@/components/UsecaseQaChatEntryAnswer.vue'
import UsecaseQaChatEntryQuestion from '@/components/UsecaseQaChatEntryQuestion.vue'
import { type UsecaseQaChatEntry } from '@/models/UsecaseQaChatEntry'

interface UsecaseQaChatEntryProps {
  chatEntry: UsecaseQaChatEntry
}

defineProps<UsecaseQaChatEntryProps>()

const emit = defineEmits<{
  delete: [id: string]
}>()
</script>

<template>
  <div class="gap-M grid grid-cols-1" aria-label="question-answer-card">
    <UsecaseQaChatEntryQuestion
      :question="chatEntry.question"
      :timestamp="chatEntry.timestamp"
      @delete="emit('delete', chatEntry.questionId)"
    />
    <UsecaseQaChatEntryAnswer :chat-entry="chatEntry" />
  </div>
</template>
