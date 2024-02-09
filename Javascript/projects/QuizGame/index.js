const prompt = require("prompt-sync")();

console.log("welcome to the Cam Quiz!")

// Declare initial variables
let correct = 0;
let incorrect = 0;

const answer1 = prompt("What is my favorite color? ");
const correctAnswer1 = "black"

if (answer1.toLowerCase() === correctAnswer1){
    console.log("Correct")
    correct ++
}
else{
    console.log("incorrect. The correct answer was", correctAnswer1)
    incorrect ++
}

const answer2 = prompt("What is my favorite food? mexican or chinese? ");
const correctAnswer2 = "mexican"

if (answer2.toLowerCase() === correctAnswer2){
    console.log("Correct")
    correct ++
}
else{
    console.log("incorrect. The correct answer was", correctAnswer2)
    incorrect ++
}

const answer3 = prompt("How old am I? ");
const correctAnswer3 = "35"

if (answer3.toString() === correctAnswer3){
    console.log("Correct")
    correct ++
}
else{
    console.log("incorrect. The correct answer was", correctAnswer3)
    incorrect ++
}

const answer4 = prompt("What is my favorite thing to do? ");
const correctAnswer4 = "nothing"

if (answer4.toLowerCase() === correctAnswer4){
    console.log("Correct")
    correct ++
}
else{
    console.log("incorrect. The correct answer was", correctAnswer4)
    incorrect ++
}

const answer5 = prompt("What is my life's goal? [1] To be rich, [2] Start a business, [3] Be a good dad, [4] All of the above ");
const correctAnswer5 = "4"

if (answer5.toString() === correctAnswer5){
    console.log("Correct")
    correct ++
}
else{
    console.log("incorrect. The correct answer was", correctAnswer5, "All of the above")
    incorrect ++
}



// Calculate final score
const percent = Math.round((correct / (correct+incorrect)) * 100).toString()

console.log("You got", correct, "correct and", incorrect, "incorrect");
console.log("Your score was", percent + "%");

