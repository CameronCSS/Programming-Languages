# Chapter 13 test
"""
In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/xml3.py. 
The program will prompt for a URL, read the XML data from that URL using urllib 
and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
"""

import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')

# Default url if nothing is entered
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'


print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//count')

# Initialize the total
total_sum = 0

# loop through data and calculate the total
for count in counts:
    # Convert the count content(text) to integers and add it to the total
    total_sum += int(count.text)

print(f'Count: {len(counts)}')
print(f'Sum: {total_sum}')
