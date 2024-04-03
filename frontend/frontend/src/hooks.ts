import { redirect, type Handle, type RequestHandler, type HandleFetch } from "@sveltejs/kit";
import { redirectToAuthCodeUrl } from "$lib/auth/services";

export const handle: Handle = async ({ event, resolve }) => {
	if (event.route.id && event.route.id.indexOf("(protected)") > 0) {
		const accessToken = event.cookies.get("accessTokenJWT")
		const idToken = event.cookies.get("idTokenJWT")

		// Checks if user is authenticated when opening a page
		if (!idToken || !accessToken) {
			const authCodeUrl = await redirectToAuthCodeUrl(event);
			if (authCodeUrl) throw redirect(302, authCodeUrl);
		}
	}
	return await resolve(event);
};


/** @type {import('@sveltejs/kit').HandleFetch} */
export async function handleFetch({ event, request, fetch }) {
	// Handle GET requests
	if (request.method === "POST") {

		const accessToken = event.cookies.get("accessTokenJWT"); 


		let newRequest = new Request(request, {
			headers: new Headers(request.headers),
		}) 

		// Set Headers		
		newRequest.headers.set('Authorization', `Bearer ${accessToken}`);

		return fetch(newRequest)
	}
}