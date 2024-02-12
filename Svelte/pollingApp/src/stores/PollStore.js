import { writable } from 'svelte/store';

const PollStore = writable([
    {
        id: 1,
        question: 'Python or Javascript?',
        answerA: 'Python',
        answerB: 'Javascript',
        votesA: 9,
        votesB: 15,
    },
]);


export default PollStore;