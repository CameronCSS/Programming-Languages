const prompt = require("prompt-sync")();

// define the slot machine symbols, rows, and columns
const ROWS = 3;
const COLS = 3;

const SYMBOLS_COUNT = {
    '🤑': 2,
    '💰': 4,
    '🍀': 6,
    '💩': 8
};

const SYMBOL_VALUES = {
    '🤑': 5,
    '💰': 4,
    '🍀': 3,
    '💩': 2
};



// Deposit some money
const getDeposit = () => {
    while (true) {
    console.clear();
    console.log("");
    const depositAmount = prompt("Enter a deposit amount: ");
    const numberDepositAmount = parseFloat(depositAmount);

    if (isNaN(numberDepositAmount) || numberDepositAmount <= 0) {
        console.log("Invalid deposit. Try again");
    } else{
        console.clear();
        return numberDepositAmount;

    }

    }
};




// determine number of lines to bet on
const getNumbersOfLines = () => {
    while (true) {
        console.log("");
        const lines = prompt("Enter the number of lines to bet on (1-3): ");
        const numbersOfLines = parseFloat(lines);
    
        if (isNaN(numbersOfLines) || numbersOfLines <= 0 || numbersOfLines > 3) {
            console.log("Invalid entry. Please Pick 1-3 ");
        } else{
            return numbersOfLines;
    
        }
    
        }
};


// collect the bet amount
const getBetAmount = (balance, lines) => {
    while (true) {
        console.log("");
        const amount = prompt("Enter the bet per line: ");
        const betAmount = parseFloat(amount);
    
        if (isNaN(betAmount) || betAmount <= 0) {
            console.log("Please pick a valid number");
        } else if(betAmount > balance / lines){
            console.log("You can't bet more money than you have deposited.");
        } else {

            return betAmount;
        }
    
        }
};


// spin the slot machine
const spin = () => {
    const symbols = [];
    for (const [symbol, count] of Object.entries(SYMBOLS_COUNT)){
        for (let i =0; i < count; i++) {
            symbols.push(symbol);
        }
    }

    const reels = [];
    for (let i = 0; i < COLS; i++) {
        reels.push([]);
        const reelSymbols = [...symbols];
        for (let j = 0; j < ROWS; j++){
            const randomIndex = Math.floor(Math.random() * reelSymbols.length);
            const selectedSymbol = reelSymbols[randomIndex];
            reels[i].push(selectedSymbol);
            reelSymbols.splice(randomIndex, 1);

        }
    }
    return reels;
};


// transpose rows into the slot machine rows
const transpose = (reels) => {
    const rows = [];
    for (let i = 0; i < ROWS; i++){
        rows.push([]);
        for (let j = 0; j < COLS; j++){
            rows[i].push(reels[j][i])
        }
    }
    return rows;
};

const printRows = (rows) => {
    console.clear();
    console.log("$ Slots $")
    console.log("")
    for (const row of rows){
        let rowString = "";
        for (const [i, symbol] of row.entries()){
            rowString += symbol
            if (i != row.length - 1) {
                rowString += " | "
            }
        }
        console.log(rowString)
    }
    console.log("")
    console.log("")
}


// check if user won
const getWinnings = (rows, bet, lines) => {
    let winnings = 0;

    for (let row = 0; row < lines; row++){
        const symbols = rows[row];
        let allSame = true;

        for (const symbol of symbols){
            if (symbol != symbols[0]){
                allSame = false;
                break;
            }
        }

        if (allSame) {
            winnings += bet * SYMBOL_VALUES[symbols[0]]
        }
    }

    return winnings;
}

// print out the winnings
const won = (winnings) => {
    if (winnings === 0){
        console.log("You lost.");
    }else {
    console.log("You won, $" + winnings.toString());
    }
    }


// give the user the winnings
const game = () => {
    let balance = getDeposit();

    while (true) {
    console.clear();
    console.log("");
    console.log("You have a balance of $" + balance);
    console.log("");
    const numbersOfLines = getNumbersOfLines();
    console.clear();
    console.log("");
    console.log("You have a balance of $" + balance);
    console.log("");
    console.log("You are betting on " + numbersOfLines + " lines");
    console.log("");
    const betAmount = getBetAmount(balance, numbersOfLines);
    balance -= betAmount * numbersOfLines;
    const reels = spin();
    const rows = transpose(reels);
    printRows(rows);
    const winnings = getWinnings(rows, betAmount, numbersOfLines);
    balance += winnings;
    won(winnings);
    console.log("");
    console.log("You now have a balance of $" + balance);

    if (balance <= 0) {
        console.log("You ran out of money!");
        console.log("");
        break;
    }

    console.log("");
    const playAgain = prompt("Do you want to play again? (y/n) ")
    if (playAgain != "y") {
        console.clear();
        break;
    }


    }
}

console.clear()
console.log("");
console.log("Welcome to the VIRTUAL SLOT MACHINE");
console.log("");
console.log("Where you can LOSE money without actually losing any money.");
const play = () => {
    console.log("");
    console.log("");
    playGame = prompt("Would you like to play? (y/n) ");
    if (playGame === "y") {
        game();
    } else {
        console.log("");
        console.log("Fine I didnt want to play anyways...");
        console.log("");
        console.log("");
    }
}

play();

// testing logs
// console.log(reels)
// console.log(`${balance}`)
// console.log(`${numbersOfLines}`)
// console.log(`${betAmount}`)