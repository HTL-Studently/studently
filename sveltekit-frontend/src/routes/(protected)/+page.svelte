<script lang="ts">
    import { onMount } from "svelte";

    let cookieContent = "";

    onMount(() => {

    });



    function checkAlive() {
        alert("Still living");
    }

</script>




<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>

<button on:click={checkAlive}>Check Alive</button>