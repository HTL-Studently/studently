<script lang="ts">
    import Licenses from '$lib/components/display/carousel/parent_carousel_licenses.svelte';
    import Payments from "$lib/components/display/carousel/parent_carousel_payments.svelte";
	import { onMount } from 'svelte';

    
    let productList = []

    onMount(async() => {


        async function getProducts() {
            let data;
            try {
                const response = await fetch('http://localhost:8080/product', {
                    credentials: 'include'
                });

                data = await response.json();
                return data
            
            } catch (error) {
                console.error('Error fetching product data:', error);
            }
        }
        productList = await getProducts()
        console.log(productList)







    })



</script>


<div class="min-h-screen lg:mx-10 mt-20 relative">

    <!-- Payments carousel view -->
    <h1 class="flex text-xl  mx-5">Products</h1>
    <div>
        {#each productList as product}

        <div class="flex-shrink-0 card w-72 lg:w-96 bg-violet-300">
            <div class="card-body">
              <h2 class="card-title">{product.name}</h2>
              <p>View or submit your payment</p>
              <div class="card-actions justify-end">
                  <p>{product.id}</p>
                  <button class="btn  btn-primary"><a  href="{`/payments/${product.id}`}" >Open</a></button>
                
              </div>
            </div>
        </div>

        {/each}
    </div>

    <!-- Licenses carousel view -->
    <h1 class="text-2xl font-bold mb-4">Licenses</h1>
    <div>
        <Licenses />
    </div>

</div>
