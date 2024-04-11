
<script>

    export let productFormData;


</script>


<div class="fixed bottom-0 right-0 mb-10 mr-10">

    <button class="btn btn-success" onclick="paymentModal.showModal()">Neues Produkt</button>
    
    <dialog id="paymentModal" class="modal">
        <div class="modal-box">
            <h3 class="font-bold text-lg">Neues Produkt</h3>
            <p class="py-4">Zum verlassen ESC drücken</p>
            <div class="modal-action">
                <form class="productform" method="dialog" on:submit|preventDefault={createProduct}>
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



                    <button id="submitButton" class="btn btn-success bottom-0 right-0 mb-10 mr-10" type="submit">Fertig</button>
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


