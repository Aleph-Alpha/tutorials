<script lang="ts" setup>
import { AaButton, AaTooltip } from '@aleph-alpha/ds-components-vue'
import { computed, ref } from 'vue'

const anchor = ref()

const emit = defineEmits<{
  action: []
}>()

const variantIcons: Record<string, string> = {
  clear: 'i-material-symbols-close',
  copy: 'i-material-symbols-content-copy-outline',
  download: 'i-material-symbols-download',
}

const textSizeClasses: Record<string, string> = {
  sm: 'text-sm',
  base: 'text-base',
}

const props = withDefaults(
  defineProps<{
    variant: 'clear' | 'copy' | 'download'
    tooltip: string
    label: string
    size?: 'sm' | 'base'
  }>(),
  {
    size: 'sm',
  },
)

const iconClasses = computed(() => {
  const baseClass = variantIcons[props.variant]
  const sizeClass = textSizeClasses[props.size]
  return `${baseClass} ${sizeClass} 'place-self-center'`
})
</script>

<template>
  <AaButton
    ref="anchor"
    :aria-label="label"
    class="border-none hover:bg-core-bg-tertiary-hover text-core-content-accent-soft"
    v-bind="$attrs"
    variant="text"
    @click="emit('action')"
  >
    <span :class="iconClasses" class="text-core-content-tertiary" />
  </AaButton>
  <AaTooltip :anchor="anchor">
    {{ tooltip }}
  </AaTooltip>
</template>
