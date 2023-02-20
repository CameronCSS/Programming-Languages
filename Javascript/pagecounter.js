var count = 0;
var countSpan = document.getElementById("count");

function updateCounter() {
  count++;
  countSpan.textContent = count;
}

// Call the updateCounter function when the page loads
window.onload = updateCounter;
