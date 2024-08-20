# Test Prompt

"""
8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

-- NOTE: The mbox-short.txt I used was altered with additional errors that needed to be correct for.
This code will still work with the py4e mbox-short.txt. But the additional protections are from the Bonus use cases discussed after the chapter.
"""

# code already given to us in the test
fname = input("Enter file name: ")

# Error handling in case file doesnt exist or name is typed wrong
try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0

for line in fh:
    # remove extra \n linebreaks
    line = line.rstrip()

    # Protection code to SKIP blank lines
    if line == '':
        continue

    # before doing anything check if line is the one we want
    if not line.startswith("From "):
        continue

    # split the line into words
    words = line.split()

    # Protection from fake lines that have From, but no actual email
    if len(words) < 3:
        continue
    
    # if the line DID start with From and was not a fake line, then add to the running count
    count += 1

    # extract the current lines email
    email = words[1]

    # print out that lines email and the loop will then start again
    print(email)

# After the loop has gone through every email print the final count
print("There were", count, "lines in the file with From as the first word")

