<script lang="ts">
  // export let something;
  export let name;
  export let id;

</script>

<div class="flex-shrink-0 card w-72 lg:w-96 bg-violet-300">
    <div class="card-body">
      <h2 class="card-title">Payment {name}!</h2>
      <p>Submit your or view your payment</p>
      <div class="card-actions justify-end">
          <p>{id}</p>
          <button class="btn  btn-primary"><a  href="{`/payments/${name}`}" >Open</a></button>
        
      </div>
    </div>
</div>

