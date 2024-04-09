import { redirect, type Handle, type RequestHandler, type HandleFetch } from "@sveltejs/kit";
import { redirectToAuthCodeUrl } from "$lib/auth/services";

export const handle: Handle = async ({ event, resolve }) => {

	console.log(event.route)


	if (event.route.id && event.route.id.indexOf("(protected)") > 0) {
		const accessToken = event.cookies.get("accessToken")
		const idToken = event.cookies.get("idToken")

		// Checks if user is authenticated when opening a page
		if (!idToken || !accessToken) {
			const authCodeUrl = await redirectToAuthCodeUrl(event);
			if (authCodeUrl) throw redirect(302, authCodeUrl);
		}
	}
	return await resolve(event);
};