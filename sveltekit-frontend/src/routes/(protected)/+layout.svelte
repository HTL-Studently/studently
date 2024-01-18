<script lang="ts">
    import '../../tailwind.css'

    import Header from '$lib/header.svelte';
    import Navbar from '$lib/navbar.svelte';
    import Footer from '$lib/footer.svelte';

    const logoutUrl: string = '/logout';
    const licensespage:string = '/licenses';
    const paymentspage:string = '/payments';
    const overviewpage:string = '/';

</script>

<div class="flex  h-auto lg:h-min">
    <Navbar {overviewpage} {licensespage} {paymentspage} />


    <div  >
        <slot/>
    </div>

    <Header {logoutUrl}/>


</div>

<Footer/>

