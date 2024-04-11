<script>
	import { createEventDispatcher } from 'svelte';

	const dispatch = createEventDispatcher();

	export let label;
	export let id = '';
	export let type = 'text';
	export let placeholder = '';
	export let value = '';

	const handleInput = ({ target }) => {
		value = target.value;
	};

	const handleKeypress = ({ charCode }) => {
		if (charCode === 13) dispatch('submit');
	};
</script>

<div>
	{#if label}
		<label for={id}>{label}</label>
	{/if}
	<input
		{id}
		{type}
		{placeholder}
		{value}
		on:keypress={handleKeypress}
		on:input={handleInput}
	/>
</div>
