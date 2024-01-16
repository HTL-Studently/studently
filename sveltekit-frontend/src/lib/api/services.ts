// Helper functions to access the Backend-API

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


export function test() {
	console.log("TEST")
}