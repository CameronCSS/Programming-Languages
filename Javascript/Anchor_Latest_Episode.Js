// This code gets the Most Recent Episode details from an Anchor RSS feed for a Podcast

// This code was created specifically to work on Carrd.co website as an alternative to buying fancy plugins that cost a premium per month and cant be customized

// The base of the code is setup to run as HTML so it works inside the <EMBED> container on Carrd

// We are using "loadRssFeed1" because later on the Carrd page we created similar code to get a full episode list from the Podcast.
// You can find the 'EpisodeList' script in this Repo as well

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

// Create a New Div for the latest episode container

<div id="rsslatest"></div>
// This script section loads and displays the RSS feed

<script>
function loadRssFeed1() {
// URL of the RSS feed to be loaded
const rssUrl = 'https://anchor.fm/s/YOUR_ANCHOR_ID/podcast/rss';
const parser = new DOMParser();

// Fetch the RSS feed data from the URL
fetch(rssUrl)
.then(response => response.text())
.then(data => {
// Parse the XML data of the RSS feed
const xml = parser.parseFromString(data, 'application/xml');
// Find all the RSS items
const items = xml.querySelectorAll('item');

// Find the latest RSS item by comparing their publication dates
let latestItem = null;
items.forEach(item => {
if (!latestItem || new Date(item.querySelector('pubDate').textContent) > new Date(latestItem.querySelector('pubDate').textContent)) {
latestItem = item;
}
});

// If a latest item is found, create the HTML elements to display it
if (latestItem) {
const title = latestItem.querySelector('title').textContent;
const description = latestItem.querySelector('description').textContent.trim().replace(/<\/?p>/g,'').replace(/<\/?br>/g,'').replace(/&nbsp;/g, ' ');
const link = latestItem.querySelector('link').textContent;
// Create a new div element
const post = document.createElement('div');
// Set the class of the new div element to 'rss-post2'
post.className = 'rss-post2';

// Create a new img element
const img = document.createElement('img');
// Find the itunes:image element in the latestItem element and set the 'src' attribute of the img element to its 'href' attribute if it exists
// Otherwise, set the 'src' attribute of the img element to a default image URL
const itunesImage = latestItem.querySelector('itunes\\:image');
if (itunesImage) {
    img.src = itunesImage.getAttribute('href');
} else {
    img.src = 'YOUR_DEFAULT_IMAGE_URL';
}

// Create a new div element
const postDetails = document.createElement('div');
// Set the class of the new div element to 'post-details2'
postDetails.className = 'post-details2';

// Create a new h3 element for the post title
const postTitle = document.createElement('h3');
// Create a new a element for the post title link and set its 'href' attribute to the link of the latestItem element
const postTitleLink = document.createElement('a');
postTitleLink.href = link;
// Set the text content of the postTitleLink element to the title of the latestItem element
postTitleLink.textContent = title;
// Append the postTitleLink element to the postTitle element
postTitle.appendChild(postTitleLink);

// Create a new div element for the post date
const postDate = document.createElement('div');
// Set the class of the new div element to 'date'
postDate.className = 'date';
// Set the text content of the new div element to the date of the latestItem element
postDate.textContent = new Date(latestItem.querySelector('pubDate').textContent).toLocaleDateString();

// Create a new div element for the post summary
const postSummary = document.createElement('div');
// Set the class of the new div element to 'post-summary2'
postSummary.className = 'post-summary2';
// Set the inner HTML of the new div element to the description of the latestItem element
postSummary.innerHTML = description;

// Create a new div element for the audio player container
const audioContainer = document.createElement('div');
// Set the ID of the new div element to 'audio-container'
audioContainer.id = 'audio-container';

// Create a new audio element for the audio player
const audioPlayer = document.createElement('audio');

// Create a new source element for the audio file and set its type and URL
const audioSource = document.createElement('source');
audioSource.id = 'audio-source';
audioSource.type = 'audio/mpeg';
const audioFileUrl = latestItem.querySelector('enclosure').getAttribute('url');
audioSource.setAttribute('src', audioFileUrl);

// Append the source element to the audio player and the player to the container
audioPlayer.appendChild(audioSource);
audioContainer.appendChild(audioPlayer);

// Append the title, date, summary, and audio container to the post details
postDetails.appendChild(postTitle);
postDetails.appendChild(postDate);
postDetails.appendChild(postSummary);
postDetails.appendChild(audioContainer);

// Append the image and post details to the post
post.appendChild(img);
post.appendChild(postDetails);

// Append the post to the #rsslatest element in the HTML
document.querySelector('#rsslatest').appendChild(post);

// Call the loadRssFeed1 function to load the RSS feed
loadRssFeed1();
</script>
