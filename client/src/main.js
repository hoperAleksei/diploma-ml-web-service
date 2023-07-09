import { createApp } from 'vue'
import App from '@/App.vue'

import router from '@/router'
import store from '@/store'
import vuetify from "@/plugins/vuetify";
import components from '@/components/ui'

const app = createApp(App)

components.forEach(component => {
    app.component(component.name, component)
})

app.use(vuetify, {
    iconfont: 'mdi'
})
app.use(store)
app.use(router)
app.mount('#app')
