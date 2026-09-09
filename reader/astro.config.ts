import { defineConfig } from "astro/config";
import { satteri } from "@astrojs/markdown-satteri";
import { systemWindows } from "./src/plugins/system-windows";

export default defineConfig({
  site: "https://murim-login.local",
  trailingSlash: "always",
  outDir: process.env.ASTRO_OUT_DIR ?? "../build/html",
  compressHTML: true,
  build: {
    format: "directory",
  },
  markdown: {
    processor: satteri({
      hastPlugins: [systemWindows],
      features: {
        gfm: {
          footnotes: {
            backContent: "↩",
            backLabel: "Back to reference {reference}",
            label: "Footnotes",
          },
        },
      },
    }),
  },
});
