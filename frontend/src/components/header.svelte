<script>

    function handleClick() {
    window.alert("Button was clicked!");
    }
</script>

<header class="md:fixed md:top-0 md:right-0 z-50 bg-white text-gray-600 p-6 flex items-center">
    <span id="username" class="mr-4" >User Name</span>
    <button id="logoutButton" class="btn btn-circle " on:click={handleClick}>
        <img class="w-[30px]" src="../../public/logout.png" alt="Logout">
    </button>
</header>


<!-- <script>
	fetch('http://localhost:8000/your-endpoint') // replace with your actual endpoint
   .then(response => response.json())
   .then(data => {
       document.getElementById('username').innerText = data.username;
   })
   .catch((error) => {
       console.error('Error:', error);
   });

</script> -->