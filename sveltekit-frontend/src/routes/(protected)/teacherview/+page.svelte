<script lang=ts>
import { onMount } from 'svelte';
import { writable } from 'svelte/store';
import { get_classes } from '$lib/api/services';

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

let all_classes = [];
let options = []

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
});
</script>

<div class="min-h-screen lg:mx-10 mt-20 relative">
<h1 class="text-2xl font-bold mb-4">Select a Class</h1>

<input type="text" id="searchInput" placeholder="Search..." class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500" bind:value={searchText} />

<div class="absolute left-0 mt-2 w-full rounded-md shadow-lg bg-white z-10" id="dropdownContent" role="listbox" tabindex="0" on:keydown={handleKeyDown} style="display: {isDropdownVisible ? 'block' : 'none'};">
    
    {#each options.filter(option => option.toLowerCase().includes(searchText.toLowerCase())) as filteredOption}
        <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100" on:click|preventDefault={handleOptionClick}>{filteredOption}</a>
    {/each}

</div>

{#if true}
<div class="overflow-x-auto mt-20">
    <table class="table">
    <!-- head -->
    <thead>
        <tr>
        <th></th>
        <th>Lastname</th>
        <th>Firstname</th>
        <th>Class</th>
        </tr>
    </thead>
    <tbody>
        <!-- {#each students as student (student.id)}
        <tr>
            <th>TEST</th>
            <td>TEST</td>
            <td>TEST</td>
            <td>TEST</td>
        </tr>
        {/each} -->
    </tbody>
    </table>
</div>
{/if}





</div>
