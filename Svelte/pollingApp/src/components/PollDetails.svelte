<script>
    export let poll;
    import Card from '../shared/Card.svelte';
    import Button from '../shared/Button.svelte';
    import PollStore from '../stores/PollStore';

    // reactive vote value
    $: totalVotes = poll.votesA + poll.votesB;

    $: percentA = Math.floor(100 / totalVotes * poll.votesA) || 0;
    $: percentB = Math.floor(100 / totalVotes * poll.votesB) || 0;


    const handleDelete = (id) => {
        PollStore.update(currentPolls => {
            return currentPolls.filter(poll => poll.id != id)
        });
    };
</script>


<Card>
    <div class="poll">
        <h3>{ poll.question}</h3>
        <p>Total votes: {totalVotes}</p>
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <div class="answer" on:click={() => poll.votesA++}>
            <div class="percent percent-a" style="width: {percentA}%"></div>
            <span>{ poll.answerA } ({ poll.votesA })</span>
        </div>
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <div class="answer" on:click={() => poll.votesB++}>
            <div class="percent percent-b" style="width: {percentB}%"></div>
            <span>{ poll.answerB } ({ poll.votesB })</span>
        </div>
        <div class="delete"><Button flat={true} on:click={() => {handleDelete(poll.id)}}>Delete</Button></div>
    </div>
    

</Card>


<style>
h3{
    margin: 0 auto;
    color: #555;
}
p{
    margin-top: 6px;
    font-size: 14px;
    color: #aaa;
    margin-bottom: 30px;
}
.answer{
    background: #fafafa;
    cursor: pointer;
    margin: 10px auto;
    position: relative;
}
.answer:hover{
    opacity: 0.7;
}
span{
    display: inline-block;
    padding: 10px 20px;
}
.percent{
    height: 100%;
    position: absolute;
    box-sizing: border-box;
}
.percent-a{
    border-left: 2px solid #d91b42;
    background: rgba(217,27,66,0.2);
    transition: width 0.4s;
}
.percent-b{
    border-left: 2px solid #45c496;
    background: rgba(69,196,150,0.2);
    transition: width 0.4s;
}
.delete{
    margin-top: 30px;
    text-align: center;
}
</style>