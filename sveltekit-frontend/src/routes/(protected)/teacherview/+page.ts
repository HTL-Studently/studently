/** @type {import('./$types').PageLoad} */
export async function load({ fetch }) {

    let url = "http://localhost:8080/class"
    let data;

    // Get class list
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            credentials: 'include',
        });

        data = await response.json();

    } catch (error) {
    console.error(`Error sending data to ${url}:, ${error}`);
    throw error;
    }

    return data
}