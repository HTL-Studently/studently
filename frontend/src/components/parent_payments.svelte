<script>
    import Child from '../components/child_payments.svelte';
  
    let numberOfBoxes = 5;
</script>


<div class="flex flex-wrap my-24 ">
    {#each Array(numberOfBoxes) as _, index}
      <!-- Use the index or any other data to customize each instance -->
      <Child key={index} />
    {/each}
</div>