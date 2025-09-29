import { useModal } from '@/@core/composables/useModal'
import {
  UsecaseQaAnswerStatus,
  type UsecaseQaChatEntry,
  type UsecaseQaChatInitializationEntry,
} from '@/models/UsecaseQaChatEntry'
import { defineStore } from 'pinia'
import { ref } from 'vue'
import { z } from 'zod'

export const SUCCESSFUL_QA_ANSWER_SCHEMA = z.object({
  traceId: z.string(),
  answer: z.string().optional(),
})
export type SuccessfulQaAnswer = z.infer<typeof SUCCESSFUL_QA_ANSWER_SCHEMA>

const QA_CHAT_HISTORY_LIMIT = 1_000

export const useUsecaseQaChatStore = defineStore('usecase-qa-chat', () => {
  const chatHistory = ref<{ [key: string]: UsecaseQaChatEntry[] }>({})
  const deleteChatHistory = useModal()

  const createEntry = (usecaseId: string, partialChatEntry: UsecaseQaChatInitializationEntry) => {
    const questionId: string = crypto.randomUUID()

    if (!chatHistory.value[usecaseId]) {
      chatHistory.value[usecaseId] = []
    }

    chatHistory.value[usecaseId].push({
      ...partialChatEntry,
      questionId: questionId,
      timestamp: new Date(),
      answer: { status: UsecaseQaAnswerStatus.PENDING },
    })

    if (chatHistory.value[usecaseId].length > QA_CHAT_HISTORY_LIMIT) {
      chatHistory.value[usecaseId].shift()
    }

    return questionId
  }

  const reversedChatHistory = (usecaseId: string) =>
    chatHistory.value[usecaseId]?.slice().reverse() ?? []

  const addAnswer = (
    usecaseId: string,
    questionId: string,
    answer: Omit<SuccessfulQaAnswer, 'feedbackStatus'>,
  ) => {
    const entry = getEntry(usecaseId, questionId)
    entry.answer = {
      ...answer,
      status: UsecaseQaAnswerStatus.SUCCESSFUL,
    }
  }

  const flagEntryAsFailed = (usecaseId: string, questionId: string) => {
    const entry = getEntry(usecaseId, questionId)
    entry.answer = { status: UsecaseQaAnswerStatus.FAILED }
  }

  const getEntry = (usecaseId: string, questionId: string): UsecaseQaChatEntry => {
    const entry = chatHistory.value[usecaseId].find((entry) => entry.questionId === questionId)
    if (!entry) {
      console.error(`QA-pair with questionId ${questionId} not found`)
      throw new Error(`QA-pair with questionId ${questionId} not found`)
    }
    return entry
  }

  const deleteEntry = (usecaseId: string, questionId: string) =>
    (chatHistory.value[usecaseId] = chatHistory.value[usecaseId].filter(
      (entry) => entry.questionId !== questionId,
    ))

  const clearChat = (usecaseId: string) => (chatHistory.value[usecaseId] = [])

  return {
    chatHistory,
    reversedChatHistory,
    createEntry,
    addAnswer,
    flagEntryAsFailed,
    getEntry,
    deleteEntry,
    clearChat,
    deleteChatHistory,
    // exporting so this information is persisted
    deleteChatHistoryShouldBeHidden: deleteChatHistory.shouldBeHidden,
  }
})
