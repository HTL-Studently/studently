import adapter from '@sveltejs/adapter-node';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	kit: {
		adapter: adapter()
	},

	preprocess: vitePreprocess(),
	
	vitePlugin: {
		// Allows you to hold ctrl+shift and click on an item in the browser and it then opens that components location in VSCode
		inspector: {
			holdMode: true
		},
	},
};

export default config;
