<script>
  export let data;
  import QrCode from '../../QRCode.svelte';

  let paymentData = {
    BIC: 'BPOTBEB1',
    merchantName: 'HTL-Villach',
    iban: 'BE72000000001616',
    transactionAmount: '1',
    purpose: 'Donation' // Example reference number
  };

</script>


<div class=" h-auto mb-10 min-h-screen lg:mx-10 mt-20">
    <h1 class="text-2xl font-bold mt-20">Payment information for {data.title}</h1>

    <div>
    <h2 class="text-lg my-5">Payment Details</h2>
    <div class=" flex card max-w-96 bg-base-100 shadow-xl">
      <div class="card-body">
        <p>Created by: {paymentData.merchantName}</p>
        <p>Amount: {paymentData.transactionAmount}€</p>
        <p>Created Date:  2024-02-01</p>
        <p>Due Date:  2023-04-30</p>
      </div>
    </div>
  </div>


    <h2 class=" text-lg my-5">Pay via QR-Code</h2>
    <div class="card w-fit bg-base-100 shadow-xl">
      <div class="card-body">
        <QrCode {paymentData} />
      </div>
    </div>
    
    
    <h2 class="text-lg my-5">Payment confirmation</h2>
    <label class="form-control w-full max-w-xs">
      <div class="label">
        <span class="label-text">Pick a file</span>
      </div>
      <input type="file" class="file-input file-input-bordered w-full max-w-xs" />
    </label>
    
</div>

