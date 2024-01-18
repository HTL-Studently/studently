// Helper functions to access the Backend-API

// Please make me dynamic
const fastapiIP = "10.1.1.131:8080";


export async function postAPI(data: any, endpoint: String, method: String,): Promise<any> {

	try {
		const response = await fetch(`https://fastapi/${endpoint}`, {
			method: `${method}`,
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify(data),
		});

		if (!response.ok) {
			throw new Error(`Failed to send data. Status: ${response.status}`);
		}

	} catch (error) {
		// Handle the error
		console.error('Error sending data:', error);
		throw error;
	}
}


export async function sendUserLogin(accessToken: any, idToken: any, account: any) {
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


export function test() {
	console.log("TEST")
}