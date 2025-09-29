import { type SelectOption } from '@aleph-alpha/ds-components-vue'
import { defineStore } from 'pinia'
import { ref } from 'vue'

interface UsecaseState {
  selectedFile?: File
  selectedCollection?: SelectOption
  question: string
}

export const useUsecaseQaInputStore = defineStore('usecase-qa-input', () => {
  const usecaseStates = ref<{ [key: string]: UsecaseState }>({})

  const getOrCreateUsecaseState = (usecaseId: string): UsecaseState => {
    if (!usecaseStates.value[usecaseId]) {
      usecaseStates.value[usecaseId] = {
        selectedFile: undefined,
        selectedCollection: undefined,
        question: '',
      }
    }
    return usecaseStates.value[usecaseId]
  }

  const setQuestion = (usecaseId: string, newQuestion: string): void => {
    const state = getOrCreateUsecaseState(usecaseId)
    state.question = newQuestion
  }

  return {
    setQuestion,
    getUsecaseState: getOrCreateUsecaseState,
    usecaseStates,
  }
})
