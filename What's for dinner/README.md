<a name="readme-top"></a>


  <img src="https://github.com/user-attachments/assets/ecd003f9-942c-48a2-b701-f0434e8bfb0a" alt="Whats4dinnerlogo" height="200">

#### [Video Demo](<https://www.youtube.com/watch?v=OztMCgm2H9A>)


> [!IMPORTANT]
> This is my CS50 certification Final Project

## Overview

We’ve all faced the age-old question: *"What's for dinner?"* Every single day we have to check the fridge, check your pantry, decide what we want, and finally make a shopping list because we realize there's no food in the house. 

**Then after all that you still have to go and actually SHOP. UGHH!!**

----

### My Solution

**What's 4 Dinner** is a web app designed to simplify both meal planning and shopping:

- **Random Recipe Selector**: When you can't decide what to cook, let the app pick recipes for you.

  <img src="https://github.com/user-attachments/assets/cadc881b-867c-4a0a-93df-9524917659c9" alt="randomrecipe" height="400">

- **Streamlined Shopping**: Map your store's aisles once, and your shopping list will be automatically sorted for a easier shopping experience.

  <img src="https://github.com/user-attachments/assets/31f161d0-17e4-491d-b52f-8517c5f23dd3" alt="aisletracker" height="200">


#### Why Manual Aisle Mapping?

I considered using local data and scraping store websites to auto-update aisle information. However, this made the entire project much more complicated and was in all sorts of grey areas since I needed to get your local data (zip code) AND scrape data from big companies that do not like you scraping anything from their websites.

## Features

- **Ingredient Tracker**: Keep track of what you have at home. Ingredients are auto-deleted after 7 days, so no need for manual removal.
- **Favorite Recipes**: Save and manage your favorite recipes.
- **Recipe Sorted by What you have**: Find recipes based on the ingredients you have on hand.
- **Recipe Rotation**: Sort recipes by the last time you shopped for them to avoid repeating meals too often.
- **Random Recipe Generator**: Get 5 random recipes and a shopping list that excludes ingredients you already have.
- **Shopping List Quick Add**: Easily add items to your shopping list and receive a warning if you already have them on hand.
- **Custom Ingredients & Recipes**: Add your own ingredients and recipes. The app includes about 50 recipes and hundreds of ingredients.
- **Saved Shopping Lists**: Save and reuse shopping lists for future trips. The app will update your list based on what ingredients you have on hand.
- **Store-Specific Aisle Mapping**: Add and track multiple stores' aisles, specific to your shopping habits.

<sup>Example from recipe page</sup>
  <img src="https://github.com/user-attachments/assets/096abdf7-b495-4fd2-a669-f9cd65d95f01" alt="onhandingredients" height="400">
  <br>
---- 

## Future Wants

- **Automated Aisle Information**: Ideally, auto-add aisle details from chosen stores (though this is currently a low priority).
- **Barcode Scanning**: Scan items to quickly update your 'On Hand' inventory.
- **Recipe Inventory**: View recipes based on ingredients you’ve purchased, for convenience.
- **Aisle Sorting**: Add the ability to sort by aisle numbers, based on store layout.
- **Recipe Search**: Improve the search functionality for easier recipe discovery.
- **Enhanced Design**: Update the app’s visual elements for a more appealing look.
- **Usage Statistics**: Add a page to view your most frequently shopped recipes and ingredients.
- **Expiration Dates**: Optionally track ingredient expiration dates and set reminders (currently considered overkill).

## Technical Details

- **Languages Used**: Python (~1300 lines), JavaScript (~500 lines), HTML (~400 lines), SQL (~50 lines).
- **Database**: Local SQLite database with 13 tables to manage user data and app information.
- **Frameworks & Libraries**: Flask is the main python Framework doing most of the interaction and heavy lifting (besides straight code)
- **Development Time**: I've spend over 100 hours programming it. To be fair, a lot of the early days where when I was lost and had NO idea what I was doing. Even now it could probably use a fresh start since its very messy and not well optimized. 

---

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a href="https://github.com/CameronCSS/Programming-Languages/blob/main/README.md"><strong>« Back to Python Projects</strong></a>
<br>
<br>
<a href="https://github.com/CameronCSS/PersonalProjects/blob/main/README.md"><strong>« Back to Portfolio</strong></a>

## <a href="https://camdoesdata.com/#contact">Contact Me</a>
  <p style="margin-left: auto;">
    <a href="https://drive.google.com/file/d/1YaM4hDtt2-79ShBVTN06Y3BU79LvFw6J/view?usp=sharing" target="_blank" rel="noopener noreferrer">
      <img src="https://user-images.githubusercontent.com/121735588/215364205-abdfc0ac-53db-4733-8d43-b57c1bafb802.png" alt="Resume button">
    </a>
  </p>
</div>
