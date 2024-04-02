import { redirect } from "@sveltejs/kit";
import type { RequestHandler } from "./$types";
import { getLogoutUri, cookiesConfig } from "$lib/auth/services";

export const GET: RequestHandler = async ({ cookies }) => {
  cookies.delete("accessToken", cookiesConfig);
  cookies.delete("idToken", cookiesConfig);
  cookies.delete("account", cookiesConfig);

  throw redirect(302, getLogoutUri());
};