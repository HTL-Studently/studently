<script lang="ts">
    import QR from '@svelte-put/qr/img/QR.svelte';
    import { user } from "$lib/stores/UserStore.js"
    import { onMount } from 'svelte';


    export let data; 

    let userValue;
    user.subscribe((value) => {
        userValue = value;
    })

    let productList = []
    let product
    let formatedDueDate;
    let formatedDueTime;
    let formatedStartDate;
    let formateStartTime;

    let paymentData = {
        BIC: "BIC",
        merchantName: "HTL-Villach",
        iban: "IBAN",
        transactionAmount: 100,
        // purpose: `${payment.name}-${$user.lastname}-${$user.firstname}`
        purpose: "PURPOSE"  
    };

    let qrData = `BCD
001
1
SCT
KSPKAT2KXXX
Panna Kunos
AT452070604600063657
EUR0.00
`

onMount(async() => {
    productList = userValue.owned_objects
    product = productList.find(obj => obj.identifier == data.slug)

    // Format time
    const dueDate = new Date(product.due_date)
    formatedDueDate = dueDate.toLocaleDateString("de-DE", {
        weekday: "long",
        year: "numeric", 
        month: "2-digit", 
        day: "2-digit",
    });
    formatedDueTime = dueDate.toLocaleTimeString("de-DE", {
        hour: "numeric",
        minute: "2-digit", 
        second: "2-digit",
        hour12: false,
    })

    const startDate = new Date(product.start_date)
    formatedStartDate = startDate.toLocaleDateString("de-DE", {
        weekday: "long",
        year: "numeric", 
        month: "2-digit", 
        day: "2-digit",
    });
    formateStartTime = startDate.toLocaleTimeString("de-DE", {
        hour: "numeric",
        minute: "2-digit", 
        second: "2-digit",
        hour12: false,
    })


    const url = "http://localhost:8080/profile"

    try {
        const response = await fetch(`${url}/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            credentials: 'include',
        })

        const data = await response.json();

        const userProfile = data.message.profile;
        
        console.log("Setting User")

        user.set({
            disabled: userProfile.disabled,
            identifier: userProfile.identifier,
            username: userProfile.username,
            firstname: userProfile.firstname,
            lastname: userProfile.lastname,
            email: userProfile.email,
            expires: userProfile.expires,
            created: userProfile.created,
            sclass: userProfile.sclass,
            type: userProfile.type,
            owned_objects: userProfile.owned_objects,
            owned_payments: userProfile.owned_payments,
        });

        return {
            slug: slug
        }

    } catch (error) {
    console.error(`Error sending data to ${url}:', ${error}`);
    throw error;
    }
}


})

</script>




{#if product}
<div class=" h-auto mb-10 min-h-screen lg:mx-10 mt-20">
    <h1 class="text-2xl font-bold mt-20">Payment information for {product.name}</h1>
    <h2 class="text-lg my-5">Payment Details</h2>

    <div class=" flex card bg-white-100 shadow-xl">
        <div class="card-body">
            <p>Created by: {product.author}</p>
            <p>Amount: {product.cost}€</p>
            <p>IBAN: {product.iban}</p>
            <p>BIC: {product.bic}</p>
            <p>Frühestens aktiv ab:  {formatedStartDate} - {formateStartTime}</p>
            <p>Läuft ab am:  {formatedDueDate} - {formatedDueTime}</p>
        </div>
    </div>

    <h2 class=" text-lg my-5">Pay via QR-Code</h2>
        <div class="card w-fit bg-base-100 shadow-xl">
        <div class="card-body">
            <QR
            data={qrData}
            moduleFill="white"
            anchorOuterFill="white"
            anchorInnerFill="white"
              width="500"
              height="500"
          />
          
        </div>
    </div>
    
    
    <h2 class="text-lg my-5">Payment confirmation</h2>
    <!-- <input id="fileUpload" type="file" class="file-input file-input-bordered w-full max-w-xs" /> -->
    <form id="uploadForm" enctype="multipart/form-data">
        <input type="file" id="fileInput" name="pdfFile">
        <button type="submit">Upload</button>
    </form>

</div>

{:else}
<div class="h-auto mb-10 min-h-screen lg:mx-10 mt-20 flex justify-center items-center">
    <span class="loading loading-dots loading-lg"></span>
</div>
{/if}