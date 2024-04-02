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

	darkTheme: false,
}

