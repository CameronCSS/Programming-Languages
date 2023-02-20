var count = 0;
  var countSpan = document.getElementById("count");

  function updateCounter() {
    count++;
    countSpan.textContent = count;
  }

  // Call the updateCounter function when the page loads
  window.onload = updateCounter;

  // Call the updateCounter function when the DOM is ready
  document.addEventListener("DOMContentLoaded", function() {
    updateCounter();
  });
