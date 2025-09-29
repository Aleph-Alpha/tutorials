<script lang="ts" setup>
import { AaSkeletonLoading } from '@aleph-alpha/ds-components-vue'
import { computed } from 'vue'

const props = defineProps<{ barCount: number; barHeightPx: number }>()

const progressWidths = [100, 80, 95, 100, 85] as const

const progressBars = computed<number[]>(() =>
  Array(Math.ceil(props.barCount / progressWidths.length))
    .fill(progressWidths)
    .flat()
    .slice(0, props.barCount),
)
const computedHeight = computed(() => `${props.barHeightPx}px`)
</script>

<template>
  <div class="flex flex-col w-full">
    <div
      v-for="(width, index) in progressBars"
      :key="index"
      :style="{ width: `${width}%`, height: computedHeight }"
    >
      <AaSkeletonLoading class="rounded" />
    </div>
  </div>
</template>
