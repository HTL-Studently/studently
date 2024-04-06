<script>
	let name = '';
</script>

<div class="min-h-screen lg:mx-10 mt-20 relative">
    <p>Frontend4</p>
    <input bind:value={name} placeholder="enter your name" />
    <p>Hello {name || 'Stranger'}!</p>
</div>