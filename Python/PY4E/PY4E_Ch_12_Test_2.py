# Chapter 12 test

# Following Links in Python
"""
In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. 
The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, 
scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Ask user for URL
url = input('Enter: ')

# Handle the URL and open it
html = urllib.request.urlopen(url, context=ctx).read()

# bs4 parses the data and makes it useable by python
soup = BeautifulSoup(html, "html.parser")

# Ask user for the number of times to repeat the process
count = int(input('Enter count: '))

# Ask user for the position of the link to follow
position = int(input('Enter position: '))

# Repeat the process x times
for i in range(count):
    # Parse the HTML content
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Retrieve all of the anchor tags
    tags = soup('a')
    
    # Extract the href attribute of the link at the specified position
    # We use '-1' because python starts at 0. So -1 will give us the actual position we are asking for.
    link = tags[position - 1].get('href', None)
    
    # Print the link being followed
    print(f'Retrieving: {url}')
    
    # Update the current URL to follow the link
    url = urllib.parse.urljoin(url, link)

# Output the final URL after repeating the desired amount
print(f'Retrieving: {url}')



### OUTPUT
"""
Enter: http://py4e-data.dr-chuck.net/known_by_Jordanne.html
Enter count: 7
Enter position: 18
Retrieving: http://py4e-data.dr-chuck.net/known_by_Jordanne.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Marvin.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Yago.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Daood.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Jillian.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Bradly.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Steffie.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Mitchel.html


Answer: Mitchel
"""