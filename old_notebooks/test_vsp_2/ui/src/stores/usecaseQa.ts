import { useUsecaseQaChatStore } from '@/stores/usecaseQaChat'
import { defineStore } from 'pinia'
import { ref } from 'vue'
import { CUSTOM_RAG_SERVICE } from '@/utils/http.ts'

export const useUsecaseQaStore = defineStore('usecase-qa', () => {
  const usecaseChatStore = useUsecaseQaChatStore()
  const isProcessingRequest = ref<{ [key: string]: boolean }>({})

  async function executeUsecase(usecaseId: string, question: string) {
    isProcessingRequest.value[usecaseId] = true

    const questionId = usecaseChatStore.createEntry(usecaseId, {
      question,
    })

    try {
      const response = await CUSTOM_RAG_SERVICE.customQa({ question: question })
      usecaseChatStore.addAnswer(usecaseId, questionId, {
        traceId: '',
        answer: response.answer,
      })
      isProcessingRequest.value[usecaseId] = false
    } catch (error) {
      usecaseChatStore.flagEntryAsFailed(usecaseId, questionId)
      isProcessingRequest.value[usecaseId] = false

      throw error
    }
  }

  const submitQuestion = async (usecaseId: string, question: string) => {
    if (!question) return
    await executeUsecase(usecaseId, question)
  }

  return {
    isProcessingRequest,
    submitQuestion,
  }
})
