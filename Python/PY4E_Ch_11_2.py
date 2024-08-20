import re

filename = 'regex_sum_2075352.txt'

# Error handling if filename doesnt exist or cant be opened
try:
    fh = open(filename)
except:
    print('File cannot be opened:', filename)
    quit()

total_sum = 0

for line in fh:
    # remove extra \n linebreaks
    line = line.rstrip()

    # Protection code to SKIP blank lines
    if line == '':
        continue

    # Find all numbers in the line
    numbers = re.findall('[0-9]+', line)
    
    # Convert numbers to ints and add them all together
    for num in numbers:
        n = int(num)
        total_sum += n

print('Total sum:', total_sum)
