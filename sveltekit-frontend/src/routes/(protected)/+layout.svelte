<script lang="ts">
    import '../../tailwind.css'
    import { onMount } from 'svelte';
    import { get_profile } from "$lib/api/services";
    import Header from '$lib/header.svelte';
    import Navbar from '$lib/navbar.svelte';
    import Footer from '$lib/footer.svelte';

    const logoutUrl: string = '/logout';
    const licensespage:string = '/licenses';
    const paymentspage:string = '/payments';
    const overviewpage:string = '/';

    let firstname: string = "";
    let lastname: string = ""

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
        }
    })


</script>

<div class="flex  h-auto lg:h-min">
    <Navbar {overviewpage} {licensespage} {paymentspage} />
    <div>
        <slot/>
    </div>

    <Header {logoutUrl} {firstname} {lastname}/>


</div>

<Footer/>

