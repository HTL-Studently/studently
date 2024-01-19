<script lang="ts">
    import { onMount, onDestroy } from "svelte";
    import Licenses from '$lib/parent_licenses.svelte';
    import Payments from "$lib/parent_payments.svelte";
    


</script>

<div class=" h-screen ">
    <!-- <h1>Payments</h1> -->
    <div class="flex flex-1 justify-center items-center mt-10">
        <Payments/>
    </div>
    <br>
    <!-- <h1>Licenses</h1> -->
    <div class="flex flex-1 justify-center items-center">
        <Licenses/>
    </div>
</div>




