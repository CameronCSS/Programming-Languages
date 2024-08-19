# Test Prompt

"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""

# ask user for filename
name = input("Enter file:")

# give default value if no filename is entered
if len(name) < 1:
    name = "mbox-short.txt"

# error handling if filename doesnt exist or cant be loaded
try:
    handle = open(name)

except:
    print("file could not be opened")
    quit()

# create our empty dict for adding and counting the emails
counts = {}

# iterate through the data and separate each line
for line in handle:
    # remove extra \n linebreak
    line = line.rstrip()

    # Make sure its a FROM email line
    if not line.startswith('From '):
        continue

    # split email into individual words
    words = line.split()

    # sift out lines that start with from but arent actual From email lines
    if len(words) < 3:
        continue

    # get all the datetime 09:15:20, etc.
    datetime = words[5]

    # Split the time by the : so we can get to the hour
    time = datetime.split(':')
    hour = time[0]

    # if that hour not in counts then add it and start counting
    if hour not in counts:
        counts[hour] = 1

    # add 1 every time that hour appears again
    else:
        counts[hour] = counts.get(hour,0) + 1

# sort the dictionary by hour and print the results
for hour in sorted(counts):
    print(hour, counts[hour])
