import { writable } from 'svelte/store';

export const user = writable({
    disabled: true,
    identifier: "",
    username: "",
    firstname: "empty",
    lastname: "empty",
    email: "",
    expires: "",
    created: "",
    sclass: "",
    type: "",
    owned_objects: "",
    owned_payments: "",
});

// user.subscribe((value) => {
//     console.log(value)
// })