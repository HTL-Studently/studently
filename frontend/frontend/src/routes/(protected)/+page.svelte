<script lang="ts">
    import Licenses from '$lib/components/display/carousel/parent_carousel_licenses.svelte';
    import Payments from "$lib/components/display/carousel/parent_carousel_payments.svelte";

</script>


<div class="min-h-screen lg:mx-10 mt-20 relative">

    <!-- Payments carousel view -->
    <h1 class="text-2xl font-bold mb-4">Payments</h1>
    <div>
        <Payments />
    </div>

    <!-- Licenses carousel view -->
    <h1 class="text-2xl font-bold mb-4">Licenses</h1>
    <div>
        <Licenses />
    </div>

</div>
