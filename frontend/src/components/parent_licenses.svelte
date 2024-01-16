<script>
    import Child from '../components/child_licenses.svelte';
  
    let numberOfBoxes = 3;
</script>


<div class="flex flex-wrap mt-24">
    {#each Array(numberOfBoxes) as _, index}
      <!-- Use the index or any other data to customize each instance -->
      <Child key={index} />
    {/each}
</div>