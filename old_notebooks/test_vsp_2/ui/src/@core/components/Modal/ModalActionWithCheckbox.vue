<script lang="ts" setup>
import ModalFooterWithActions from '@/@core/components/Modal/ModalFooterWithActions.vue'
import { AaModal, AaText } from '@aleph-alpha/ds-components-vue'

defineProps<{
  title: string
  content: string
  cancelButtonText: string
  confirmButtonText: string
}>()

const emit = defineEmits<{
  close: []
  cancel: []
  confirm: [checkboxChecked: boolean]
}>()
</script>

<template>
  <AaModal
    :title
    :with-overlay="true"
    :with-dividers="false"
    class="w-143.5"
    @close="emit('close')"
  >
    <AaText class="text-core-content-secondary" size="sm">
      {{ content }}
    </AaText>
    <template #footer>
      <ModalFooterWithActions
        :with-checkbox="true"
        :cancel-button-text="cancelButtonText"
        :action-button-text="confirmButtonText"
        @cancel="emit('cancel')"
        @action="emit('confirm', $event)"
      />
    </template>
  </AaModal>
</template>
