import { createApp } from 'vue'
import App from '@/App.vue'
import router from '@/router'
import store from '@/store'
import components from '@/components/ui'

components.forEach(component => {
    app.component(component.name, component)
})

const app = createApp(App)
app.use(store)
app.use(router)
app.mount('#app')
