import { getDesignSystemContentPathConfig, presetAlephAlpha } from '@aleph-alpha/config-css'
import { presetAlephAlphaIcons } from '@aleph-alpha/ds-icons'
import { defineConfig } from 'unocss'

export default defineConfig({
  ...getDesignSystemContentPathConfig('vue'),
  presets: [presetAlephAlpha(), presetAlephAlphaIcons()],
})
