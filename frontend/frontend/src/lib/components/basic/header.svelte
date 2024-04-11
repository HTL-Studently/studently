<script lang="ts">
    import logout from '$lib/assets/logout.png'
    import { user } from "$lib/stores/UserStore.js"


    export let logoutUrl: string;

    let userValue;
    user.subscribe((value) => {
        userValue = value;
    })

    let imageUrl = "";


</script>


<div class="max-h-10 absolute top-0 justify-end navbar  bg-secondary shadow-lg">
    


    <!-- name -->
    <p class="m-3 text-lighttext">{userValue.firstname} {userValue.lastname}</p>


    <!-- logout  -->
    <svg class="btn btn-square btn-ghost h-10 w-10 text-lighttext" on:click={()=>window.location.href = logoutUrl} width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">  <path stroke="none" d="M0 0h24v24H0z"/>  <path d="M14 8v-2a2 2 0 0 0 -2 -2h-7a2 2 0 0 0 -2 2v12a2 2 0 0 0 2 2h7a2 2 0 0 0 2 -2v-2" />  <path d="M7 12h14l-3 -3m0 6l3 -3" /></svg>
    <!-- avatar -->
    <!-- <div class="avatar p-2">
        <div class="max-w-12 rounded-full"> -->
            <!-- Show custom pfp if available -->
            <!-- {#if imageUrl}
                <img src="blob:https://developer.microsoft.com/456cbdd4-c47c-4c35-8413-09f0c313096a", alt="Profile Picture" />
            {:else}
                <img src="https://daisyui.com/images/stock/photo-1534528741775-53994a69daeb.jpg", alt="Profile Picture" />
            {/if}
        </div>
    </div> -->

</div>