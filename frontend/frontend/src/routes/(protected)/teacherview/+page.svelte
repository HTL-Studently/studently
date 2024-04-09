<script lang=ts>
import { onMount } from 'svelte';
import { writable } from 'svelte/store';
import { get_classes, get_students, assign_payment} from '$lib/api/services';
import { user } from "$lib/stores/UserStore.js"
import { DateInput } from 'date-picker-svelte'

// All classes list
export let data;

let selectedOptionStore = writable('');
let searchText = '';
let isDropdownVisible = false; // Reactive variable to toggle dropdown visibility

let options = []
let selectedClass = "";
let student_list = [];

let productFormData = {
    disabled: false,
    name: "Produkt123",
    author: "",
    target: [],
    info: "Beschreibung",
    cost: 10,
    iban: "IBAN",
    bic: "BIC",
    start_date: new Date(),
    due_date: new Date(),
    expires: new Date(),

};


function handleOptionClick(event) {
    const targetOption = event.target.textContent;
    selectedOptionStore.set(targetOption);
    searchText = targetOption.trim();
    isDropdownVisible = false; // Hide the dropdown when an option is clicked
}


async function paymentSubmit(event) {
    event.preventDefault();
    await assign_payment(productFormData)


}


onMount(async() => {
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








</script>

<div class="min-h-screen lg:mx-10 mt-20 relative">

    <h1 class="text-2xl font-bold mb-4">Select a Class</h1>
    <input type="text" id="searchInput" placeholder="Search..." class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500" bind:value={searchText} />


    <div class="absolute left-0 mt-2 w-full rounded-md shadow-lg bg-white z-10" id="dropdownContent" role="listbox" tabindex="0" style="display: {isDropdownVisible ? 'block' : 'none'};">
        
        {#each options.filter(option => option.toLowerCase().includes(searchText.toLowerCase())) as filteredOption}
            <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100" on:click|preventDefault={handleOptionClick}>{filteredOption}</a>
        {/each}

    </div>


    {#if selectedClass != ""}
    <div class="overflow-x-auto mt-20">
        <table class="table">
        <!-- head -->
        <p></p>
        <thead>
            <tr>
            <th>{selectedClass}</th>
            <th>Lastname</th>
            <th>Firstname</th>
            <th>Class</th>
            <th>Payments and Licenses</th>
            </tr>
        </thead>
        <tbody>
            {#each student_list as student}
            <tr>
                <th>{student["identifier"]}</th>
                <td>{student["lastname"]}</td>
                <td>{student["firstname"]}</td>
                <td>{student["sclass"]}</td>
                
                <td>
                    <thead>
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
                    
                    {/each}
                </td>




            </tr>
            {/each}
        </tbody>
        </table>
    </div>
    {/if}


    <div class="fixed bottom-0 right-0 mb-10 mr-10">

        <button class="btn btn-primary m-4" onclick="paymentModal.showModal()">Neues Produkt</button>
        
        <dialog id="paymentModal" class="modal">
            <div class="modal-box">
                <h3 class="font-bold text-lg">Neues Produkt</h3>
                <p class="py-4">Zum verlassen ESC drücken</p>
                <div class="modal-action">
                    <form class="productform" method="dialog">
                        <button class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">✕</button>


                        <label>
                            <div class="label">
                                <span class="label-text">Produktname</span>
                                <input class="input w-full max-w-xs right-0" type="text" bind:value="{productFormData.name}" placeholder="Produkt123" />
                            </div>
                        </label>

                        <label>
                            <div class="label">
                                <span class="label-text">Produktbeschreibung</span>
                                <input class="input w-full max-w-xs right-0" type="text" bind:value="{productFormData.info}" placeholder="Beschreibung" />
                            </div>
                        </label>


                        <div class="divider">Kosten</div>


                        <label>
                            <div class="label">
                                <span class="label-text">Preis</span>
                                <input class="input w-full max-w-xs right-0" type="text" data-type="currency" bind:value="{productFormData.cost}" placeholder="10€" />
                            </div>
                        </label>

                        <label>
                            <div class="label">
                                <span class="label-text">IBAN</span>
                                <input class="input w-full max-w-xs right-0" type="text" bind:value="{productFormData.iban}" placeholder="IBAN" />
                            </div>
                        </label>

                        <label>
                            <div class="label">
                                <span class="label-text">BIC</span>
                                <input class="input w-full max-w-xs right-0" type="text" bind:value="{productFormData.bic}" placeholder="BIC" />
                            </div>
                        </label>


                        <div class="divider">Zeitrahmen</div>
                        
                        <!-- svelte-ignore a11y-label-has-associated-control -->
                        <label>
                            <div class="label">
                                <span class="label-text">Start der Einzahlung</span>
                                <DateInput bind:value={productFormData.start_date} />
                            </div>
                        </label>

                        <!-- svelte-ignore a11y-label-has-associated-control -->
                        <label>
                            <div class="label">
                                <span class="label-text">Ende der Einzalung</span>
                                <DateInput bind:value={productFormData.due_date} />
                            </div>
                        </label>

                        <!-- svelte-ignore a11y-label-has-associated-control -->
                        <label>
                            <div class="label">
                                <span class="label-text">Ablaufdatum des Produkts</span>
                                <DateInput bind:value={productFormData.expires} />
                            </div>
                        </label>



                        <button id="submitButton" class="btn btn-success bottom-0 right-0 mb-10 mr-10">Submit</button>
                        <!-- <button class="btn bottom-0 right-0 mb-10 mr-10" on:click|preventDefault="{closeModal}">Close</button> -->

                    </form>






                </div>
            </div>
        </dialog>
    </div>
</div>


