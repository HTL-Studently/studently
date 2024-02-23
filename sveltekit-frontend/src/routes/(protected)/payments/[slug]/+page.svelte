<script>
    export let data;
    import QrCode from '../../QRCode.svelte';
    import { upload_paymentconfirm } from '$lib/api/services';
    import { user } from "$lib/stores/UserStore.js"
    import { list } from 'postcss';
    import { onMount } from 'svelte';

    // File upload
    onMount( () => {
        const fileInput = document.getElementById("fileUpload");

        fileInput?.addEventListener("change", async (event) => {
            const file = event.target.files[0];
            if(!file) return;

            const formData = new FormData();
            formData.append("file", file)

            const response = await upload_paymentconfirm()
        })
    })


    let payment;

    $user.owned_payments.forEach(entry => {
        if(entry.id == data.title) {
            payment = entry;
        }
    })

    let paymentData = {
    BIC: payment.bic,
    merchantName: 'HTL-Villach',
    iban: payment.iban,
    transactionAmount: payment.cost,
    purpose: `${payment.name}-${$user.lastname}-${$user.firstname}`  
  };


</script>


<div class=" h-auto mb-10 min-h-screen lg:mx-10 mt-20">
    <h1 class="text-2xl font-bold mt-20">Payment information for {payment.name}</h1>
    <h2 class="text-lg my-5">Payment Details</h2>

    <div class=" flex card max-w-96 bg-base-100 shadow-xl">
        <div class="card-body">
            <p>Created by: {payment.author}</p>
            <p>Amount: {payment.cost}€</p>
            <p>IBAN: {payment.iban}</p>
            <p>BIC: {payment.bic}</p>
            <p>Created Date:  {payment.start_date}</p>
            <p>Due Date:  {payment.expires}</p>
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
        <input id="fileUpload" type="file" class="file-input file-input-bordered w-full max-w-xs" />
    </label>
    
</div>

