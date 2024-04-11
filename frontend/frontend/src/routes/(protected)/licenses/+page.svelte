<script lang="ts">
    import { onMount } from "svelte";

    let cookieContent = "";

    onMount(() => {

    });

    import Licenses from '$lib/components/display/carousel/parent_carousel_licenses.svelte';

    function checkAlive() {
        alert("Still living");
    }

</script>

<div class="mt-20 lg:mx-10 h-screen ">
    <h1 class="flex text-2xl font-bold  my-5">Licenses</h1>
    <p>Available Licenses</p>
    <div class="flex flex-1 justify-center items-center">
    <Licenses/>
    </div>
    <p>Your Licenses</p>
    <div class="flex flex-1 justify-center items-center">
        <Licenses/>
        </div>
</div>