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


<div class="max-h-10 absolute top-0 justify-end navbar  bg-base-100">
    


    <!-- name -->
    <p class="m-3">{userValue.firstname} {userValue.lastname}</p>


    <!-- logout  -->
    <img class="btn btn-square btn-ghost max-w-24" src="{logout}" alt="logout" on:click={()=>window.location.href = logoutUrl}>


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