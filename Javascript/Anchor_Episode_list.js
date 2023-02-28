// This code creates an Episode list from an Anchor RSS feed for a Podcast

// This code was created specifically to work on Carrd.co website as an alternative to buying fancy plugins that cost a premium per month and cant be customized

// The base of the code is setup to run as HTML so it works inside the <EMBED> container on Carrd

// We are using "loadRssFeed2" because earlier on the Carrd page we created similar code to get our latest Episode from the Podcast.
// YOU CAN FIND THE 'LATEST EPISODE' script in this Repo as well

// This Code is to be used in Conjuction with the Searchbar.js that I also have available in this repository. 
// The Search bar sifts through the results of this 'Episode list' so you cant quickly find what you are looking for since this code returns every episode avaialable 

// Feel free to adjust the CSS Styling of this code to your needs. Be Careful adjusting the <Script> part of this code to retain its functionality.

<style>
// Using HTML elements so we can embed this on Carrd

// Importing our font from Google Fonts
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

// Styling for the body element
body {
  font-family: 'Roboto', sans-serif;
}

// Styling for the RSS posts
.rss-post {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  padding: 20px;
  margin-bottom: 20px;
  width: 100%;
  word-break: break-word;
  color: white;
  background-color: #070708C9;
}

// Styling for the links within the RSS posts
.rss-post a {
  text-decoration: none;
}

// Styling for the title
.rss-post h3 {
  font-size: 40px;
  color: pink;
  margin-bottom: 10px;
  margin-top: 0;
  text-align: center;
}

// Styling for the date
.rss-post .date {
  font-size: 24px;
  color: #fff;
  margin-top: 0;
  margin-bottom: 10px;
  text-align: right;
}

// Styling for the image
.rss-post img {
  width: 40%;
  object-fit: cover;
  opacity: 0.8;
  margin-right: 20px;
}

// Styling for the post
.post-details {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}

// Styling for the post
.post-summary {
  font-size: 20px;
  line-height: 1.4;
  color: #A0A0A0;
  margin-bottom: 40px;
}

// Media query for screens with max-width 640px (mobile devices) 
@media screen and (max-width: 640px) {
  // Styling for the RSS posts on mobile devices
  .rss-post {
    flex-direction: column;
    align-items: center;
  }

  // Styling for the image on mobile devices 
  .rss-post img {
    width: 100%;
    margin-right: 0;
    margin-bottom: 10px;
  }

  // Styling for the date on mobile devices 
  .rss-post .date {
    text-align: right;
    margin-bottom: 15px;
    margin-top: 5px;
    font-size: 20px;
    color: #fff;
  }

  // Styling for the title on mobile devices 
  .rss-post h3 {
    font-size: 28px;
    text-align: center;
    margin-top: 0;
    margin-bottom: 10px;
  }

  // Styling for the post on mobile devices 
  .post-summary {
    font-size: 16px;
    line-height: 1.4;
    color: #A0A0A0;
    margin-bottom: 40px;
  }
}
</style>


// Create a div element with the id "rss"

<div id="rss"></div>
// Create a function named "loadRssFeed2"
// We are using "loadRssFeed2" because earlier on the Carrd page we used an Initial loadRssFeed to get our latest Episode from the Podcast.
function loadRssFeed2() {

// Assign the RSS feed URL to a variable named "rssUrl"
const rssUrl = 'https://anchor.fm/s/YOUR_ANCHOR_ID/podcast/rss';

// Create a new DOMParser object named "parser"
const parser = new DOMParser();

// Fetch the data from the RSS feed URL
fetch(rssUrl)
.then(response => response.text())
.then(data => { // Parse the data as an XML document and assign it to a variable named "xml"
const xml = parser.parseFromString(data, 'application/xml');

// Select all items from the XML document and assign them to a variable named "items"
const items = xml.querySelectorAll('item');

// Loop through each item in the "items" array
items.forEach(item => {
  
  // Get the title, description, and link from the current item
  const title = item.querySelector('title').textContent;
  const description = item.querySelector('description').textContent.trim().replace(/<\/?p>/g,'').replace(/<\/?br>/g,'').replace(/&nbsp;/g, ' ');
  const link = item.querySelector('link').textContent;
  
  // Create a new div element with the class "rss-post"
  const post = document.createElement('div');
  post.className = 'rss-post';
  
  // Create a new img element with the class "rss-image"
  const img = document.createElement('img');
  
  // Check if the item has an "itunes:image" element and get the image URL if it does
  if (item.querySelector('itunes\\:image')) {
    img.src = item.querySelector('itunes\\:image').getAttribute('href');
  } 
  // Otherwise, use a default image URL
  else {
    img.src = 'YOUR_DEFAULT_IMAGE_URL';
  }
  
  // Create a new div element with the class "post-details"
  const postDetails = document.createElement('div');
  postDetails.className = 'post-details';
  
  // Create a new h3 element and a new a element with the title and link, respectively
  const postTitle = document.createElement('h3');
  const postTitleLink = document.createElement('a');
  postTitleLink.href = link;
  postTitleLink.textContent = title;
  postTitle.appendChild(postTitleLink);
  
  // Create a new div element with the class "date" and the date of the item
  const postDate = document.createElement('div');
  postDate.className = 'date';
  postDate.textContent = new Date(item.querySelector('pubDate').textContent).toLocaleDateString();
  
  // Create a new div element with the class "post-summary" and the description of the item
  const postSummary = document.createElement('div');
  postSummary.className = 'post-summary';
  postSummary.innerHTML = description;
  
  // Create a new div element with the id "audio-container"
  const audioContainer = document.createElement('div');
  audioContainer.id = 'audio-container';
  
  // Create a new audio element with the controls attribute and the id "audio-player"
  const audioPlayer = document.createElement('audio');
  audioPlayer.controls = true;
  audioPlayer.id = 'audio-player';
  
  // create a new HTML element for the audio source
  const audioSource = document.createElement('source');
  audioSource.id = 'audio-source';
  audioSource.type = 'audio/mpeg';

  // get the URL of the audio file from the RSS feed
  const audioFileUrl = item.querySelector('enclosure').getAttribute('url');

  // set the source attribute of the audio element to the URL of the audio file
  audioSource.setAttribute('src', audioFileUrl);

  // append the audio source to the audio player element
  audioPlayer.appendChild(audioSource);

  // append the audio player to the audio container element
  audioContainer.appendChild(audioPlayer);

  // append the post details elements to the post details container element
  postDetails.appendChild(postTitle);
  postDetails.appendChild(postDate);
  postDetails.appendChild(postSummary);
  postDetails.appendChild(audioContainer);

  // append the image and post details container elements to the post element
  post.appendChild(img);
  post.appendChild(postDetails);

  // append the post element to the RSS container element on the page
  document.querySelector('#rss').appendChild(post);
  });
  })
  .catch(error => console.error(error));

  // call the function to load the RSS feed when the page is loaded
  loadRssFeed2();
  </script>
