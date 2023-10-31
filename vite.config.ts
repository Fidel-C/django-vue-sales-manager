import { defineConfig } from "vite";
import { resolve } from "path";
import vue from "@vitejs/plugin-vue";
import { quasar, transformAssetUrls } from '@quasar/vite-plugin'




export default defineConfig({
  root: resolve("./static/src"),
  base: "/static/",
  //the vue template transformAssetUrls is a quasar specific setting
  plugins: [vue({
    template: { transformAssetUrls }
  }),
      // @quasar/plugin-vite options list:
    // https://github.com/quasarframework/quasar/blob/dev/vite-plugin/index.d.ts
    quasar({
      sassVariables: './static/src/quasar-variables.sass'
    })


  ],
  build: {
    outDir: resolve("./static/dist"),
    assetsDir: "",
    manifest: true,
    emptyOutDir: true,
    rollupOptions: {
      // Overwrite default .html entry to main.ts in the static directory
      input: resolve("./static/src/main.ts"),
      
    },
  },
});