// This code creates a search bar to search through a Podcast episode list for keywords

// This code was created specifically to work on Carrd.co website as an alternative Search function since they do not have one,
// but it should work anywhere you can run Javascript

// The base of the code is setup to run as HTML so it works inside the <EMBED> container on Carrd

// This Code is to be used in Conjuction with the Episode_list.js RSS pull that I also have available in this repository. 
// The Search results are sifting through that episode list that is created by the other JS code

<div id="search"></div>  <!-- Creates an empty div with an id of "search" -->

<style>
  .highlight {
    background-color: yellow;  // Defines a CSS class for highlighting text
  }

  .search-container {
    display: flex;  // Defines a CSS class for the container with flexible layout
    align-items: right;  // Aligns flex items along the right edge of the container 
  }

  #search-input {
    width: 300px;
    height: 30px;
    margin-left: 10px;  // Styles the search input with CSS 
  }

  #search-no-results {
    display: none;  // Hides the "No results found" message by default
    margin-top: 10px;
    font-style: italic;
    color: pink;
  }

  #search-results-count {
    display: none;  // Hides the search results count by default
    margin-top: 10px;
    font-style: italic;
    color: pink;
  }
</style>

<input type="text" id="search-input" placeholder="Enter Keywords...">  <!-- Creates default words shown in the search bar -->

<div id="search-no-results">No results found.</div>  <!-- Displays a message when there are no search results -->

<div id="search-results-count"></div>  <!-- Displays the number of search results found -->

<script>
const searchInput = document.getElementById('search-input'); // Get the search input element by ID
const noResultsMessage = document.getElementById('search-no-results'); // Get the "no results" message element by ID
const resultsCountMessage = document.getElementById('search-results-count'); // Get the results count message element by ID

// Add an event listener to the search input for whenever the input changes
searchInput.addEventListener('input', () => {
  const query = searchInput.value.toLowerCase(); // Get the current search query, and convert to lowercase
  const posts = document.querySelectorAll('.rss-post'); // Get all elements with the class "rss-post"
  let resultsCount = 0; // Initialize the count of search results to 0

  // Loop through each "rss-post" element
  posts.forEach(post => {
    const title = post.querySelector('h3 a').textContent.toLowerCase(); // Get the lowercase text content of the "rss-post" title
    const summary = post.querySelector('.post-summary').textContent.toLowerCase(); // Get the lowercase text content of the "rss-post" summary

    // If the title or summary includes the search query, highlight the matching text and display the post element. Otherwise, hide the post element.
    if (title.includes(query) || summary.includes(query)) {
      post.style.display = 'block'; // Show the post element
      post.querySelector('h3 a').innerHTML = highlightQuery(title, query); // Highlight the matching text in the title
      post.querySelector('.post-summary').innerHTML = highlightQuery(summary, query); // Highlight the matching text in the summary
      resultsCount++; // Increment the count of search results
    } else {
      post.style.display = 'none'; // Hide the post element
    }
  });

  // If the search query is empty, hide both the "no results" message and the results count message. Otherwise, if no results were found, display the "no results" message and hide the results count message. Otherwise, display the results count message with the number of results found.
  if (query === '') {
    noResultsMessage.style.display = 'none';
    resultsCountMessage.style.display = 'none';
  } else if (resultsCount === 0) {
    noResultsMessage.style.display = 'block';
    resultsCountMessage.style.display = 'none';
  } else {
    noResultsMessage.style.display = 'none';
    resultsCountMessage.style.display = 'block';
    resultsCountMessage.textContent = resultsCount + ' result(s) found';
  }
});

// Add an event listener to the search input for when it loses focus
searchInput.addEventListener('blur', () => {
  if (searchInput.value === '') {
    resultsCountMessage.style.display = 'none'; // If the search input is empty, hide the results count
  }
});

// Function to highlight the search query in a block of text
const highlightQuery = (text, query) => {
  const pattern = new RegExp(`(${query})`, 'gi'); // Create a regular expression pattern to match the search query (with the 'g' flag to match all occurrences, and the 'i' flag to ignore case)
  return text.replace(pattern, '<span class="highlight">$1</span>'); // Replace all occurrences of the search query with the query wrapped in a span element with the class "highlight"
};
</script>

