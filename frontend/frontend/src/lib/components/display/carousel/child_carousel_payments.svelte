<script lang="ts">
  // export let something;
  export let name: any = "123";
  export let id: any;
  export let payment: any;

</script>

<div class="flex-shrink-0 card w-72 lg:w-96 bg-violet-300">
    <div class="card-body">
      <h2 class="card-title">{payment.name}</h2>
      <p>View or submit your payment</p>
      <div class="card-actions justify-end">
          <p>{payment.id}</p>
          <button class="btn  btn-primary"><a  href="{`/payments/${payment.id}`}" >Open</a></button>
        
      </div>
    </div>
</div>

