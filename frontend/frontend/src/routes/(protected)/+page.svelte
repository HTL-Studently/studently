<script lang="ts">
    import Licenses from '$lib/components/display/carousel/parent_carousel_licenses.svelte';
    import Payments from "$lib/components/display/carousel/parent_carousel_payments.svelte";

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
