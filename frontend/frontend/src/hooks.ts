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