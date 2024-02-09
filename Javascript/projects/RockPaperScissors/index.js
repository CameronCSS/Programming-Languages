const prompt = require("prompt-sync")();

let wins = 0;
let losses = 0;
let ties = 0;



while(true){
const choices = ["rock", "paper", "scissors"]
const randomIndex = Math.round(Math.random() * 2)

const pcChoice = choices[randomIndex]
const playerChoice = prompt("Enter rock, paper, or scissors: (press e to end) ").toLowerCase()
if (playerChoice.toLowerCase() === "e"){
    break;
}
else if (playerChoice !== "rock" && playerChoice !== "paper" && playerChoice !== "scissors" ){
    console.log("Please enter a valid playerChoice")
    continue;
}
if (playerChoice === "rock" && pcChoice === "paper" || playerChoice === "paper" && pcChoice === "scissors" || playerChoice === "scissors" && pcChoice === "rock" ){
    console.log("The PC chose", pcChoice)
    console.log("You lost!")
    losses ++
} else if (playerChoice === pcChoice){ 
    console.log("You both chose", playerChoice)
    console.log("DRAW!")
    ties ++
}
else{
    console.log("the PC chose", pcChoice)
    console.log("You Won!")
    wins ++
}
}


console.log("Wins:", wins, "Losses:", losses, "Tied", ties)

