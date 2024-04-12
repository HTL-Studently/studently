<script>
    import { user } from "$lib/stores/UserStore.js"
    import { onMount } from 'svelte';

    export let data; 

    let userValue;
    user.subscribe((value) => {
        userValue = value;
    })

    let studentProfile;



onMount(async() => {
    try {
        const url = "http://localhost:8080/profile"
        const response = await fetch(`${url}?id=${data.slug}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            credentials: 'include',
        })

        const apiresponse = await response.json();
        studentProfile = apiresponse.message.profile;


    } catch (error) {
        console.error(`Error sending data to ${url}:', ${error}`);
        throw error;
    }

    console.log(studentProfile)

})
</script>

