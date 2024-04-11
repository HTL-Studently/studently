// Imports ENV Vars, creates a config var and exports it mainly for /lib/auth/services.ts

// Imports from the .env file stopped working
// import {
// 	CLIENT_ID,
// 	CLOUD_INSTANCE,
// 	TENANT_ID,
// 	CLIENT_SECRET,
// } from "$env/static/private";


const CLIENT_ID = "https://login.microsoftonline.com/"
const CLOUD_INSTANCE = "2b197efa-8e1b-4680-b263-8e237889b5b3"
const TENANT_ID = "a9c7cdfe-635e-47d1-b6ca-1682a47d473c"
const CLIENT_SECRET = "e9s8Q~l3oyyxVzxD2mCTZ9B-tsWceirCQRcj.bKY"
const REDIRECT_URI = "http://localhost:5173/callback"


export const msalConfig = {
	auth: {
		clientId: CLIENT_ID,
		authority: CLOUD_INSTANCE + TENANT_ID,
		clientSecret: CLIENT_SECRET,
	},
};



// CLOUD_INSTANCE="https://login.microsoftonline.com/"
// TENANT_ID="2b197efa-8e1b-4680-b263-8e237889b5b3"
// CLIENT_ID="a9c7cdfe-635e-47d1-b6ca-1682a47d473c"
// CLIENT_SECRET="e9s8Q~l3oyyxVzxD2mCTZ9B-tsWceirCQRcj.bKY"
// REDIRECT_URI="http://localhost:5173/callback"
