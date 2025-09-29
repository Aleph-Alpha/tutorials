<script lang="ts" setup>
import SkillLayout from '@/@core/layouts/SkillLayout.vue'
import { HTTP_CLIENT } from '@/utils/http.ts'
import { onMounted } from 'vue'
import { useUsecaseQaStore } from '@/stores/usecaseQa.ts'
import { useUsecaseQaChatStore } from '@/stores/usecaseQaChat.ts'
import UsecaseQaInput from '@/components/UsecaseQaInput.vue'
import UsecaseQaChatEntry from '@/components/UsecaseQaChatEntry.vue'
import UsecaseQaTopBanner from '@/components/UsecaseQaTopBanner.vue'
import ModalActionWithCheckbox from '@/@core/components/Modal/ModalActionWithCheckbox.vue'

const props = withDefaults(
  defineProps<{
    userToken: string
    serviceBaseUrl?: string
  }>(),
  {
    userToken: import.meta.env.VITE_USER_TOKEN || '',
    serviceBaseUrl: import.meta.env.VITE_SERVICE_BASE_URL || '',
  },
)

const usecaseId = 'default'

const usecaseQaChatStore = useUsecaseQaChatStore()
const usecaseQaStore = useUsecaseQaStore()

function onDeleteChatHistory() {
  usecaseQaChatStore.deleteChatHistory.callActionOrOpenModal(deleteChatHistory)
}

function onConfirmDeleteChatHistory(checkboxChecked: boolean) {
  usecaseQaChatStore.deleteChatHistory.getConfirmActionCallback(deleteChatHistory)(checkboxChecked)
}

async function deleteChatHistory() {
  usecaseQaChatStore.clearChat(usecaseId)
}

async function onDeleteChatHistoryItem(idToDelete: string) {
  usecaseQaChatStore.deleteEntry(usecaseId, idToDelete)
}

const onSubmit = async (usecaseId: string, question: string) => {
  await usecaseQaStore.submitQuestion(usecaseId, question)
}

onMounted(() => {
  HTTP_CLIENT.updateConfig({ baseURL: props.serviceBaseUrl })
  HTTP_CLIENT.setBearerToken(props.userToken)
})
</script>

<template>
  <Teleport v-if="usecaseQaChatStore.deleteChatHistory.showModal" to="body">
    <ModalActionWithCheckbox
      :title="'Delete chat history'"
      :cancel-button-text="'Cancel'"
      :confirm-button-text="'Delete'"
      :content="'Are you sure you want to delete the chat history?'"
      @cancel="usecaseQaChatStore.deleteChatHistory.onCloseModal"
      @close="usecaseQaChatStore.deleteChatHistory.onCloseModal"
      @confirm="onConfirmDeleteChatHistory"
    />
  </Teleport>
  <UsecaseQaTopBanner />
  <SkillLayout :skill-title="'QA Usecase'">
    <div class="flex h-[calc(100%_-_157px)] w-full flex-row items-center">
      <section
        class="p-y-XL w-182 mx-auto flex h-full flex-col justify-between self-stretch overflow-y-hidden"
      >
        <div class="w-full flex-col overflow-y-auto">
          <div class="flex h-full w-full flex-col-reverse gap-10 overflow-y-auto">
            <UsecaseQaChatEntry
              v-for="item in usecaseQaChatStore.reversedChatHistory(usecaseId)"
              :key="item.questionId"
              :chat-entry="item"
              @delete="onDeleteChatHistoryItem($event)"
            />
          </div>
        </div>
        <div class="w-full flex-col">
          <UsecaseQaInput
            :usecase-id="usecaseId"
            :request-processing="usecaseQaStore.isProcessingRequest[usecaseId]"
            @on-submit="onSubmit"
            @clear-all="onDeleteChatHistory"
          />
        </div>
      </section>
    </div>
  </SkillLayout>
</template>

<style lang="scss">
:root {
  font-family: Raleway, sans-serif, ui-sans-serif;
}
</style>
