<script lang="ts" setup>
import ActionButton from '@/@core/components/ActionButton.vue'
import { type UsecaseQaChatEntry } from '@/models/UsecaseQaChatEntry'
import { copyToClipboard } from '@/@core/utils/copyToClipboard.ts'

defineProps<{
  chatEntry: UsecaseQaChatEntry
}>()
</script>
<template>
  <div class="flex-shrink-0">
    <!--    Empty diff to keep layout-->
  </div>
  <div class="p-XS flex flex-shrink-0 flex-row">
    <ActionButton
      :tooltip="'Copy answer'"
      label="copy-answer-button"
      size="sm"
      variant="copy"
      @action="copyToClipboard(chatEntry.answer.answer ?? '')"
    />
  </div>
</template>
