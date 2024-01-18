<script lang="ts">
  import Child from './child_payments.svelte';

  let numberOfBoxes: number = 2;
</script>

<div class="flex flex-row mt-20" >
 {#each Array(numberOfBoxes) as _, index (index)}
   <!-- Use the index or any other data to customize each instance -->
   <Child />
 {/each}
</div>
