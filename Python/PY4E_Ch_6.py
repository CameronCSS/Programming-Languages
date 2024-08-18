# This is extremely simple string manipluation. 
# I wanted to add comments that can hopefully help anyone new to learning python for the first time.

# Base code provided in the chapter
text = "X-DSPAM-Confidence:    0.8475"

# Find the ':' so we can create our float number from that point
colon = text.find(':')

# start from the : and add 1 so we start at the position directly AFTER the colon
# the second number is the position we end on. So we go to 30 position (Which is actually beyond the string. so this will just go to the end)
string = text[colon + 1: 30]

# Create the float from our string we just created.  
# Float automatically gets rid of white space so we dont need to trim anything
number = float(string)

# print out the final float number
print(number)
