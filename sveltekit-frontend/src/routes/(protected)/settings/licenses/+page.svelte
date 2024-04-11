<script context="module">
    export async function load({ locals }) {
       // Access the accessTokenJWT from locals
       const accessToken = locals.accessToken;
   
       // Return the value to the component
       return {
         props: {
           accessToken
         }
       };
    }
   </script>

<script>
    import { onMount } from 'svelte';

    export let accessToken;


    let data;
    let newLicenseGroup = {};
    let students;






    function test() {
        console.log("")
    }


    onMount(async() => {



    })

</script>


<!-- Page Content -->
 

{#await data}

<div class="min-h-screen lg:mx-10 mt-20 relative">
    <h1 class="text-2xl font-bold mb-4">Page Loading</h1> 
</div>

{:then value}

<div class="min-h-screen lg:mx-10 mt-20 relative">

    <h1 class="text-2xl font-bold mb-4">License Management</h1>

    <!-- Show default licenses -->
    <div>
        <h2 class="text-xl font-bold mb-4">Default Licenses</h2>
    </div>


    <div class="divider"></div> 


    <!-- Show active licenses -->
    <div>
        <h2 class="text-xl font-bold mb-4">Active Licenses</h2>
    </div>

    <div class="divider"></div> 


    <!-- Create a new license group -->
    <div>
        <h2 class="text-xl font-bold mb-4">Create a new License Group</h2>

        <!-- Name -->
        <label class="form-control w-full max-w-xs">
            <div class="label">
                <span class="label-text">Name</span>
            </div>
            <input type="text" placeholder="Adobe Default License" class="input input-bordered w-full max-w-xs" />
            <div class="label">
                <span class="label-text-alt"></span>
                <span class="label-text-alt">Will be used when displaying licenses of this group</span>
            </div>
        </label>

        <!-- Description -->
        <label class="form-control w-full max-w-xs">
            <div class="label">
                <span class="label-text">Description</span>
            </div>
            <textarea class="textarea textarea-bordered" placeholder="Description"></textarea>
            <div class="label">
                <span class="label-text-alt"></span>
            </div>
        </label>

        <!-- Source -->
        <label class="form-control w-full max-w-xs">
            <div class="label">
                <span class="label-text">Source</span>
            </div>
            <input type="text" placeholder="Adobe Default License" class="input input-bordered w-full max-w-xs" />
            <div class="label">
                <span class="label-text-alt"></span>
                <span class="label-text-alt">Define a target group for this license group. Either use a Microsoft ID or a list of classes, seperated with ","</span>
            </div>
        </label>



    </div>


    <button on:click={test}>Test</button>

    <p>{accessToken}</p>

</div>


{/await}
