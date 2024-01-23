// Helper functions to access the Backend-API

// Please make me dynamic
const fastapiIP = "localhost:8080";

export async function sendUserLogin(accessToken: any, idToken: any) {
	const url = `http://${fastapiIP}/signin`

	const loginData = {
		"accessToken": accessToken,
		"idToken": idToken,
	}

	try {
		const response = await fetch(url, {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify(loginData)
		})

		return response;

	} catch (error) {
	console.error(`Error sending data to ${url}:', ${error}`);
	throw error;
	}
}

export async function get_profile(accessToken: any) {
	console.log("TRYING TO GET PROFILE")
	const url = `http://${fastapiIP}/profile`

	const loginData = {
		"accessToken": accessToken,
	}

	try {
		const response = await fetch(url, {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify(loginData)
		})

        const data = await response.json();

		return data


	} catch (error) {
	console.error(`Error sending data to ${url}:', ${error}`);
	throw error;
	}
}