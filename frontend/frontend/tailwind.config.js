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

// https://coolors.co/fde65e-313131-ffffff-0257d5-267dfd


	theme: {
		extend: {
			colors: {
				"primary-muted": "oklch(var(--primary-muted) / <alpha-value>)",
				"htlyellow": "#fde65e",
				"lighttext": "#FAFAFA"
			},
		},
	 },
	
	daisyui: {
		themes: [
			{
			light: {
				"htlyellow": "#FDE65E",			
				// "secondary": "#313131",	
				"secondary": "#202937",			
				"accent": "#FEEF9A",				
				"background": "#FAFAFA",	
				"info": "#5E9CFF",			
				"success": "#00d17a",
				"warning": "#FF7F11",			
				"error": "#E3170A",
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

