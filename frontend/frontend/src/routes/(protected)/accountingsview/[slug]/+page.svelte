<script lang="ts">
    import { user } from "$lib/stores/UserStore.js"
    import { onMount } from 'svelte';


    export let data; 

    let userValue;
    user.subscribe((value) => {
        userValue = value;
    })


    let product
    let studentIDList = []
    let studentList = []
    let formatedDueDate;
    let formatedDueTime;
    let formatedStartDate;
    let formateStartTime;
    let authors = [];
    let doneFetchingStudents = false

    
    onMount(async() => {

        console.log("SLUG: ", data.slug)

        let url = "http://localhost:8080/profile"
        try {
            const response = await fetch(`${url}?product=${data.slug}`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                credentials: 'include',
            })

            const result = await response.json();
            studentIDList = result.message.profile
            console.log("RESULT: ", studentIDList)

        } catch (error) {
            console.error(`Error sending data to ${url}:', ${error}`);
            throw error;
        }


        url = "http://localhost:8080/product"
        try {
            const response = await fetch(`${url}?id=${data.slug}`, {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                },
                credentials: 'include',
            })
            const result = await response.json();
            product = result[0]


        } catch (error) {
            console.error(`Error sending data to ${url}:', ${error}`);
            throw error;
        }


        for(let id in studentIDList) {
            url = "http://localhost:8080/profile"
            try {
                const response = await fetch(`${url}?id=${id}`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    credentials: 'include',
                })

                const result = await response.json();
                studentList.push(result.message.profile)
                

            } catch (error) {
                console.error(`Error sending data to ${url}:', ${error}`);
                throw error;
            }
        }
        doneFetchingStudents = true
        print("ACUALSS: ", studentList)


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


    }
)




</script>




{#if product && studentList && doneFetchingStudents}
<div class=" h-auto mb-10 min-h-screen lg:mx-10 mt-20">
    <h1 class="text-2xl font-bold mt-20">Produktinformationen für {product.name}</h1>

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


    <table class="table mb-20">
        <thead>
            <tr>
                <th>Vorname</th>
                <th>Nachname</th>
            </tr>
        </thead>
        
        <tbody>
            {#each studentList as student}
                <tr>
                    <td><h2>{student.lastname}</h2></td>
                    <td><h2>{student.firstname}</h2></td>
                </tr>
            {/each}
        </tbody>

</div>

{:else}
<div class="h-auto mb-10 min-h-screen lg:mx-10 mt-20 flex justify-center items-center">
    <span class="loading loading-dots loading-lg"></span>
</div>
{/if}