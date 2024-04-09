	/** @type {import('tailwindcss').Config} */
	export default {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	
	theme: {
		extend: {
			boxShadow: {
			'2':'inset 2em 0 15px -35px rgba(0, 0, 0, 0.3), inset -2em 0 15px -35px rgba(0, 0, 0, 0.3) '
			}
		},
	},

	plugins: [require('daisyui')],

	theme: {
		extend: {
		  colors: {
			"primary-muted": "oklch(var(--primary-muted) / <alpha-value>)",
			"htlyellow": "#fde65e",
		  },
		},
	 },
	
	daisyui: {
		themes: [
		  // light theme
		  {
			light: {
			  ...require("daisyui/src/theming/themes")["[data-theme=light]"],
			  "--primary-muted": "259 94% 71%",
			},
		  },
		  // cupcake theme
		  {
			cupcake: {
			  ...require("daisyui/src/theming/themes")["[data-theme=cupcake]"],
			  "--primary-muted": "183 47% 79%",
			},
		  },
		  // dark theme
		  {
			dark: {
			  ...require("daisyui/src/theming/themes")["[data-theme=dark]"],
			  "--primary-muted": "262 80% 30%",
			},
		  },
		],
	},
}

