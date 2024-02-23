<script lang="ts">
    export let data;
    import QrCode from '../../QRCode.svelte';
    import { upload_paymentconfirm } from '$lib/api/services';
    import { user } from "$lib/stores/UserStore.js"
    import { list } from 'postcss';
    import { onMount } from 'svelte';


    let payment;

    $user.owned_payments.forEach(entry => {
        if(entry.id == data.title) {
            payment = entry;
        }
    })

    let paymentData = {
        BIC: payment.bic,
        merchantName: "HTL-Villach",
        iban: payment.iban,
        transactionAmount: payment.cost,
        purpose: `${payment.name}-${$user.lastname}-${$user.firstname}`  
    };


    // File upload
    onMount( () => {
        const fileInput = document.getElementById('fileUpload');

        document.getElementById("uploadForm")?.addEventListener("submit", async function(event) {
            event.preventDefault();

            const fileInput = document.getElementById("fileInput");
            const formData = new FormData();
            formData.append("file", fileInput.files[0]);
            formData.append("payment", payment.id)
            formData.append("id", $user.identifier)
            formData.append("sclass", $user.sclass)

            upload_paymentconfirm(formData)

        })

    })




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
    <!-- <input id="fileUpload" type="file" class="file-input file-input-bordered w-full max-w-xs" /> -->
    <form id="uploadForm" enctype="multipart/form-data">
        <input type="file" id="fileInput", name="pdfFile">
        <button type="submit">Upload</button>
    </form>

</div>

