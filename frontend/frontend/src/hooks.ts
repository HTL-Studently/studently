/** @type {import('@sveltejs/kit').HandleFetch} */
export async function handleFetch({ event, request, fetch }) {
	// Handle GET requests

	console.log("FETCHING - ", request.url)

	if (request.method === "POST") {
		const accessToken = event.cookies.get("accessToken"); 
		let newRequest = new Request(request, {
			headers: new Headers(request.headers),
		}) 

		// Set Headers		
		newRequest.headers.set('Authorization', `Bearer ${accessToken}`);

		return fetch(newRequest)
	}
}


export async function getSession() {
    const url = "http://localhost:8080/profile"

	const response = await fetch(url, {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		credentials: 'include',
	})

	const data = await response.json();

	const userProfile = data.message.profile;

    return {
        user: {
            firstname: userProfile.firstname,
			lastname: userProfile.lastname,
            userId: userProfile.identifier,
            // Add other user data as needed
        }
    };
}