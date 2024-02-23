<script lang="ts">
    import type { list } from 'postcss';
    import Child from './child_payments.svelte';
    import type { List } from 'postcss/lib/list';
    import { user } from "$lib/stores/UserStore.js"

    let something='../routes/(protected)/licenses/+page.svelte'
    console.log($user.owned_payments)

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


<!-- flex flex-start  -->

<style>
    .carousel > div{
        margin-right: 2em;
    }
    .carousel > div:last-child{
        margin-right: 0;
    }

</style>