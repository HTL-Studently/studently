<script lang="ts">
    import type { list } from 'postcss';
    import Child from '$lib/components/display/carousel/child_carousel_payments.svelte';
    import type { List } from 'postcss/lib/list';
    import { user } from "$lib/stores/UserStore.js"

    let something='../routes/(protected)/licenses/+page.svelte'

</script>

<div class="mt-10 ml-5 mb-5 carousel max-w-full shadow-2 rounded-[1rem]" >
    {#if $user.owned_payments != []}
        {#each $user.owned_payments as payment}

            <div class="">
            <Child class="carousel-item" payment={payment}/>
            </div>
        {/each}
    {:else}
        <p>NO PAYMENTS</p>
    {/if}
    <div class=" inset-0 shadow-white"></div>
</div>

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



<!-- flex flex-start  -->

<style>
    .carousel > div{
        margin-right: 2em;
    }
    .carousel > div:last-child{
        margin-right: 0;
    }

</style>