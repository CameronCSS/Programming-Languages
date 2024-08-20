# This is a study guide to go along with Chapter 7 of PY4E
# Comments are added to help explain various ideas.
-----

# Searching through a file

# assign a name to our file handler
varname = open ('file_name.txt')

# Search through the file for any line that starts with 'From:'
# For loop will go through the whole file line by line and we can do whatever we want with that data
for line in varname:
    if line.startswith('From:'):
        print(line)


# Output example
From: stephen.marquard@uct.ac.za \n
\n
From: louis@media.berkeley.edu \n
\n
From: zqian@umich.edu \n
\n
From: rjlowe@iupui.edu \n
\n

-- One \n is from the file. and one \n is from the print statement


------------

# If you want the data readout without the blank line whitespaces "\n" added from the original file you can do this
for line in varname:
    # rstrip strips white space from the right so we dont get additional line breaks '\n'
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

# Output example
From: stephen.marquard@uct.ac.za
From: louis@media.berkeley.edu
From: zqian@umich.edu
From: rjlowe@iupui.edu


------------

# You can reverse your IF logic and get the exact same results.
# You may want to do this to make things easier to understand depending on what you are trying to do
# The output is the same either way.

for line in varname:
    # rstrip strips white space from the right so we dont get additional line breaks '\n'
    line = line.rstrip()
    if not line.startswith('From:'):
        # Continue means if this line does NOT start with 'From:' restart the loop
        continue
    # If the line does start with From: instead of continuing back to the start of the loop it first prints and then the loop is continued.
    print(line)

# Output example
From: stephen.marquard@uct.ac.za
From: louis@media.berkeley.edu
From: zqian@umich.edu
From: rjlowe@iupui.edu


------------

# You can also look for a string anywhere IN the line

for line in varname:
    # rstrip strips white space from the right so we dont get additional line breaks '\n'
    line = line.rstrip()
    if '@uct.ac.za' in line:
        print(line)

# Output example
From: stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
X-Authentication-warning: set sender to stephen.marquard@uct.ac.za using -f
From: stephen.marquard@uct.ac.za
From: david.horwitz@uct.ac.za Fri Jan 4 07:02:32 2008
X-Authentication-warning: set sender to david.horwitz@uct.ac.za using -f

------------

# Its a good idea to build error handling into your code.
# Best practice is to always include some type of error handling to avoid issues with your program.
# You cant account for every error. But get in the habit of handling the most common errors. Like when someone wants to open a file and they typed the name wrong.

# Example of error handling

filename = input('Enter the file name: ')

# This will try to open the file. if it cant open it will give the error and close.
try:
    file_handler = open(filename)
except:
    print('File cannot be opened:', filename)
    quit()

# if the file is opened the code continues
count = 0

for line in file_handler:
    # count Subject lines
    if line.startswith('Subject:'):
        # This line adds one to the count
        count = count + 1
        # An easier way to write this line is 'count += 1'  But for now we can leave it in common language that is easier to understand.

    print('There are', count, 'subject lines in', filename)
