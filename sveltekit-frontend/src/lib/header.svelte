<script lang="ts">
import logout from '$lib/assets/logout.png'
import { writable } from 'svelte/store';
export let logoutUrl:string;
</script>


<div class="max-h-10 absolute top-0 justify-end navbar  bg-base-100">
    


    <!-- name -->
    <p class="m-3">User Name</p>

    <!-- logout  -->
    <img class="btn btn-square btn-ghost max-w-10" src="{logout}" alt="logout" on:click={()=>window.location.href = logoutUrl}>


    

    <!-- avatar -->
    <div class="avatar p-2">
        <div class="max-w-12 rounded-full">
        <img src="https://daisyui.com/images/stock/photo-1534528741775-53994a69daeb.jpg" />
        </div>
    </div>

</div>