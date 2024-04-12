<script lang="ts">
    import Licenses from '$lib/components/display/carousel/parent_carousel_licenses.svelte';
    import Payments from "$lib/components/display/carousel/parent_carousel_payments.svelte";
	import { onMount } from 'svelte';
    import { user } from "$lib/stores/UserStore"

    let userValue;
    user.subscribe((value) => {
        userValue = value;
    })

    export let slug;

    let productList = []

    onMount(async() => {
        productList = userValue.owned_objects
        console.log("SLUG: ", slug)
    })

</script>


<div class="min-h-screen lg:mx-10 mt-20 relative">

    <!-- Payments carousel view -->
    <h1 class="text-2xl font-bold mb-4">Payments</h1>
    <div>
        <!-- <Payments></Payments> -->
        <div>
            {#each productList as product}
    
            <div class="flex-shrink-0 card w-72 lg:w-96 bg-violet-300">
                <div class="card-body">
                  <h2 class="card-title">{product.name}</h2>
                  <p>View or submit your payment</p>
                  <div class="card-actions justify-end">
                        <p>ID: {product.identifier}</p>
                        <button class="btn  btn-primary"><a  href="{`/payments/${product.identifier}`}" >Open</a></button>
                  </div>
                </div>
            </div>
    
            {/each}
        </div>
    </div>

    <!-- Licenses carousel view -->
    <h1 class="text-2xl font-bold mb-4">Licenses</h1>
    <div>
        <Licenses />
    </div>

</div>
