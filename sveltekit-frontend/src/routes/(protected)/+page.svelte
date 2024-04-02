<script context="module">
    export async function load({ cookies }) {
        const accessToken = cookies.get('accessTokenJWT');
        return {
        props: {
            accessToken
        }
        };
    }
</script>


<script lang="ts">
    import { onMount } from "svelte";

	export let data;



    export let accessToken;

    onMount(() => {

    });

    import Licenses from '$lib/parent_licenses.svelte';
    import Payments from "$lib/parent_payments.svelte";

    const something:string = '/licenses';

    function checkAlive() {
        alert("Still living");
    }

</script>




<div class="mt-20">

    <h1 class="flex text-xl  mx-5 ">Payments</h1>

    <div class="">
        <Payments />
    </div>
    <br>
    <h1 class="flex text-xl  m-5">Licenses</h1>
    <div class="">
        <Licenses/>
    </div>

    <p>{$accessToken}</p>
</div>
