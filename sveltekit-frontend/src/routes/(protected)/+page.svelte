<script lang="ts">
    import { onMount } from "svelte";

    let cookieContent = "";

    onMount(() => {

    });

    import Licenses from '$lib/parent_licenses.svelte';
    import Payments from "$lib/parent_payments.svelte";

    const something:string = '/licenses';

    function checkAlive() {
        alert("Still living");
    }

</script>

<div class="mt-20">
    <h1 class="flex text-xl  mx-5 ">Payments</h1>

    <div class="">
        <Payments />
    </div>
    <br>
    <h1 class="flex text-xl  m-5">Licenses</h1>
    <div class="">
        <Licenses/>
    </div>
</div>
