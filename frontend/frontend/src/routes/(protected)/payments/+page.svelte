<script lang="ts">
    import { onMount } from "svelte";

    let cookieContent = "";

    onMount(() => {

    });

    import Payments from "$lib/components/display/carousel/parent_carousel_payments.svelte";

    function checkAlive() {
        alert("Still living");
    }

    let showToast = false;
    function showNotification() {
    showToast = true;
    setTimeout(() => {
      showToast = false;
    },  4000); 
    }

</script>

<div class="mt-20 lg:mx-10 h-screen ">
    <h1 class="flex text-2xl font-bold  my-5">Payments</h1>
    <p>All Payments</p>
    <div class="flex flex-1 justify-center items-center">
    <Payments/>
    </div>
    <p class="mt-20 ">Create a Payment request</p>
    <button on:click={showNotification} class="btn bg-htlyellow mt-4">Create now</button>
    {#if showToast}
    <div class="toast toast-end">
        <div class="alert alert-error">
          <span>You can't do this.</span>
        </div>
    </div>
    {/if}
</div>
