# This is a study guide for PY4E Chapter 10
# Notes and comments have been added for clarity and explaining topics

# tuples
"""
Tuples are another kind of sequence that functions much like a list.
Tuples have elements which are indexed starting at 0

Unlike a list, once you create a tuple, you cannot alter its contents. Just like a string, it is immutable.

You cannot sort a tuple. Whatever order it is when you create it is the order it stays in. 

You cant flip it or append or do anything with the tuple that changes it.

a Tuple is a simpler and more efficent version of a list because it uses less memory and is more performant since it is immutable.
"""


# you can use tuples to assign multiple variables at once

# Example
(x,y) = (4, 'fred')
print(y)
# OUTPUT
fred


(a,b) = (99, 98)
print(a)
# OUTPUT
99


"""
Comparison operators work with tuples and other sequences. If the first item is equal, Python goes on to the next element, and so on. Until if finds something that differs.
On the other hand, if the first items compared are less than / greater than it assumes the entire tuple is also less than / greater than.
"""

# Example
(0,1,2) < (5,1,2)
True

(0,1,20000) < (0,3,4)
True


# sorting lists of tuples

# We can take advantage of the ability to sort a list of tuples to get a sorted version of a dictionary.

'Rememebr you cant sort anyhting inside a tuple. But you CAN sort a list of tuples'

# Example
'First we sort the dictionary by the key using the items() method and sorted() function'

d = {'a':10, 'c':22, 'b':1}
d.items()
# OUTPUT
-- dict_items([('a', 10), ('c', 22), ('b', 1)])

sorted(d.items())
# OUTPUT
[('a', 10), ('b', 1), ('c', 22)]

' "sorted(d.items())"  is the quickest way to sort by KEY'

'Sorting by Values is a little trickier, but still doable'

# Example
c = {'a':10, 'b':1, 'c':22}
tmp = list()

# Itterate through and FLIP the values to the key
for k, v in c.items():
    tmp.append( (v,k))
print(tmp)
# OUTPUT
[(10, 'a'), (1, 'b'), (22, 'c')]

tmp = sorted(tmp, reverse=True)
print(tmp)
# OUTPUT
[(22, 'c'), (10, 'a'), (1, 'b')]

'Now we are sorted by values in Desc order.  Dont use reverse if you want it to be ascendiang'

----

# Sorting top 10 words in Descending order

# set our filename
fhand = open('romeo.txt')

# initilize our dict
counts = {}

# iterate through each line and split into individual words
for line in fhand:
    words = line.split()

    # for each word check if it exists and add it to count, and increase count on each loop by 1
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# initialize our list
lst = []

# create a list of tuples with reverse key value mapping
for key, val in counts.items():
    newtup = (val,key)
    lst.append(newtup)

# once we have our list of tuples with values and keys flipped we can sort in DESC order
lst = sorted(lst, reverse=True)

# iterate through the Top 10 key value pairs 
for val, key in lst[:10]:
    # print them so key and value are in the correct order
    # we could build a whole new tuple with correct key value pairing now that we have it. but for now we just print
    print(key,val)



# We can do the about (flipping tupple key value pairs and sorting) all in one line of code using List comprehension
'List comprehension creates a dynamic list. In this case, we make a list of reversed tuples and then sort it'

# Example 
c = {'a':10, 'b':1, 'c':22}
print( sorted( [(v,k) for k,v in c.items()],reverse=True))

# OUTPUT
[(22, 'c'), (10, 'a'), (1, 'b')]
