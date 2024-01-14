<script>



	let NAME = "TEST123";


	function handleClick() {
		console.log('Button Clicked');
		NAME = "TESTONHE123";
	}



import * as msal from "@azure/msal-node";

const clientConfig = {
    auth: {
        clientId: "3fa5cc69-91e7-4e54-b2ff-dfa9b146e44b",
        authority: "https://login.microsoftonline.com/2b197efa-8e1b-4680-b263-8e237889b5b3",
        clientSecret: "HFe8Q~5g.xazG~l7cbrr5drzkN88oOZnyVtstb2l",
    }
};
const pca = new msal.ConfidentialClientApplication(clientConfig);

const tokenRequest = {
  scopes: ["api://3fa5cc69-91e7-4e54-b2ff-dfa9b146e44b/.default"], // Use .default scope
};

pca.acquireTokenByClientCredential(tokenRequest)
  .then((response) => {
    console.log('Access Token:', response.accessToken);
  })
  .catch((error) => {
    console.error('Error acquiring token:', error.message);
  });



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
		<li><a href="/licenses.astro" >Licenses</a></li> 
		<li><a href="/pages/payments.astro" >Payments</a></li>
	</ul>

	<p>{NAME}</p>

	<button on:click={handleClick}>BUTTON</button>

</nav>



