<script>
    import { onMount } from "svelte"
    import { user } from "$lib/stores/UserStore"

    let savestore = false

    $: if (savestore && $user) {
        window.sessionStorage.setItem("store", JSON.stringify($user))
    }

    onMount(async () => {
      let ses = window.sessionStorage.getItem("store")
        if (ses) {
            console.log("sob-- ~ loading ses", ses)
            $user = JSON.parse(ses)
        }
        savestore = true
    })
</script>