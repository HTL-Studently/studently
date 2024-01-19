<script lang="ts">
    import '../../tailwind.css'
    import { onMount } from 'svelte';
    import { get_profile } from "$lib/api/services";
    import Header from '$lib/header.svelte';
    import Navbar from '$lib/navbar.svelte';
    import Footer from '$lib/footer.svelte';
    import Payments from "$lib/parent_payments.svelte";

    const logoutUrl: string = '/logout';
    const licensespage:string = '/licenses';
    const paymentspage:string = '/payments';
    const overviewpage:string = '/';

    export let firstname: string = "";
    export let lastname: string = ""
    export let licenses: [] = []

    let AccessToken: any; 
    let AccountData: any; 

    async function fetchToken() {
        const response = await fetch('/api', {
            method: 'GET',
        })
        AccessToken = await response.text();
        if(AccessToken) {
            console.log("AccessToken 1");
        }else {
            console.log("AccessToken 0")
        }
    }

    onMount( async () => {
        await fetchToken()
        const response = await get_profile({"accessToken": AccessToken})

        AccountData = response
        console.log("MY SUPA: " + AccountData)

        if(AccountData) {
            firstname = AccountData["firstname"]
            lastname = AccountData["lastname"]
            licenses = AccountData["owned_objects"]
        }

        console.log(licenses)

    })


</script>

<div class="flex  h-auto lg:h-min">
    <Navbar {overviewpage} {licensespage} {paymentspage} />


    <div class=" h-screen ">
        <!-- <h1>Payments</h1> -->
    
        <div class="flex flex-1 justify-center items-center mt-10">
            <Payments {licenses}/>
        </div>
        <br>
        <!-- <h1>Licenses</h1> -->
        <div class="flex flex-1 justify-center items-center">
            <Licenses/>
        </div>
    </div>



    <Header {logoutUrl} {firstname} {lastname}/>


</div>

<Footer/>

