<script lang=ts>
import { onMount } from 'svelte';
import { writable } from 'svelte/store';
import { get_classes, get_students, assign_payment} from '$lib/api/services';
import { DateInput } from 'date-picker-svelte'
import { user } from "$lib/stores/UserStore.js"
import {v4 as uuidv4} from 'uuid';

// All classes list
export let data;



let userIdentifier;

let userValue;
    user.subscribe((value) => {
        userValue = value;
        userIdentifier = userValue.identifier
    })

let selectedOptionStore = writable('');
let searchText = '';
let isDropdownVisible = false; // Reactive variable to toggle dropdown visibility

//sorting and table
let options = []
let selectedClass = "";
let student_list = [];
let targetList = [];
let targetIntput = "";
let successfullPaymentCreation = null;
let sortColumn = "lastname";
let sortAscending = true;

let productFormData;
productFormData = {
        disabled: false,
        name: "",
        author: [userIdentifier],
        target: targetList,
        info: "",
        cost: 0.0,
        iban: "",
        bic: "",
        start_date: new Date(),
        due_date: new Date(),
        expires: new Date(),
        delete_date: new Date(),
    };

function handleOptionClick(event) {
    const targetOption = event.target.textContent;
    selectedOptionStore.set(targetOption);
    searchText = targetOption.trim();
    isDropdownVisible = false; // Hide the dropdown when an option is clicked
}

function addToTargetList() {
    if(options.includes(targetIntput)) {
        if(targetList.includes(targetIntput)) {
            console.log("Already included")
            targetIntput = "" // Clears input field
        }else {
            console.log("TRYING TO ADD ", targetIntput)
            targetList = [...targetList, targetIntput]
            console.log(targetList)
            targetIntput = "" // Clears input field
        }

    }else {
        console.log("Not a valid class")
        targetIntput = "" // Clears input field
    }
}

function removeFromTargetList(target) {
    targetList = targetList.filter(i => i !== target);
}



async function createProduct() {
    try {
        productFormData.target = targetList

        const response = await fetch('http://localhost:8080/product', {
            method: 'POST',
            headers: {
            'Content-Type': 
            'application/json',
            },
            credentials: 'include',
            body: JSON.stringify(productFormData),
        });
        
        const data = await response.json();

        if(data) {
            successfullPaymentCreation = true;
        } else {
            successfullPaymentCreation = false;
        }

    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
    }
}

async function getProducts() {
    try {
        const response = await fetch('http://localhost:8080/product', {
            credentials: 'include'
        });
        data = await response.json();
        console.log(data)
    } catch (error) {
        console.error('Error fetching product data:', error);
    }
}

onMount(async() => {
    // await getProducts()
    data = data["message"]

    for(let i = 0; i < data.length; i++) {
        options.push(data[i]["name"])
    }
    const dropdownContent = document.getElementById('dropdownContent');
    const searchInput = document.getElementById('searchInput');

    // Show the dropdown when the search input is focused
    searchInput.addEventListener('focus', () => {
        isDropdownVisible = true;
    });

    // Hide the dropdown when clicking outside of it
    document.addEventListener('click', (event) => {
        if (!dropdownContent.contains(event.target) && !searchInput.contains(event.target)) {
        isDropdownVisible = false;
        }
    });

    searchInput.addEventListener("change", async function(event) {
        selectedClass = searchInput.value;
        student_list = await get_students(selectedClass);
        console.log(student_list);
    });

});


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

        student_list = student_list.sort((a, b) => {
            if (a[sortColumn] < b[sortColumn]) {
                return sortAscending ? -1 : 1;
            }
            if (a[sortColumn] > b[sortColumn]) {
                return sortAscending ? 1 : -1;
            }
            return 0;
        });
}

</script>





<div class="min-h-screen lg:mx-10 mt-20 relative">

    <h1 class="text-2xl font-bold mb-4">Select a Class</h1>
    <input type="text" id="searchInput" placeholder="Search..." class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500" bind:value={searchText} />


    <div class="absolute left-0 mt-2 w-full rounded-md shadow-lg bg-white z-10" id="dropdownContent" role="listbox" tabindex="0" style="display: {isDropdownVisible ? 'block' : 'none'};">
        
        {#each options.filter(option => option.toLowerCase().includes(searchText.toLowerCase())) as filteredOption}
            <button class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100" on:click|preventDefault={handleOptionClick}>{filteredOption}</button>
        {/each}

    </div>


    <!-- Class list table -->
    {#if selectedClass != ""}
    <div class="overflow-x-auto mt-20">
        <table class="table">
        <!-- head -->
        <p></p>

        <thead>
            <tr>
                <th>{selectedClass}</th>
                <th on:click={() => sortList('lastname')}>
                    <span class="inline-block">Lastname</span>
                    <svg class="h-4 w-4 text-secondary inline-block ml-2" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                        <path stroke="none" d="M0 0h24v24H0z"/>
                        <path d="M3 9l4-4l4 4m-4 -4v14" />
                        <path d="M21 15l-4 4l-4-4m4 4v-14" />
                    </svg>
                </th>
                <th on:click={() => sortList('firstname')}>
                    <span class="inline-block">Firstname</span>
                    <svg class="h-4 w-4 text-secondary inline-block ml-2" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                        <path stroke="none" d="M0 0h24v24H0z"/>
                        <path d="M3 9l4-4l4 4m-4 -4v14" />
                        <path d="M21 15l-4 4l-4-4m4 4v-14" />
                    </svg>
                </th>
                <th> Class</th>
                <th>Payments and Licenses</th>
            </tr>
        </thead>
        




        <tbody>
            {#each student_list as student}
            <tr class="hover">
                <!-- <th>{student["identifier"]}</th> -->
                <td></td>
                <td>{student["lastname"]}</td>
                <td>{student["firstname"]}</td>
                <td>{student["sclass"]}</td>
                

                <td>
                    <button class="btn btn-primary bg-htlyellow">View for this student</button>
                    <!-- <thead>
                        <th>Payment</th>
                        <th>Paid</th>
                        <th>Confirmation</th>
                    </thead>
                    {#each student["owned_payments"] as payment}
    
                        <tr>
                            <td>{payment["name"]}</td>
                            <td>
                                {#if payment["payed"]}    
                                    Yes
                                {:else}
                                    No
                                {/if}
                            
                            </td>
                            <td>
                                
                                {#if payment["confirmation"]}    
                                    Yes
                                {:else}
                                    -
                                {/if}
                                
                            </td>
                        </tr>
                    
                    {/each} -->
                </td>
            </tr>
            {/each}
        </tbody>


        </table>
    </div>
    {/if}


</div>



    <div class="fixed bottom-0 right-0 mb-10 mr-10">

        <button class="btn btn-primary m-4" onclick="paymentModal.showModal()">Neues Produkt</button>
        
        <dialog id="paymentModal" class="modal">
            <div class="modal-box">
                <h3 class="font-bold text-lg">Neues Produkt</h3>
                <p class="py-4">Zum verlassen <kbd class="kbd kbd-lg">ESC</kbd> drücken</p>
                <div class="modal-action m-0 p-0">
                    <form class="productform" method="dialog" on:submit|preventDefault={createProduct}>
                        <button class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">✕</button>


                        <div class="divider divider-accent">Allgemein</div>


                        <input class="input input-bordered input-accent w-full max-w-xs my-2 shadow-lg" type="text" bind:value="{productFormData.name}" placeholder="Produkt123" />
                        <input class="input input-bordered input-accent w-full max-w-xs my-2 shadow-lg" type="text" bind:value="{productFormData.info}" placeholder="Beschreibung" />

                        <p>Target List</p>
                        <ul>
                            {#each targetList as target}
                                <li class="flex">
                                    <p>- {target}</p>
                                    <button on:click={() => removeFromTargetList(target)}>Remove</button>
                                </li>

                            {/each}

                        </ul>

                        <input class="input input-bordered input-accent w-full max-w-xs my-2 shadow-lg" type="text" bind:value="{targetIntput}" placeholder="Zielgruppe" />
                        <button on:click|preventDefault={addToTargetList}>Add</button>

                        <div class="divider divider-accent">Kosten</div>


                        <input class="input input-bordered input-accent w-full max-w-xs my-2 shadow-lg" type="text" data-type="currency" bind:value="{productFormData.cost}" placeholder="10€" />
                        <input class="input input-bordered input-accent w-full max-w-xs my-2 shadow-lg" type="text" bind:value="{productFormData.iban}" placeholder="IBAN" />
                        <input class="input input-bordered input-accent w-full max-w-xs my-2 shadow-lg" type="text" bind:value="{productFormData.bic}" placeholder="BIC" />


                        <div class="divider divider-accent">Zeitrahmen</div>
                        

                        <DateInput class="shadow-lg my-2" bind:value={productFormData.start_date} />
                        <DateInput class="shadow-lg my-2" bind:value={productFormData.due_date} />
                        <DateInput class="shadow-lg my-2" bind:value={productFormData.expires} />
                        <DateInput class="shadow-lg my-2" bind:value={productFormData.delete_date} />




                        <button id="submitButton" class="btn btn-success bottom-0 right-0 mb-10 mr-10" type="submit" on:click|preventDefault={createProduct}>Fertig</button>
                        <!-- <button class="btn bottom-0 right-0 mb-10 mr-10" on:click|preventDefault="{closeModal}">Close</button> -->

                        {#if successfullPaymentCreation === true}
                            <p>Product Successfully created</p>
                        {/if}

                        {#if successfullPaymentCreation === false}
                            <p>Error creating Product</p>
                        {/if}


                    </form>


                <!--  -->


            </div>
            </div>
        </dialog>
    </div>


