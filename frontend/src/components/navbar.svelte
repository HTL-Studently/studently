<script>

</script>

<style>
	ul li{
		text-decoration: none;
		color: #000; 
		padding: 10px;
		transition: background-color 0.3s ease;
		font-size: 1.5em;
		width: 100%;
		
	}
	ul li:hover{
		background-color: #fbbf06;
		text-decoration: none;
		color: #000; 
		padding: 10px;
		border-radius: 10px;
		
	}
	nav {
		height: 100vh;
		width: 15%;
		background-color: #ffe65d;
		position: fixed;
		top: 0;
		left: 0;
		display: flex;
		flex-direction: column; 
		padding: 20px;
	}
	ul{
		margin-top: 10vh;
		width: 100%;
		
	}
	img{
		align-items: center;
		margin-left: -1em;
	}
	
</style>
<nav>
	<img src="../public/logo.png" alt="Logo"/>
	<ul>
		<li><a href="/pages/index" >Overview</a></li>
		<li><a href="licenses.astro" >Licenses</a></li> 
		<li><a href="../pages/payments.astro" >Payments</a></li>
	</ul>
</nav>



