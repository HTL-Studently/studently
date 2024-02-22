<script lang="ts">
    import type { list } from 'postcss';
  import Child from './child_payments.svelte';
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
  let p3 = {
    "name": "N3",
    "id": "ID1",
    "value": "value1"
  }

  let p4 = {
    "name": "N4",
    "id": "ID2",
    "value": "value2"
  }

  let numberOfBoxes = [p1, p2, p3, p4];
</script>

<div class="mt-10 ml-5 mb-5 carousel max-w-full shadow-2 rounded-[1rem]" >
  {#each numberOfBoxes as box}

  <div class="">
   <Child class="carousel-item" name={box.name} id={box.id}/>
  </div>
 {/each}
 <div class=" inset-0 shadow-white"></div>
</div>

<!-- flex flex-start  -->

<style>
  .carousel > div{
    margin-right: 2em;
  }
  .carousel > div:last-child{
    margin-right: 0;
  }

</style>