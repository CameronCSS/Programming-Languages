# Chapter 13_7 test

# Extracting Data from JSON

"""

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_2075357.json (Sum ends with 28)
You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
"""

import urllib.request
import json

# Ask user for desired URL
url = input('Enter URL: ')

# print to confirm entered URL
print('Retrieving', url)

# Open url and decode the data for json
opened = urllib.request.urlopen(url)
data = opened.read().decode()

print('Retrieved', len(data), 'characters')
info = json.loads(data)

# Print the count of comments found
print('Count:', len(info['comments']))

# create Total variable to track total sum of all counts
total = 0

# Loop through the data and get all the counts and add it to our running total
for item in info['comments']:
    count = item['count']
    total += count

# Print out the final total
print('Sum:', total)


