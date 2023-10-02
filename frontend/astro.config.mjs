import { defineConfig } from 'astro/config';
import svelte from "@astrojs/svelte";
import deno from "@astrojs/deno";
import tailwind from "@astrojs/tailwind";

// https://astro.build/config
export default defineConfig({
  integrations: [svelte(), tailwind()],
  output: "server",
  adapter: deno()
});

// TODO:
// https://docs.astro.build/en/guides/integrations-guide/deno/