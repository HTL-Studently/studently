import { redirect, type Handle } from "@sveltejs/kit";
import { redirectToAuthCodeUrl } from "$lib/auth/services";

export const handle: Handle = async ({ event, resolve }) => {
	if (event.route.id && event.route.id.indexOf("(protected)") > 0) {

		// Checks if user is authenticated when opening a page
		if (!event.cookies.get("idTokenJWT") || !event.cookies.get("accessTokenJWT")) {
			const authCodeUrl = await redirectToAuthCodeUrl(event);
			if (authCodeUrl) throw redirect(302, authCodeUrl);
		}
	}
	return await resolve(event);
};