import { createApp } from 'vue'
import { createPinia } from 'pinia'
import AADesignSystem from '@aleph-alpha/ds-components-vue'
import '@unocss/reset/tailwind.css'
import 'virtual:uno.css'

import App from './App.vue'

const app = createApp(App)

// @ts-expect-error AADesignSystem is a plugin, but it's not typed as such in the package.
app.use(AADesignSystem)
app.use(createPinia())

app.mount('#app')
