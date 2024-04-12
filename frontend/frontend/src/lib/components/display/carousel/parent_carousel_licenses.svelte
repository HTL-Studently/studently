
<script lang="ts">
  import Child from '$lib/components/display/carousel/child_carousel_licenses.svelte';  


let p1 = {
  "name": "N1",
  "id": "ID1",
  "value": "value1"
}


let numberOfBoxes = [p1];
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