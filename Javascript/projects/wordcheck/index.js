const input = document.getElementById("input")

function reverseString(str){
    "hello"
    return str.split("").reverse().join("")
}

function check(){
    const value = input.value;
    const reverse = reverseString(value)
    
    if (value === reverse) {
        alert(`${value} is a PALINDROME!!`);
    }
    else {
        alert(`${value} is NOT a Palindrome`);
    }

    input.value = ""

}