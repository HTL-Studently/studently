
<script lang="ts">
  import type { list } from 'postcss';
  import Child from './child_licenses.svelte';  
  import type { List } from 'postcss/lib/list';

let something='../routes/(protected)/licenses/+page.svelte'

let p1 = {
  "name": "N1",
  "id": "ID1",
  "value": "value1"
}

let p2 = {
  "name": "N2",
  "id": "ID2",
  "value": "value2"
}


let numberOfBoxes = [p1, p2];
</script>

<div class="mt-10 ml-5 mb-5 carousel max-w-full shadow-2 rounded-[1rem]" >
{#each numberOfBoxes as box}

  <div>
  <Child class="carousel-item" />
  </div>
{/each}
</div>

<!-- flex flex-start  -->
<!-- name={box.name} id={box.id} -->

<style>
  .carousel > div{
    margin-right: 2em;
  }
  .carousel > div:last-child{
    margin-right: 0;
  }
</style>