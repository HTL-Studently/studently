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
    <h1 class="text-2xl font-bold mb-4">Zahlungen</h1>
    <div>
        <!-- <Payments></Payments> -->
        <div class="mb-10">
            {#each productList as product}
    
            <div class="flex-shrink-0 inline-block  m-3 card w-64 lg:w-96 bg-violet-300">
                <div class="card-body">
                  <h2 class="card-title">{product.name}</h2>
                  <p>Zahlungsdetails</p>
                  <div class="card-actions justify-end">
                        <p>ID: {product.identifier}</p>
                        <button class="btn  btn-primary"><a  href="{`/payments/${product.identifier}`}" >Open</a></button>
                  </div>
                </div>
            </div>
    
            {/each}
        </div>
    </div>

</div>
