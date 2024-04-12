<script lang="ts">
	import htllogo from '$lib/assets/logo.png'
	export let paymentspage:string
	export let licensespage:string
	export let overviewpage:string
	export let teacherviewpage:string
	export let settingspage: string
	export let accountingviewpage: string
</script>





<div class="relative lg:drawer-open z-10">
	<input id="my-drawer-2" type="checkbox" class="drawer-toggle" />
	
	<div class="drawer-content flex justify-start">
	<label for="my-drawer-2" class="btn btn-square btn-ghost drawer-button lg:hidden">
		<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block stroke-white w-6 h-6 mt-4 "><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
	</label>
	
	</div> 

	
<div class="drawer-side ">
	<label for="my-drawer-2" aria-label="close sidebar" class="drawer-overlay"></label> 

	  
	<ul class="menu p-4 w-80 min-h-full bg-htlyellow text-base-content ">
		<img src="{htllogo}" alt="HTL-Logo">
		<li><a href="{overviewpage}" class="text-lg rounded-md hover:bg-secondary hover:text-lighttext">Übersicht</a></li>
		<li><a href="{licensespage}" class="text-lg rounded-md hover:bg-secondary hover:text-lighttext">Lizenzen</a></li>
		<li><a href="{paymentspage}" class="text-lg rounded-md hover:bg-secondary hover:text-lighttext">Zahlungen</a></li>
		<li><a href="{teacherviewpage}" class="text-lg rounded-md hover:bg-secondary hover:text-lighttext">Lehreransicht</a></li>
		<li><a href="{accountingviewpage}" class="text-lg rounded-md hover:bg-secondary hover:text-lighttext">Buchhaltung</a></li>
		<li><a href="{settingspage}" class="text-lg rounded-md hover:bg-secondary hover:text-lighttext">Einstellungen</a></li>
	</ul>
	
	</div>
</div>

