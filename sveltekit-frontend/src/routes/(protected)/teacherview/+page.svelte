<script lang=ts>
import { onMount } from 'svelte';
import { writable } from 'svelte/store';
import { get_classes, get_students, assign_payment} from '$lib/api/services';
import { user } from "$lib/stores/UserStore.js"

let isSearchInputFocused = false;

let selectedOptionStore = writable('');
let searchText = '';
let isDropdownVisible = false; // Reactive variable to toggle dropdown visibility
let isTableVisible = false; // Reactive variable to toggle table visibility

selectedOptionStore.subscribe(value => {
    console.log('Selected option:', value);
    isTableVisible = !!value; // Set isTableVisible to true if a value is selected, false otherwise
});

function handleOptionClick(event) {
    const targetOption = event.target.textContent;
    selectedOptionStore.set(targetOption);
    searchText = targetOption.trim();
    isDropdownVisible = false; // Hide the dropdown when an option is clicked
}

function handleKeyDown(event) {
    if (event.key === 'Enter' || event.key === ' ') {
        const activeOption = document.activeElement.textContent;
        selectedOptionStore.set(activeOption);
        searchText = activeOption.trim();
        isDropdownVisible = false; // Hide the dropdown when Enter or Space is pressed
    }
}

let payment_window = false;
let license_window = false;

let all_classes = [];
let options = []
let selectedClass = "";
let student_list = [];

onMount(async() => {
    all_classes = await get_classes()
    all_classes = all_classes["message"]

    for(let i = 0; i < all_classes.length; i++) {
        options.push(all_classes[i]["name"])
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


    let paymentFormData = { // Define an object to hold form data
        disabled: false,
        id: '',
        name: '',
        author: $user.identifier,
        target: selectedClass,
        product: '',
        confirmation: '',
        payed: '',
        cost: '',
        iban: '',
        bic: '',
        start_date: '',
        due_date: '',
        expires: ''

    };

    async function paymentSubmit(event) {
        event.preventDefault();


        await assign_payment(paymentFormData)

        
    }





</script>

<div class="min-h-screen lg:mx-10 mt-20 relative">
<h1 class="text-2xl font-bold mb-4">Select a Class</h1>

<input type="text" id="searchInput" placeholder="Search..." class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500" bind:value={searchText} />

<div class="absolute left-0 mt-2 w-full rounded-md shadow-lg bg-white z-10" id="dropdownContent" role="listbox" tabindex="0" on:keydown={handleKeyDown} style="display: {isDropdownVisible ? 'block' : 'none'};">
    
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

        <button class="btn btn-primary m-4" onclick="paymentModal.showModal()">Create Payment</button>
        <button class="btn btn-primary  m-4" onclick="licenseModal.showModal()">Create License</button>
        
        <dialog id="paymentModal" class="modal">
            <div class="modal-box">
            <h3 class="font-bold text-lg">Create Payment</h3>
            <p class="py-4">Press ESC key or click the button below to close</p>
            <div class="modal-action">
                <form method="dialog" on:submit={paymentSubmit}>



                    <input class="input w-full max-w-xs right-0" type="text" bind:value="{paymentFormData.name}" placeholder="Name" />
                    <input class="input w-full max-w-xs right-0" type="text" bind:value="{paymentFormData.product}" placeholder="Product/License" />
                    

                    <input class="input w-full max-w-xs right-0" type="text" bind:value="{paymentFormData.cost}" placeholder="Cost" />
                    <input class="input w-full max-w-xs right-0" type="text" bind:value="{paymentFormData.iban}" placeholder="IBAN"/>
                    <input class="input w-full max-w-xs right-0" type="text" bind:value="{paymentFormData.bic}" placeholder="BIC"/>
                    
                    <input class="input w-full max-w-xs right-0" type="text" bind:value="{paymentFormData.start_date}" placeholder="Start Date" />
                    <input class="input w-full max-w-xs right-0" type="text" bind:value="{paymentFormData.due_date}" placeholder="Due Date" />
                    <input class="input w-full max-w-xs right-0" type="text" bind:value="{paymentFormData.expires}" placeholder="Expiration Date" />

                    <button class="btn btn-success bottom-0 right-0 mb-10 mr-10" type="submit" on:click{paymentSubmit}>Submit</button>
                    <!-- <button class="btn bottom-0 right-0 mb-10 mr-10" on:click|preventDefault="{closeModal}">Close</button> -->

                </form>


                <!--  -->


            </div>
            </div>
        </dialog>
        
        <dialog id="licenseModal" class="modal">
            <div class="modal-box">
            <h3 class="font-bold text-lg">Create License!</h3>
            <p class="py-4">Press ESC key or click the button below to close</p>
            <div class="modal-action">
                <form method="dialog">
                <!-- if there is a button in form, it will close the modal -->
                <button class="btn">Close</button>
                </form>
            </div>
            </div>
        </dialog>

    </div>






</div>
