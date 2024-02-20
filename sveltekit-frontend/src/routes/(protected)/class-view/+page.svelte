<script lang="ts">
    export let data: { items: { text: string, name: string }[] };
    import Licenses from '$lib/parent_licenses.svelte';
    import Payments from "$lib/parent_payments.svelte";
</script>



<!-- 
<div class=" h-screen  mt-20">

    <h1 class="text-3xl" >Slug</h1>
    <div class="w-96">
        <h1>Welcome to base</h1>

    {#each data.items as choice}
    <div>
        <p>{choice.text}</p>
        <a href={`/class-view/${choice.name}`}>{choice.name}</a>
    </div>
    {/each}


    </div>
</div> -->


<div class=" h-screen ">
    <!-- <h1>Payments</h1> -->
    <h1 class="text-3xl font-bold mt-20 mb-0 pl-10">My Class</h1>
    <div class="flex flex-1 justify-center items-center pl-10">
        <Payments/>
    </div>
    <br>
    <!-- <h1>Licenses</h1> -->
    <h1 class="text-3xl font-bold mt-10 mb-0 pl-10" >Licenses</h1>
    <div class="flex flex-1 justify-center items-center pl-10">
    <Licenses/>
    </div>
</div>