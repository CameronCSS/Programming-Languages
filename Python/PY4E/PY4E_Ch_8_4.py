# Test Prompt

"""
8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.
You can download the sample data at http://www.py4e.com/code3/romeo.txt
"""

# some code already given to us in the test
fname = input("Enter file name: ")

# Error handling in case file doesnt exist or name is typed wrong
try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

# Create our list we are going to put the words into
lst = []

# Read each line of the file
for line in fh:
    # remove the extra \n linebreak
    line = line.rstrip()

    # split the line into individual words
    words = line.split()

    # loop through each individual word
    for word in words:

        # if the word is not already in the list, then append it to the end of the list
        if word not in lst:
            lst.append(word)

            # contiue will loop back through and check the next word
            continue

# Sort the final list. Sorting string will automatically do it alphabetically.
lst.sort()

# print out the sorted list
print(lst)


