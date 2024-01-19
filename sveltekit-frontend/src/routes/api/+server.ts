import { json } from '@sveltejs/kit'
import { getAccessTokenStore } from "$lib/auth/services.js"



export async function GET() {
	try {
		const tokens = await getAccessTokenStore();
		return new Response(tokens, {
			headers: {
				'Content-Type': 'application/json',
			},
		});
	} catch (error) {
		console.error('Error:', error);
		return new Response('Internal Server Error', { status: 500 });
	}
}