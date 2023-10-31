import "vite/modulepreload-polyfill";
import { createApp, h } from "vue";
import { createInertiaApp } from "@inertiajs/inertia-vue3";

import { Quasar,Notify} from 'quasar'

// Import icon libraries
import '@quasar/extras/material-icons/material-icons.css'
import '@quasar/extras/material-icons-outlined/material-icons-outlined.css'
import '@quasar/extras/material-icons-round/material-icons-round.css'
import '@quasar/extras/mdi-v7/mdi-v7.css'
import '@quasar/extras/fontawesome-v5/fontawesome-v5.css'
import '@quasar/extras/fontawesome-v6/fontawesome-v6.css'
import '@quasar/extras/bootstrap-icons/bootstrap-icons.css'


// Import Quasar css
import 'quasar/src/css/index.sass'



createInertiaApp({
  resolve: (name) => import(`./pages/${name}.vue`),
  setup({ el, app, props, plugin }) {
    createApp({ render: () => h(app, props) })
      .use(plugin)
      .use(Quasar, {
        plugins: {Notify},  
        // import Quasar plugins and add here
})
      .mount(el);
  },
});


