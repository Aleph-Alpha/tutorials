<script lang="ts" setup>
import UsecaseQaAnswerActions from './UsecaseQaAnswerActions.vue'
import SkeletonPlaceholderContainer from '@/@core/components/SkeletonPlaceholderContainer.vue'
import { UsecaseQaAnswerStatus, type UsecaseQaChatEntry } from '@/models/UsecaseQaChatEntry'
import { AaText } from '@aleph-alpha/ds-components-vue'

defineProps<{
  chatEntry: UsecaseQaChatEntry
}>()
</script>

<template>
  <div class="w-179 p-M gap-XS text-core-content-primary flex grow rounded">
    <div
      class="border-core-border-default flex size-8 flex-shrink-0 items-center justify-center rounded-full border"
    >
      <span class="i-aa-logo flex size-4 flex-shrink-0" />
    </div>
    <SkeletonPlaceholderContainer
      v-if="chatEntry.answer.status === UsecaseQaAnswerStatus.PENDING"
      :bar-count="4"
      :bar-height-px="32"
      class="gap-y-lg"
    />
    <div v-else class="flex w-full flex-col justify-center">
      <AaText element="div" class="whitespace-pre-line">
        {{ chatEntry.answer.answer || 'No answer found' }}
      </AaText>
      <div class="pt-L text-core-content-tertiary flex items-center justify-between">
        <UsecaseQaAnswerActions :chat-entry="chatEntry" />
      </div>
    </div>
  </div>
</template>
