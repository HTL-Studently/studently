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
    let authors = [];

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

    for(const author of product.author) {
        try {
            const url = "http://localhost:8080/profile"
            const response = await fetch(`${url}?id=${author}`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                credentials: 'include',
            })

            const data = await response.json();
            const authorProfile = data.message.profile;
            // authors.push(authorProfile)
            authors = [...authors, authorProfile];

        } catch (error) {
            console.error(`Error sending data to ${url}:', ${error}`);
            throw error;
        }
    }
})



async function uploadPayment() {
    const fileInput = document.getElementById("paymentInput");
    const file = fileInput.files[0];

    if (file) {
        const reader = new FileReader();

        // Use a promise to wait for the file reading operation to complete
        const base64pdf = await new Promise((resolve, reject) => {
            reader.onloadend = function() {
                resolve(reader.result); // Resolve with the result when reading is done
            };
            reader.onerror = function(error) {
                reject(error);
            };
            reader.readAsDataURL(file);
        });

        const url = "http://localhost:8080/confirmpay";
        try {
            const payload = {
                "file": base64pdf.split(',')[1], // Get only the Base64 data without the data URL prefix
                "payment": product.identifier
            };
            const response = await fetch(url, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(payload),
                credentials: 'include',
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }else {
                alert("Successfully added confirmation")
            }

        } catch (error) {
            console.error(`Error sending data to ${url}:', ${error}`);
            throw error;
        }
    }
}



</script>




{#if product}
<div class=" h-auto mb-10 min-h-screen lg:mx-10 mt-20">
    <h1 class="text-2xl font-bold mt-20">Payment information for {product.name}</h1>
    <h2 class="text-lg my-5">Payment Details</h2>

    <div class=" flex card bg-white-100 shadow-xl">
        <div class="card-body">
            <p>Erstellt von:</p>
            {#each authors as author}
                <p>AU: {author.username}</p>
            {/each}
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

    <input type="file" id="paymentInput" class="file-input file-input-bordered file-input-primary w-full max-w-xs" />
    <button class="button-primary" on:click="{uploadPayment}">Upload</button>

</div>

{:else}
<div class="h-auto mb-10 min-h-screen lg:mx-10 mt-20 flex justify-center items-center">
    <span class="loading loading-dots loading-lg"></span>
</div>
{/if}