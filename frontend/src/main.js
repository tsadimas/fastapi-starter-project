import 'bootstrap/dist/css/bootstrap.css';
import { createApp } from "vue";
import axios from 'axios';

import App from './App.vue';
import router from './router';
import store from './store';
import { vueKeycloak } from '@baloise/vue-keycloak'


const app = createApp(App);

app.use(vueKeycloak, {
  initOptions: {
    flow: 'standard', // default
    checkLoginIframe: false, // default
    onLoad: 'login-required', // default
  },
  config: {
    url: 'http://keycloak:8080',
    realm: 'hulk',
    clientId: 'frontend-client'
  }
})

axios.defaults.withCredentials = true;
axios.defaults.baseURL = process.env.VUE_APP_BASE_URL;
console.log(process.env.VUE_APP_BASE_URL);
app.use(router);
app.use(store);
app.mount("#app");