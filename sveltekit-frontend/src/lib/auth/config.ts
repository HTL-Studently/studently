// Imports ENV Vars, creates a config var and exports it

// import {
// 	CLIENT_ID,
// 	CLOUD_INSTANCE,
// 	TENANT_ID,
// 	CLIENT_SECRET,
// } from "$env/static/private";

// export const msalConfig = {
// 	auth: {
// 		clientId: CLIENT_ID,
// 		authority: CLOUD_INSTANCE + TENANT_ID,
// 		clientSecret: CLIENT_SECRET,
// 	},
// };


// Needs to become dynamic again
export const msalConfig = {
	auth: {
		clientId: "a9c7cdfe-635e-47d1-b6ca-1682a47d473c",
		authority: "https://login.microsoftonline.com/" + "2b197efa-8e1b-4680-b263-8e237889b5b3",
		clientSecret: "e9s8Q~l3oyyxVzxD2mCTZ9B-tsWceirCQRcj.bKY",
	},
};