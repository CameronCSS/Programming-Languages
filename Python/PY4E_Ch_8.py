# This is a study guide for PY4E Chapter 8
# Notes and comments have been added for clarity and explaining topics

------

# Calculating Sum with lists instead of loops

# OLD METHOD using loops learned from earlier chapters
total = 0
count = 0

while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    total += value
    count += 1

average = total / count
print('Average:', average)

------

# NEW METHOD USING LISTS

# Create an empty list called numlist
# You can also use numlist = list(). but the standard method most programmers use is numlist = []
numlist = []

while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)

    # append / add our value into the list
    # Unless you speicify. appending will default adding to the end of the list
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)

# NOTE: Using loops will only store the one value for the number.  Using lists will store every single number before doing any calculation.
# This wont really matter until you start working with millions of numers and then memory usage can be a problem.

------

# Split breaks a string into parts and produces a list of strings. We think of these as words. We can access a particular word or loop through all the words.

# Example

# DATA
abc = 'With three words'
stuff = abc.split()

# COMMAND
print(stuff)

# OUTPUT
['With', 'three', 'words']

# COMMAND
print(len(stuff))

# OUTPUT
3

# COMMAND
print(stuff[0])

# OUTPUT
With


# COMMAND
for word in stuff:
        print(word)

# OUTPUT
With
three
words

------

# Split treats all white space the same. so whether there is a single space or 100. it will get rid of them all

# Example
line = 'A lot               of          spaces'
split_line = line.split()
print(split_line)

# OUTPUT
['A', 'lot', 'of', 'spaces']

---

# you can split by a specific delimiter. By default split looks for spaces.

# Example
line = 'first;second;third'

# incorrect use trying to use regular split
split_line = line.split()
print(split_line)

# incorrect output
['first;second;third']

--

# CORRECTED USE ( With specific delimiter)
split_line = line.split(';')
print(split_line)

# CORRECTED OUTPUT ( With specific delimiter)
['first', 'second', 'third']



# Example using split to split email data
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
print(words)

# Example output after .split() SPLITS the data between each space.
['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16' , '2008']

--

# In an earlier chapter we tried to extract the host name from an email using a loop
# now we can do it easier and with less lines of code by using split

line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])

# OUTPUT
uct.ac.za

--

