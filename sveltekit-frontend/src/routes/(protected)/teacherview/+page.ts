interface Item {
    name: string;
    text: string;
}

const values: Item[] = [
    {name: "Slug One", text: "I am text slug 1 "},
    {name: "Slug Two", text: "I am text slug 2 "},
    {name: "Slug Three", text: "I am text slug 3 "},
];

export function load(): { items: Item[] } {
    return {
        items: values
    };
}