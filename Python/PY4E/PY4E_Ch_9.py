# This is a study guide for PY4E Chapter 9
# Notes and comments have been added for clarity and explaining topics

""" 
List: A linear collection of values where you can lookup their position using a value. pos[1] for example.

Dictionary: A linear collection of key-value pairs where you can lookup the value by using a 'tag' or a 'key' 
"""


# counting names

# create our dictionary
counts = dict()
OR 
counts = {}

# {} is the shortcut nickname for a dictionary.
counts = {}
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:

        # If this is the first time we see the name. Add it to the dictionary AND start counting it
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

# OUTPUT
{'csev': 2, 'cwen': 2, 'zqian': 1}

# Luckily for us dictionaries are so common in python that many METHODS exist to make things even easier for us.
# Instead of writing ALL of teh above code. you can simply call .get()

# Example

counts = {}
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    # Use .get() to get the current count of the name, defaulting to 0 if the name is not found
    count = counts.get(name, 0)
    # Update the count for this name
    counts[name] = count + 1
print(counts)

# OUTPUT
{'csev': 2, 'cwen': 2, 'zqian': 1}



# Counting words

counts = {}
print('Enter a line of text:')
line = input('')

words = line.split()

print('Words:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)

# INPUT
the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car

# OUTPUT
Words: ['the', 'clown', 'ran', 'after', 'the', 'car', 'and', 'the', 'car', 'ran', 'into', 'the', 'tent', 'and', 'the', 'tent', 'fell', 'down', 'on', 'the', 'clown', 'and', 'the', 'car']
Counting...
Counts {'the': 7, 'clown': 2, 'ran': 2, 'after': 1, 'car': 3, 'and': 3, 'into': 1, 'tent': 2, 'fell': 1, 'down': 1, 'on': 1}


# KEY and VALUE lookup
# you can easily call or lookup the key and value of the dictionary.

age = {'chuck' : 24, 'fred' : 40, 'Julio' : 32}

# get all keys
print(list(age.keys()))
# OUTPUT
['chuck', 'fred', 'Julio']

# get all values
print(list(age.values()))
# OUTPUT
[24, 40, 32]


# You can also return a tuple using .items()
print(age.items())
# OUTPUT
dict_items([('chuck', 24), ('fred', 40), ('Julio', 32)])

# NOTE: Tuples are covered more in the next chapter




# counting big words

filename = input('Enter file:')
handle = open(filename)

# initialize our count dict
counts = {}
for line in handle:
    # split lines into individual words
    words = line.split()

    # for every word in the loop add onto our count
    for word in words:
        counts[word] = counts.get(word,0) + 1

# create our variables to track the word and count
bigcount = None
bigword = None

# loop through the dictionary by making it a list
for word,count in counts.items():

    # If the current pair (word, Count) is bigger than change the big word and count to the new values
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

# After everything has ran print out the biggest word and the count of that word.
print(bigword, bigcount)
