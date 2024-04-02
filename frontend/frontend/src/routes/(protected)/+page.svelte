<script lang="ts">
    import Licenses from '$lib/components/display/carousel/parent_carousel_licenses.svelte';
    import Payments from "$lib/components/display/carousel/parent_carousel_payments.svelte";
    import { API_BASEURL } from '$env/static/private'; 
    import { user } from "$lib/stores/UserStore"
	import { onMount } from 'svelte';

    // export async function load() {




    //     const url = `${API_BASEURL}/profile`

    //     try {
    //         const response = await fetch(url, {
    //             method: "POST",
    //             headers: {
    //                 "Content-Type": "application/json",
    //             },
    //             credentials: 'include',
    //         })

    //         const data = await response.json();
    //         const userProfile = data.message.profile;
            
    //         user.set({
    //             disabled: userProfile.disabled,
    //             identifier: userProfile.identifier,
    //             username: userProfile.username,
    //             firstname: userProfile.firstname,
    //             lastname: userProfile.lastname,
    //             email: userProfile.email,
    //             expires: userProfile.expires,
    //             created: userProfile.created,
    //             sclass: userProfile.sclass,
    //             type: userProfile.type,
    //             owned_objects: userProfile.owned_objects,
    //             owned_payments: userProfile.owned_payments,
    //         });

    //         console.log("TEST")
    //         console.log(userProfile.identifier)

    //         return 

    //     } catch (error) {
    //     console.error(`Error sending data to ${url}:', ${error}`);
    //     throw error;
    //     }
    // }


    // onMount(async () => {

    //     const url = `${API_BASEURL}/profile`

    //     try {
    //         const response = await fetch(url, {
    //             method: "POST",
    //             headers: {
    //                 "Content-Type": "application/json",
    //             },
    //             credentials: 'include',
    //         })

    //         const data = await response.json();
    //         const userProfile = data.message.profile;
            
    //         user.set({
    //             disabled: userProfile.disabled,
    //             identifier: userProfile.identifier,
    //             username: userProfile.username,
    //             firstname: userProfile.firstname,
    //             lastname: userProfile.lastname,
    //             email: userProfile.email,
    //             expires: userProfile.expires,
    //             created: userProfile.created,
    //             sclass: userProfile.sclass,
    //             type: userProfile.type,
    //             owned_objects: userProfile.owned_objects,
    //             owned_payments: userProfile.owned_payments,
    //         });

    //         console.log("TEST")
    //         console.log(userProfile.identifier)

    //         return 

    //     } catch (error) {
    //     console.error(`Error sending data to ${url}:', ${error}`);
    //     throw error;
    //     }
    // });

</script>


<div class="mt-20">

    <!-- Payments carousel view -->
    <h1 class="flex text-xl  mx-5">Payments</h1>
    <div>
        <Payments />
    </div>

    <!-- Licenses carousel view -->
    <h1 class="flex text-xl  m-5">Licenses</h1>
    <div>
        <Licenses />
    </div>

</div>
