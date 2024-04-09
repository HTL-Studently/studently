// import jwt from 'jsonwebtoken';
// import jwtDecode from 'jwt-decode';
import dotenv from 'dotenv';
import type { RequestEvent } from "@sveltejs/kit";
import {
	ConfidentialClientApplication,
	CryptoProvider,
	ResponseMode,
} from "@azure/msal-node";
// import { REDIRECT_URI } from "$env/static/private";



// import { msalConfig } from "./config";

const CLOUD_INSTANCE="https://login.microsoftonline.com/"
const TENANT_ID="2b197efa-8e1b-4680-b263-8e237889b5b3"
const CLIENT_ID="a9c7cdfe-635e-47d1-b6ca-1682a47d473c"
const CLIENT_SECRET="e9s8Q~l3oyyxVzxD2mCTZ9B-tsWceirCQRcj.bKY"
const REDIRECT_URI="http://localhost:5173/callback"



export const msalConfig = {
	auth: {
		clientId: CLIENT_ID,
		authority: CLOUD_INSTANCE + TENANT_ID,
		clientSecret: CLIENT_SECRET,
	},
};






dotenv.config();

const msalInstance = new ConfidentialClientApplication(msalConfig);
const cryptoProvider = new CryptoProvider();

let tokenResponse:any = 0;


// const generateJWT = async (data: any) => {
// 	return jwt.sign(data, "secret_key", {expiresIn: "1h"});

// 	// REWRITE

// 	const response = await fetch('/generate-jwt', {
// 		method: 'POST',
// 		headers: {
// 		  'Content-Type': 'application/json',
// 		},
// 		body: JSON.stringify(data),
// 	  });
// 	  const token = await response.text();
// 	  return token;
// }

// export const readJWTCookies = (event: RequestEvent) => {
// 	let jwtCookie = event.cookies.get("accessTokenJWT")
// 	console.log("JWT COOKIE: ", jwtCookie)
// 	return jwtCookie

// }

export const cookiesConfig = {
	httpOnly: true,
	path: "/",
	secure: true,
	sameSite: "strict",
	expires: new Date(Date.now() + 10 * 60 * 1000),
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
	// const verifierJWT = generateJWT({ verifier })
	// const csrfTokenJWT = generateJWT({ csrfToken })



	try {
		const authCodeUrl = await msalInstance.getAuthCodeUrl(authCodeUrlRequest);
		
		event.cookies.set("pkceVerifier", verifier, cookiesConfig);
		event.cookies.set("csrfToken", csrfToken, cookiesConfig);
		
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
		// Old jwt workflow
		// const csrfTokenJwt = event.cookies.get("csrfTokenJWT")
		// const pkceVerifierJWT = event.cookies.get("pkceVerifierJWT")

		// const pkceVerifier = jwtDecode(pkceVerifierJWT).verifier;
		// const csrfToken = jwtDecode(csrfTokenJwt).csrfToken;

		const csrfToken = event.cookies.get("csrfToken")
		const pkceVerifier = event.cookies.get("pkceVerifier")


		// if (decodedState.csrfToken === csrfToken) {
		if(true) {	
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

					// Generate Cookies
					event.cookies.set("accessToken", tokenResponse.accessToken, cookiesConfig);
					event.cookies.set("idToken", tokenResponse.idToken, cookiesConfig);

					console.log("REDIRECT: ", decodedState.redirectTo)

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

export const getLogoutUri = () => {
	return `${msalConfig.auth.authority}/oauth2/v2.0/logout`;
};