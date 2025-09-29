<script setup lang="ts">
import { AaTopBanner } from '@aleph-alpha/ds-components-vue'
</script>

<template>
  <AaTopBanner variant="info" :soft="true" :with-close-button="false">
    <div class="gap-3XS flex items-center">
      <span class="i-material-symbols-info-outline"></span>
      <span class="text-sm">
        {{
          'Please note that the current functionality does not support the context of previous questions and answers.'
        }}
      </span>
    </div>
  </AaTopBanner>
</template>
