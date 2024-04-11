<script lang="ts">
    import "tailwindcss/tailwind.css";


    import Header from '$lib/components/basic/header.svelte';
    import Navbar from '$lib/components/basic/navbar.svelte';
    import Footer from '$lib/components/basic/footer.svelte';

    const logoutUrl: string = '/logout';
    const firstname: string = "FIRSTNAME";
    const lastname: string = "LASTNAME";

    const licensespage:string = '/licenses';
    const paymentspage:string = '/payments';
    const overviewpage:string = '/';
    const teacherviewpage:string = '/teacherview'
    const settingspage:string = "/"

</script>

<div class="flex h-full lg:h-min bg-background">
    <Header logoutUrl={logoutUrl} firstname={firstname} lastname={lastname}/>
    <Navbar {overviewpage} {licensespage} {paymentspage} {teacherviewpage} {settingspage}/>

    <div class=" lg:w-2/3 lg:justify-around  w-4/5" >
        <slot/>
    </div>

</div>

<Footer/>


