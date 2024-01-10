<script>
	let user;
  
	const fetchData = async () => {
	  try {
		const response = await fetch('http://10.1.1.134:8080/me');
		user = await response.json();
	  } catch (error) {
		console.error('Error fetching data:', error);
	  }
	};
  
	// Fetch data when the component is mounted
	fetchData();
</script>

<header>
	<button>
		<img src="../public/logout.png" alt="Logout">
	</button>
	
	{#if user}
    <p>Username from FastAPI endpoint: {user.username}</p>
  {/if}
</header>

<style>
	header{
		margin-left: 15%;
		width: 85%;
		min-height: 5vh;
		background-color: #fff;
		text-align: right;
        position: fixed;
		display: flex;
		align-items: center;
		justify-content: flex-end;
		
	}
	header img{
		max-width: 2em;
	}
	header p{

		margin: 1.5em;
		font-size: large;
		display: flex;
		align-items: center;

	}
</style>

