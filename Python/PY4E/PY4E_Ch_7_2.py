# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")

# Error handling in case file doesnt exist or name is typed wrong
try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0
total = 0.0


for line in fh:

    # before doing anything check if line is the one we want
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    # If we find a line, add to our count
    count += 1

    # Similar to chapter 6 code. We want to extract the number from the string.

    # start at the colon
    colon = line.find(':')

    # starting from the spot after the colon and to the end of the line.
    string = line[colon + 1:]

    # Float automatically trims the whitespace 
    number = float(string)

    # Once we have our float, add to our running total
    total += number


# Calculate the Average
# Check we found any lines of Confidence before calculating
if count > 0:
    average = total / count
# if no lines found print an error
else:
    print('No "X-DSPAM-Confidence" Lines found')

print('Average spam confidence:', average)

