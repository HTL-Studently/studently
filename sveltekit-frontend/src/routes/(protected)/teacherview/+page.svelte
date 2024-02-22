<script lang="ts">
    import { onMount } from 'svelte';
  
    let isDropdownVisible = false;
    let options = ['Option  1', 'Option  2', 'Option  3', 'Option  4'];
  
    onMount(() => {
      const searchInput = document.getElementById('searchInput');
      const dropdownContent = document.getElementById('dropdownContent');
  
      if (searchInput && dropdownContent) {
        searchInput.addEventListener('input', function() {
          let filter = this.value.toUpperCase();
          let aTags = dropdownContent.getElementsByTagName('a');
  
          for (let i =  0; i < aTags.length; i++) {
            let txtValue = aTags[i].textContent || aTags[i].innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
              aTags[i].style.display = "";
            } else {
              aTags[i].style.display = "none";
            }
          }
        });
  
        searchInput.addEventListener('focus', () => {
          dropdownContent.style.display = 'block';
        });
  
        searchInput.addEventListener('blur', () => {
          dropdownContent.style.display = 'none';
        });
  
        // Dynamically add options to the dropdown content
        options.forEach(option => {
          let a = document.createElement('a');
          a.href = '#';
          a.textContent = option;
          a.className = 'block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100';
          dropdownContent.appendChild(a);
        });
      }
    });
  </script>
  
  
  <div class="min-h-screen mt-20 lg:mx-10 relative">
<h1 class="text-2xl font-bold mb-4">Select a Class</h1>

    <input type="text" id="searchInput" placeholder="Search..." class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500" />
    <div class="absolute left-0 mt-2 w-full rounded-md shadow-lg bg-white z-10" id="dropdownContent" style="display: none;">
      <!-- Options will be dynamically added here -->
    </div>
  </div>
  