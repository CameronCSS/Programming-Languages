# Test Prompt

"""
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""

# ask user for filename input
filename = input('Enter a filename')

# if filename not given give it a default value
if len(filename) < 1:
    # default value to file to open
    filename = 'mbox-short.txt'

# Even with default value. Built in error handling just in case file cant be opened.
try:
    fh = open(filename)
except:
    print("Couldn't open file")
    quit()

# create our empty dict for adding and counting the emails
counts = {}

# iterate through each line looking for the From lines
for line in fh:

    # remove the extra \n linebreak
    line = line.rstrip()

    # restart loop if it doesnt start with From
    if not line.startswith('From '):
        continue

    # Split line into individual words
    words = line.split()

    # Filter out lines that dont actually have emails
    if len(words) < 3:
        continue

    # email is the second word on the line. So set the email to that word.
    email = words[1]

    # if that email is not in counts, add it and set count to 1
    if email not in counts:
        counts[email] = 1

    # if email is in the counts, just add one to it.
    else:
        counts[email] = counts.get(email, 0) + 1
        
    # set our count variables
    topEmail = None
    topCount = None

    # iterate through the dictionary looking for the highest count
    for email,count in counts.items():

        # if the list is just being started OR if the current email selected has a higher count. Then set current email as the highestEmail with the current count
        if topCount is None or count > topCount:
            topEmail = email
            topCount = count

# after iterating through the whole dictionary print out the highestEmail and the count of emails from them.
print(topEmail, topCount)
