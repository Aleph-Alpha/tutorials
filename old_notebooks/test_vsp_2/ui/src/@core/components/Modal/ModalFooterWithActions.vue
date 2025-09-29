<script lang="ts" setup>
import { AaButton, AaText } from '@aleph-alpha/ds-components-vue'
import { ref } from 'vue'

withDefaults(
  defineProps<{
    actionButtonText?: string
    actionButtonPrependIcon?: string
    actionButtonLoading?: boolean
    actionButtonDisabled?: boolean
    cancelButtonText?: string
    withCheckbox?: boolean
  }>(),
  {
    actionButtonText: '',
    actionButtonPrependIcon: '',
    actionButtonLoading: false,
    actionButtonDisabled: false,
    cancelButtonText: 'Cancel',
    withCheckbox: false,
  },
)

const emit = defineEmits<{
  cancel: []
  action: [checkboxChecked: boolean]
}>()

const isChecked = ref(false)
</script>
<template>
  <div class="gap-M bg-core-bg-tertiary flex rounded-b">
    <div class="gap-XS relative flex grow flex-row justify-start self-center">
      <div v-if="withCheckbox">
        <label class="gap-x-XS flex flex-row items-center" for="modal-footer-checkbox">
          <input
            id="modal-footer-checkbox"
            v-model="isChecked"
            class="size-5 rounded"
            type="checkbox"
          />
          <AaText class="text-core-content-tertiary" size="xs">
            {{ "Don't show again" }}
          </AaText>
        </label>
      </div>
    </div>
    <div :class="'gap-M flex flex-row justify-end'">
      <AaButton type="button" variant="text" @click="emit('cancel')">
        <AaText size="sm" weight="regular">
          {{ cancelButtonText }}
        </AaText>
      </AaButton>
      <AaButton
        :loading="actionButtonLoading"
        :disabled="actionButtonDisabled"
        :prepend-icon="actionButtonPrependIcon"
        @click="emit('action', isChecked)"
      >
        {{ actionButtonText }}
      </AaButton>
    </div>
  </div>
</template>
