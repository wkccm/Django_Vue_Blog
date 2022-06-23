import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import $ from 'jquery'

URLSearchParams.prototype.appendIfExists = function (key, value) {
    if (value !== null && value !== undefined) {
        this.append(key, value)
    }
};


createApp(App).use(router).mount('#app');
// createApp(App).mount('#app')
