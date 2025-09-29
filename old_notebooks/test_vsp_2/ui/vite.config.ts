import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'
import federation from '@originjs/vite-plugin-federation'
import UnoCSS from 'unocss/vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
    federation({
      name: 'application',
      filename: 'usecase.js',
      exposes: {
        './Usecase': './src/App.vue',
      },
      shared: {
        vue: {},
        pinia: {},
        'vue-router': {},
        '@aleph-alpha/ds-components-vue': { version: '*' },
        '@aleph-alpha/lib-http': { version: '*' },
      },
    }),
    UnoCSS(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
  build: {
    target: 'esnext',
    cssCodeSplit: false,
  },
})
