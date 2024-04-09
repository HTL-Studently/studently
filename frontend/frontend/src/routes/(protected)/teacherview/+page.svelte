<script lang=ts>
import { onMount } from 'svelte';
import { writable } from 'svelte/store';
import { get_classes, get_students, assign_payment} from '$lib/api/services';
import { user } from "$lib/stores/UserStore.js"

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


function handleOptionClick(event) {
    const targetOption = event.target.textContent;
    selectedOptionStore.set(targetOption);
    searchText = targetOption.trim();
    isDropdownVisible = false; // Hide the dropdown when an option is clicked
}






async function fetchResults() {
    console.log("Button clicked")
    const response = await fetch('http://localhost:8080/profile', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        credentials: 'include',
    });

    if (response.ok) {
        const data = await response.json();
        console.log(data)
    } else {
        console.error('Failed to fetch profile');
    }

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

    <button on:click={fetchResults}>ZTESET</button>

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

</div>

<div class="fixed bottom-0 right-0 mb-10 mr-10">

    <button class="btn btn-primary m-4" onclick="paymentModal.showModal()">Create Product</button>
    
    <dialog id="paymentModal" class="modal">
        <div class="modal-box">
        <h3 class="font-bold text-lg">Create Payment</h3>
        <p class="py-4">Press ESC key or click the button below to close</p>
        
        
        <div class="modal-action">
            <form method="dialog" on:submit={paymentSubmit}>



                <input class="forminput" type="text" bind:value="{productFormData.name}" placeholder="Name" />
                <div class="label">
                    <span class="label">The name of your new product</span>
                </div>

                <input class="forminput" type="text" bind:value="{productFormData.product}" placeholder="Product/License" />
                <div class="label">
                    <span class="label">The name of your new product</span>
                </div>   

                

                <input class="forminput" type="text" bind:value="{productFormData.cost}" placeholder="Cost" />
                <input class="forminput" type="text" bind:value="{productFormData.iban}" placeholder="IBAN"/>
                <input class="forminput" type="text" bind:value="{productFormData.bic}" placeholder="BIC"/>
                
                <input class="forminput" type="text" bind:value="{productFormData.start_date}" placeholder="Start Date" />
                <input class="forminput" type="text" bind:value="{productFormData.due_date}" placeholder="Due Date" />
                <input class="forminput" type="text" bind:value="{productFormData.expires}" placeholder="Expiration Date" />

                <button class="btn btn-success bottom-0 right-0 mb-10 mr-10" type="submit" on:click{paymentSubmit}>Submit</button>
                <!-- <button class="btn bottom-0 right-0 mb-10 mr-10" on:click|preventDefault="{closeModal}">Close</button> -->

            </form>


            <!--  -->


        </div>
        </div>
    </dialog>
</div>

<style>

    .forminput {
        @apply
        input 
        w-full 
        max-w-xs 
        right-0
        my-2
    }

</style>

