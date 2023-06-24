import { createApp } from 'vue'
import App from '@/App.vue'
import router from '@/router'
import store from '@/store'
import components from '@/components/ui'

const app = createApp(App)

components.forEach(component => {
    app.component(component.name, component)
})

app.use(store)
app.use(router)
app.mount('#app')
