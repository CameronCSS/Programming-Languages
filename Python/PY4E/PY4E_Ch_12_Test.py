# Chapter 12 test
"""
Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. 
The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

# Ask user for URL
url = input('Enter - ')

# Handle the URL and open it
html = urlopen(url).read()

# bs4 parses the data and makes it useable by python
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of span tags
tags = soup('span')

numbers = []
total = 0
for tag in tags:

    # Grab the content from the Span elements
    numbers.append(tag.contents[0])

# mapping our list to a list of integers instead of strings
numbers = list(map(int, numbers))

# sum all the numbers
total = sum(numbers)
print(total)
