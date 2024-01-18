<script>
// if (typeof window !== 'undefined') {
//    document.querySelector('#menuToggle').addEventListener('click', function() {
//        var menu = document.querySelector('.sidebar');
//        menu.classList.toggle('hidden');
//    });
// }

import { onMount } from 'svelte';

onMount(() => {
  // Add your initialization logic here
});
</script>



	
<!-- <div class="flex h-screen">
	
	<div class="w-64   bg-yellow-300 border-r overflow-hidden ">
		<button>
			<img src="../../public/logo.png" alt="HTL-Logo">
		</button>
		<nav class=" h-full px-2 space-y-1 bg-yellow-300 " id="sidebar">
			<a href="../pages/index.astro" class="block px-6 py-2 hover:bg-yellow-400 rounded-md">Overview</a>
			<a href="../pages/licenses.astro" class="block px-6 py-2 hover:bg-yellow-400 rounded-md">Licenses</a>
			<a href="../pages/payments.astro" class="block px-6 py-2 hover:bg-yellow-400 rounded-md">Payments</a>
		</nav>
	</div>
</div> -->

<!-- Sidebar.svelte -->
<div class=" bg-yellow-300">
	
	<div class=" md:w-64 bg-yellow-300 border-r overflow-hidden ">
		<button class="md:w-64 w-44">
			<img src="../../public/logo.png" alt="HTL-Logo">
		</button>
		<nav class=" md:h-full px-2 md:space-y-1 bg-yellow-300 " >
			<a href="../pages/index.astro" class="block px-6 py-2 hover:bg-yellow-400 rounded-md">Overview</a>
			<a href="../pages/licenses.astro" class="block px-6 py-2 hover:bg-yellow-400 rounded-md">Licenses</a>
			<a href="../pages/payments.astro" class="block px-6 py-2 hover:bg-yellow-400 rounded-md">Payments</a>
		</nav>
	</div>
</div>
   





   
<!-- <style>
	@media (max-width:768px){
		#sidebar{
			display: none;
		}
		#menuToggle{
			max-width: 10rem;
		}
	}
</style> -->