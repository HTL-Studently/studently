import { user } from "$lib/stores/UserStore"
import { API_BASEURL } from '$env/static/private';

/** @type {import('./$types').PageLoad} */
export async function load({ fetch }) {
	
    
    const url = `${API_BASEURL}/profile`

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            credentials: 'include',
        })

        const data = await response.json();

        console.log(data)


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

        console.log("TEST")
        console.log(userProfile.identifier)

        return 

    } catch (error) {
    console.error(`Error sending data to ${url}:', ${error}`);
    throw error;
    }
    
    
    
    
    return {};
}