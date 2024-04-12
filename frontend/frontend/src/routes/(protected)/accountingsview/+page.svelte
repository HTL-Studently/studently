<script lang="ts">
import { onMount } from 'svelte';
import { writable } from 'svelte/store';
import { get_classes, get_students, assign_payment} from '$lib/api/services';
import { DateInput } from 'date-picker-svelte'
import { user } from "$lib/stores/UserStore.js"

    
    let productListRaw = []
    let productList = []

    onMount(async() => {


        async function getProducts() {
            let data;
            try {
                const response = await fetch('http://localhost:8080/product', {
                    credentials: 'include'
                });

                data = await response.json();
                return data
            
            } catch (error) {
                console.error('Error fetching product data:', error);
            }
        }
        productListRaw = await getProducts()

        for(let product of productListRaw) {
            // Format time
            const dueDate = new Date(product.due_date)
            const formatedDueDate = dueDate.toLocaleDateString("de-DE", {
                weekday: "long",
                year: "numeric", 
                month: "2-digit", 
                day: "2-digit",
            });
            const formatedDueTime = dueDate.toLocaleTimeString("de-DE", {
                hour: "numeric",
                minute: "2-digit", 
                second: "2-digit",
                hour12: false,
            })

            const startDate = new Date(product.start_date)
            const formatedStartDate = startDate.toLocaleDateString("de-DE", {
                weekday: "long",
                year: "numeric", 
                month: "2-digit", 
                day: "2-digit",
            });
            const formateStartTime = startDate.toLocaleTimeString("de-DE", {
                hour: "numeric",
                minute: "2-digit", 
                second: "2-digit",
                hour12: false,
            })

            product.due_date = `${formatedDueDate} - ${formatedDueTime}`;
            product.expires = `${formatedStartDate} - ${formateStartTime}`
            productList.push(product)
        }
    })

//sorting and table
let options = []
let selectedClass = "";
let successfullPaymentCreation = null;
let sortColumn = "name";
let sortAscending = true;



//Sortingfunktion
function sortList(column) {
if (sortColumn === column) {
    // If the same column is clicked, toggle the sort order
    sortAscending = !sortAscending;
} else {
    // If a different column is clicked, sort in ascending order by default
    sortColumn = column;
    sortAscending = true;
}

productList = productList.sort((a, b) => {
    if (a[sortColumn] < b[sortColumn]) {
        return sortAscending ? -1 : 1;
    }
    if (a[sortColumn] > b[sortColumn]) {
        return sortAscending ? 1 : -1;
    }
    return 0;
});
}

//verifying incoming payment

let isToggled = false;

function getTogglerState(){
    return isToggled;
}

</script>



<div class="min-h-screen lg:mx-10 mt-20 relative">


    <h1 class="text-2xl font-bold mb-4">Alle Zahlungen</h1>
    <input type="text" id="" placeholder="Search for a payment, class or a student" class="my-4 w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"  />

        <table class="table mb-20">
            <thead>
                <tr>
                    <th on:click={() => sortList('name')}>
                        <span class="inline-block">Produkt</span>
                        <svg class="h-4 w-4 text-secondary inline-block ml-2" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <path stroke="none" d="M0 0h24v24H0z"/>
                            <path d="M3 9l4-4l4 4m-4 -4v14" />
                            <path d="M21 15l-4 4l-4-4m4 4v-14" />
                        </svg>
                    </th>
                    <th on:click={() => sortList('target[0]')}>
                        <span class="inline-block">Schüler</span>
                        <svg class="h-4 w-4 text-secondary inline-block ml-2" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <path stroke="none" d="M0 0h24v24H0z"/>
                            <path d="M3 9l4-4l4 4m-4 -4v14" />
                            <path d="M21 15l-4 4l-4-4m4 4v-14" />
                        </svg>
                    </th>

                    <th on:click={() => sortList('disabled')}>
                        <span class="inline-block">Status</span>
                        <svg class="h-4 w-4 text-secondary inline-block ml-2" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <path stroke="none" d="M0 0h24v24H0z"/>
                            <path d="M3 9l4-4l4 4m-4 -4v14" />
                            <path d="M21 15l-4 4l-4-4m4 4v-14" />
                        </svg>
                    </th>
                    <th>Erstellt am</th>
                    <th>Gültig bis</th> 
                    <th>Ansehen</th>
                </tr>
            </thead>

            <tbody>

                {#each productListRaw as product}
                <tr>
                    <td><h2 class="">{product.name}</h2></td>
                    <td><h2 class="">Schüler</h2></td>

                    <td>
                        {#if product.disabled}    
                            <h2 class="">Geschlossen</h2>
                        {:else}
                            <h2 class="">Offen</h2>
                        {/if}
                    </td>

                    <td><h2 class="">{product.start_date}</h2></td>
                    <td><h2 class="">{product.expires}</h2></td>
                    
                    <td><h2 class=""><button class="btn btn-info btn-xs" href="{`/accountingsview/${product.identifier}`}">Ansehen</button></td>

                </tr>


  
                {/each}


            </tbody>


        </table>


        <div class="fixed bottom-0 right-0 mb-10 mr-10">

            {#if isToggled === true}
                <button class="btn btn-success m-4" onclick="verify.showModal()">Bestätigen</button> 
            {/if}

                
          
        </div>


</div>
