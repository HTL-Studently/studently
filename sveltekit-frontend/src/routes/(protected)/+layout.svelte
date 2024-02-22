<script lang="ts">
    import '../../tailwind.css'


    import Header from '$lib/header.svelte';
    import Navbar from '$lib/navbar.svelte';
    import Footer from '$lib/footer.svelte';

    const logoutUrl: string = '/logout';
    const licensespage:string = '/licenses';
    const paymentspage:string = '/payments';
    const overviewpage:string = '/';
    const teacherviewpage:string = '/teacherview'

</script>

<div class="flex h-full lg:h-min">
    <Header {logoutUrl}/>
    <Navbar {overviewpage} {licensespage} {paymentspage} {teacherviewpage}/>

    <div class=" lg:w-2/3 lg:justify-around  w-4/5" >
        <slot/>
    </div>

</div>

<Footer/>


