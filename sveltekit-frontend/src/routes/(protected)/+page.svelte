<script lang="ts">
    import { onMount } from "svelte";

    let cookieContent = "";

    onMount(() => {

    });



</script>




<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>


<!-- event.cookies.get("idToken") || !event.cookies.get("accessToken") -->

<p>Account Cookie: {cookieContent}</p>
