<script lang="ts">
  import Child from './child_payments.svelte';

  let numberOfBoxes: number = 5;
</script>

<div class="flex flex-wrap mt-24">
 {#each Array(numberOfBoxes) as _, index (index)}
   <!-- Use the index or any other data to customize each instance -->
   <Child />
 {/each}
</div>
