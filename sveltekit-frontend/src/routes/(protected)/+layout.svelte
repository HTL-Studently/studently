<script lang="ts">
    import '../../tailwind.css'


    import Header from '$lib/header.svelte';
    import Navbar from '$lib/navbar.svelte';
    import Footer from '$lib/footer.svelte';

	export let data;

    const logoutUrl: string = '/logout';
    const firstname: string = "FIRSTNAME";
    const lastname: string = "LASTNAME";

    const licensespage:string = '/licenses';
    const paymentspage:string = '/payments';
    const overviewpage:string = '/';
    const teacherviewpage:string = '/teacherview'

</script>

<div class="flex h-full lg:h-min">
    <Header logoutUrl={logoutUrl} firstname={firstname} lastname={lastname}/>
    <Navbar {overviewpage} {licensespage} {paymentspage} {teacherviewpage}/>

    <div class=" lg:w-2/3 lg:justify-around  w-4/5" >
        <slot/>
    </div>

</div>

<Footer/>


