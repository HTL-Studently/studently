<script>
    let isDropdownVisible = false;
    let selectedOption = '';
    let options = ['Option 1', 'Option 2', 'Option 3', 'Option 4'];

    function toggleDropdown() {
        isDropdownVisible = !isDropdownVisible;
    }

    function selectOption(option) {
        selectedOption = option;
        isDropdownVisible = false; // Hide the dropdown after selecting an option
    }
</script>

<div class="dropdown mt-20">
    <button on:click={toggleDropdown}>
        {selectedOption || 'Select an option'}
    </button>
    <div class="dropdown-content" style="display: {isDropdownVisible ? 'block' : 'none'};">
        {#each options as option}
            <div on:click={() => selectOption(option)}>
                {option}
            </div>
        {/each}
    </div>
</div>

<style>
    .dropdown {
        position: relative;
        display: inline-block;
    }

    .dropdown-content {
        display: none;
        position: absolute;
        background-color: #f9f9f9;
        min-width: 160px;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 1;
    }

    .dropdown-content div {
        color: black;
        padding: 12px 16px;
        text-decoration: none;
        display: block;
    }

    .dropdown-content div:hover {
        background-color: #f1f1f1;
    }
</style>
