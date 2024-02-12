<script>
	import Header from "./components/Header.svelte";
	import Footer from "./components/Footer.svelte";
	import Tabs from "./shared/Tabs.svelte";
	import CreatePollForm from "./components/CreatePollForm.svelte";
	import PollList from "./components/PollList.svelte";
	import { tweened} from 'svelte/motion';


	// tabs
	let items = ['Current Polls', 'Add New Poll'];
	let activeItem = 'Current Polls';
	const tabChange = (e) => {
		activeItem = e.detail;
	}



	const handleAdd = (e) => {
		activeItem = 'Current Polls';
	}


	const value = tweened(0);

</script>

<Header />

<main>
	<Tabs {activeItem} {items} on:tabChange={tabChange}/>
	{#if activeItem ==='Current Polls'}
		<PollList />
		{:else if activeItem === 'Add New Poll'}
		<CreatePollForm on:add={handleAdd}/>
	{/if}
</main>


<Footer />
<style>
main{
	max-width: 960px;
	margin: 40px auto;
}
</style>