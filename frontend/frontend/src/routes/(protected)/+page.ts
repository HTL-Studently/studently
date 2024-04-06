import { user } from "$lib/stores/UserStore"

/** @type {import('./$types').PageLoad} */
export async function load({ fetch }) {
	
    const url = "http://localhost:8080/profile"

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            credentials: 'include',
        })

        const data = await response.json();

        const userProfile = data.message.profile;
        
        user.set({
            disabled: userProfile.disabled,
            identifier: userProfile.identifier,
            username: userProfile.username,
            firstname: userProfile.firstname,
            lastname: userProfile.lastname,
            email: userProfile.email,
            expires: userProfile.expires,
            created: userProfile.created,
            sclass: userProfile.sclass,
            type: userProfile.type,
            owned_objects: userProfile.owned_objects,
            owned_payments: userProfile.owned_payments,
        });

        return 

    } catch (error) {
    console.error(`Error sending data to ${url}:', ${error}`);
    throw error;
    }
}