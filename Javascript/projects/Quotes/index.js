const quotes = [
    "Your time is limited, don't waste it living someone else's life.",
    "The best way to predict the future is to create it.",
    "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful.",
    "The only limit to our realization of tomorrow will be our doubts of today.",
    "Believe you can and you're halfway there.",
    "The greatest glory in living lies not in never falling, but in rising every time we fall.",
    "It is never too late to be what you might have been.",
    "Happiness is not something ready-made. It comes from your own actions.",
    "In the middle of difficulty lies opportunity.",
    "Dream big and dare to fail.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "The only way to do great work is to love what you do.",
    "Life is what happens when you're busy making other plans.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "It does not matter how slowly you go as long as you do not stop.",
    "In the end, it's not the years in your life that count. It's the life in your years.",
    "The purpose of our lives is to be happy.",
    "Get busy living or get busy dying.",
    "You only live once, but if you do it right, once is enough.",
    "Many of life's failures are people who did not realize how close they were to success when they gave up.",
    "If you want to live a happy life, tie it to a goal, not to people or things.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "The only limit to our realization of tomorrow will be our doubts of today.",
    "Don't watch the clock; do what it does. Keep going.",
    "The way to get started is to quit talking and begin doing.",
];


const usedIndexes = new Set()
const quoteElement = document.getElementById("quote")


function generateQuote(){
    if (usedIndexes.size >= quotes.length){
        usedIndexes.clear()
    }

    while (true) {
    const randomIdx = Math.floor(Math.random() * quotes.length)

    if (usedIndexes.has(randomIdx)) {
        continue
    }

    const quote = quotes[randomIdx]
    quoteElement.innerHTML = quote
    usedIndexes.add(randomIdx)
    break
}
}