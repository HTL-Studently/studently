import jwt from 'jsonwebtoken';
import dotenv from 'dotenv';
import type { RequestEvent } from "@sveltejs/kit";
import {
	ConfidentialClientApplication,
	CryptoProvider,
	ResponseMode,
} from "@azure/msal-node";
// import { REDIRECT_URI } from "$env/static/private";
const REDIRECT_URI = "http://localhost:5173/callback" // Needs to become dynamic
import { dev } from "$app/environment";
import { msalConfig } from "./config";
import { sendUserLogin } from "$lib/api/services"

dotenv.config();

const msalInstance = new ConfidentialClientApplication(msalConfig);
const cryptoProvider = new CryptoProvider();

let tokenResponse:any = 0;

export function getAccessTokenStore() {
	return tokenResponse;
}

const generateJWT = (data: any) => {
	return jwt.sign(data, "secret_key", {expiresIn: "1h"});
}

export const cookiesConfig = {
	httpOnly: true,
	path: "/",
	secure: !dev,
	sameSite: "strict",
};

export const redirectToAuthCodeUrl = async (event: RequestEvent) => {
	const { verifier, challenge } = await cryptoProvider.generatePkceCodes();

	const pkceCodes = {
		challengeMethod: "S256",
		verifier,
		challenge,
	};


	const csrfToken = cryptoProvider.createNewGuid();
	
	const state = cryptoProvider.base64Encode(
		JSON.stringify({
			csrfToken,
			redirectTo: event.url.pathname,
		})
	);

	const authCodeUrlRequest = {
		redirectUri: REDIRECT_URI,
		responseMode: ResponseMode.QUERY,
		codeChallenge: pkceCodes.challenge,
		codeChallengeMethod: pkceCodes.challengeMethod,
		scopes: ["email", "offline_access", "profile", "User.Read"],
		state,
	};


	// Generate JWTs
	const verifierJWT = generateJWT({ verifier })
	const csrfTokenJWT = generateJWT({ csrfToken })



	try {
		const authCodeUrl = await msalInstance.getAuthCodeUrl(authCodeUrlRequest);
		
		event.cookies.set("pkceVerifierJWT", verifierJWT, cookiesConfig);
		event.cookies.set("csrfTokenJWT", csrfTokenJWT, cookiesConfig);
		
		return authCodeUrl;
	} catch (error) {
		console.log(error);
	}
};

export const getTokens = async (event: RequestEvent) => {
	// Gets visited subpage to reroute to it after authentication
	const state = event.url.searchParams.get("state");


	if (state) {
		const decodedState = JSON.parse(cryptoProvider.base64Decode(state));
		// const csrfToken = event.cookies.get("csrfToken");

		const csrfTokenJwt = event.cookies.get("csrfTokenJWT")
		const pkceVerifierJWT = event.cookies.get("pkceVerifierJWT")

		const pkceVerifier = jwt.verify(pkceVerifierJWT, "secret_key").verifier
		const csrfToken = jwt.verify(csrfTokenJwt, "secret_key").csrfToken


		if (decodedState.csrfToken === csrfToken) {
			const code = event.url.searchParams.get("code");
			const error = event.url.searchParams.get("error");
			if (code) {
				const authCodeRequest = {
					redirectUri: REDIRECT_URI,
					code,
					scopes: ["email", "offline_access", "profile", "User.Read"],
					codeVerifier: pkceVerifier,
				};

		
				try {
					tokenResponse = await msalInstance.acquireTokenByCode(
						authCodeRequest
					);

					const apiLoginResponse = sendUserLogin(tokenResponse.accessToken, tokenResponse.idToken)
						
					// Generate JWT Cookies
					event.cookies.set("accessTokenJWT", tokenResponse.accessToken, cookiesConfig);
					event.cookies.set("idTokenJWT", tokenResponse.idToken, cookiesConfig);

					return decodedState.redirectTo;

				} catch (error) {	
					console.log(error);
				}
			} else if (error) {
				throw new Error(error);
			}
		} else {
			throw new Error("CSRF token mismatch");
		}
	} else {
		throw new Error("State parameter missing");
	}
};

export const readJWTCookies = (event: RequestEvent) => {
	let jwtCookie = event.cookies.get("accessTokenJWT")
	console.log("JWT COOKIE: ", jwtCookie)
	return jwtCookie

}

export const getLogoutUri = () => {
	return `${msalConfig.auth.authority}/oauth2/v2.0/logout`;
};