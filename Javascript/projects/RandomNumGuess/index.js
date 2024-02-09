const prompt = require("prompt-sync")();

console.log("welcome to the Random Number Guesser!")
console.log("")


const target = Math.round(Math.random() * 100)

let guesses = 0;


while(true){
    const guess = Number(prompt("Guess the number (0-100): "))
    guesses ++
if (guess > target) {
    console.log("You guessed too high")
} else if (guess < target) {
    console.log("You guessed too low")
} else {
    if (guesses === 1){
        console.log("You guessed it on the first try!!! WOW!!!!!")
        break
    }
    else {
        console.log("You guessed the number! Great job!!!")
        break
    }
}
}


console.log("The number was", target)
console.log("It took you", guesses, "guesses")