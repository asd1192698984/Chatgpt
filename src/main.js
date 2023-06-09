import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'

import ElementUI from 'element-plus'
import 'element-plus/dist/index.css'
// import 'element-plus/lib/theme-chalk/index.css'

createApp(App).use(ElementUI).mount('#app')
