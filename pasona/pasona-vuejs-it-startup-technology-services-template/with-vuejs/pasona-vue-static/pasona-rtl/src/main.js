import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import Toaster from "@meforma/vue-toaster";
import VueFeather from "vue-feather";

import "./assets/custom.scss";

const app = createApp(App);

app.component(VueFeather.name, VueFeather).use(router).use(store).use(Toaster);
app.mount("#app");
