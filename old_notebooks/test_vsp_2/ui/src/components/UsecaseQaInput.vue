<script lang="ts" setup>
import { useUsecaseQaInputStore } from '@/stores/usecaseQaInput'
import { AaButton } from '@aleph-alpha/ds-components-vue'
import { computed } from 'vue'

const props = withDefaults(
  defineProps<{
    usecaseId: string
    requestProcessing: boolean
  }>(),
  {
    usecaseId: 'default',
    requestProcessing: false,
  },
)

const emit = defineEmits<{
  clearAll: []
  onSubmit: [usecaseId: string, question: string, file?: File, collection?: string]
}>()

const usecaseQaInputStore = useUsecaseQaInputStore()

const isSendButtonDisabled = computed(() => {
  const { question } = usecaseQaInputStore.getUsecaseState(props.usecaseId)

  const isQuestionEmpty = question.trim() === ''
  const isRequestInProgress = props.requestProcessing
  return isQuestionEmpty || isRequestInProgress
})

const onSend = async () => {
  const usecaseState = usecaseQaInputStore.getUsecaseState(props.usecaseId)
  emit(
    'onSubmit',
    props.usecaseId,
    usecaseState.question,
    usecaseState.selectedFile,
    usecaseState.selectedCollection?.value,
  )
  usecaseQaInputStore.setQuestion(props.usecaseId, '')
}
</script>

<template>
  <div
    class="p-L h-27.75 bg-core-bg-tertiary border-core-border-default hover:border-core-content-secondary [&:has(textarea:focus)]:border-core-border-focus flex flex-col rounded-tl rounded-tr border [&:has(textarea:focus)]:border-2 [&:has(textarea:focus)]:p-[calc(theme(spacing.L)-1px)]"
  >
    <textarea
      v-model="usecaseQaInputStore.getUsecaseState(usecaseId).question"
      aria-label="question-input"
      :placeholder="'Ask a question'"
      class="text-core-content-secondary bg-core-bg-primary placeholder-core-content-placeholder h-full w-full resize-none focus:outline-none"
      @keydown.enter.prevent="!isSendButtonDisabled && onSend()"
    />
    <div class="text-size-sm flex w-full flex-row justify-between">
      <div class="flex-row justify-start">
        <!--        Empty diff to keep layout-->
      </div>
      <div class="gap-x-XS flex flex-row justify-end">
        <AaButton class="shrink-0" size="small" variant="text" @click="emit('clearAll')">
          {{ 'Clear all' }}
        </AaButton>
        <AaButton
          class="shrink-0"
          :disabled="isSendButtonDisabled"
          :loading="requestProcessing"
          append-icon="i-material-symbols-arrow-forward-rounded text-sm"
          size="small"
          variant="primary"
          @click="onSend()"
        >
          {{ 'Send' }}
        </AaButton>
      </div>
    </div>
  </div>
</template>
