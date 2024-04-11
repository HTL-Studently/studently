import { user } from "$lib/stores/UserStore"


/** @type {import('./$types').PageLoad} */
export async function load({ fetch }) {

    let data;

    // Get User Data
    let url = "http://localhost:8080/profile"
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

    } catch (error) {
    console.error(`Error sending data to ${url}:', ${error}`);
    throw error;
    }


    // Get class list
    url = "http://localhost:8080/class"
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
    console.error(`Error sending data to ${url}:', ${error}`);
    throw error;
    }

    return data
}