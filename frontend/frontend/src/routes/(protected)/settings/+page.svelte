<script lang="ts">
import { onMount } from 'svelte';

</script>


<div class="min-h-screen lg:mx-10 mt-20 relative">

    <div class="mt-32">
        <svg class="h-8 w-8 mb-2 text-secondary inline-block"  width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">  <path stroke="none" d="M0 0h24v24H0z"/>  <path d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 0 0 2.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 0 0 1.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 0 0 -1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 0 0 -2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 0 0 -2.573 -1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 0 0 -1.065 -2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 0 0 1.066 -2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />  <circle cx="12" cy="12" r="3" /></svg>
        <h1 class=" inline-block text-2xl font-bold mb-4">Einstellungen</h1>
    </div>
   
   
    <div>
      <h2 class="text-xl mt-10">Darstellung</h2>

      <div class="join mt-10 join-hoizontal">
        <input type="radio" name="theme-buttons" class="btn bg-htlyellow border-0 hover:bg-lighttext hover:text-secondary theme-controller join-item" aria-label="Standard HTL" value="default"/>
        <input type="radio" name="theme-buttons" class="btn bg-secondary border-0 text-lighttext hover:bg-lighttext hover:text-secondary theme-controller join-item" aria-label="Dunkel" value="retro"/>
        <input type="radio" name="theme-buttons" class="btn bg-indigo-500 border-0 text-lighttext hover:bg-lighttext hover:text-secondary theme-controller  join-item" aria-label="Kontrastreich" value="cyberpunk"/>
      </div>



      <h2 class="text-xl mt-10">Sprache</h2>
      <select class=" mt-10 select w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500">

        <option>Deutsch</option>
        <option>Englisch</option>
      </select>

      
    <h2 class="text-xl mt-10 ">Leitungsteam kontaktieren</h2>
        <div class="mt-10">
            <a data-tip="Im Haus suchen" class="tooltip" href="https://services.htl-villach.at/findtheteacher/">
                <svg class="mr-4 inline-block h-12 w-12 text-secondary"  viewBox="0 0 24 24"  fill="none"  stroke="currentColor"  stroke-width="2"  stroke-linecap="round"  stroke-linejoin="round">  <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z" />  <polyline points="9 22 9 12 15 12 15 22" /></svg>
            </a>
            <a data-tip="Am Telefon erreichen" class="tooltip" href="https://www.htl-villach.at/kontakt">
                <svg class="mr-4 inline-block h-12 w-12 text-secondary"  width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">  <path stroke="none" d="M0 0h24v24H0z"/>  <path d="M5 4h4l2 5l-2.5 1.5a11 11 0 0 0 5 5l1.5 -2.5l5 2v4a2 2 0 0 1 -2 2a16 16 0 0 1 -15 -15a2 2 0 0 1 2 -2" />  <path d="M15 7a2 2 0 0 1 2 2" />  <path d="M15 3a6 6 0 0 1 6 6" /></svg>
            </a>
            <a data-tip="Eine Nachricht schreiben" class="tooltip" href="https://www.htl-villach.at/kontakt">
                <svg class="inline-block h-12 w-12 text-secondary"  fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/>
                </svg>              
            </a>
        </div>
      

    </div>


</div>
