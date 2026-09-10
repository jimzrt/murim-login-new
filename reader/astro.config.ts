import { defineConfig } from "astro/config";
import { satteri } from "@astrojs/markdown-satteri";
import { systemWindows } from "./src/plugins/system-windows";

function siteUrl(): string {
  return process.env.ASTRO_SITE ?? "https://murim-login.local";
}

function siteBase(): string {
  const raw = process.env.ASTRO_BASE ?? "/";
  if (!raw || raw === "/") {
    return "/";
  }
  return `/${raw.replace(/^\/+|\/+$/g, "")}/`;
}

export default defineConfig({
  site: siteUrl(),
  base: siteBase(),
  trailingSlash: "always",
  outDir: process.env.ASTRO_OUT_DIR ?? "../build/html",
  compressHTML: true,
  prefetch: true,
  redirects: {
    "/chapters/": "/",
  },
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
