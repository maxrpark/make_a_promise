import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

import axios from 'axios';
axios.defaults.baseURL = 'https://maxicode.pythonanywhere.com/';

createApp(App).use(router, axios).mount('#app');

// axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
// axios.defaults.xsrfCookieName = 'csrftoken';
// axios.defaults.withCredentials = false;
// axios.defaults.baseURL = 'http://127.0.0.1:8000/';
