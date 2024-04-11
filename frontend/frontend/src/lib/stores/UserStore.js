import { writable } from 'svelte/store';

export const user = writable({
    disabled: true,
    identifier: "",
    username: "",
    firstname: "",
    lastname: "",
    email: "",
    expires: "",
    created: "",
    sclass: "",
    type: "",
    owned_objects: "",
    owned_payments: "",
});

