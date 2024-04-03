<script>
	import Button from "./Button.svelte"
</script>

<div class="mt-20">

    <Button class="primary sm">
        My Button
    </Button>

    <Button class="danger lg" on:click={()=>console.log("Clicked")}>
        My Button
    </Button>


</div>
