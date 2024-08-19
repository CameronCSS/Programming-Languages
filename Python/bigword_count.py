# counting big words

filename = input('Enter file:')

try:
    handle = open(filename)
except:
    print("filename doesnt exist")
    quit()

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
