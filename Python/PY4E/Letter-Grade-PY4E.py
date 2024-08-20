# This code is for lesson 3 of the coursera course Python for Everybody.
# The task was this
# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. 
# If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

# I also set the value of grade to None in case they had a valid entry, and then their next entry was invalid it wouldnt return an error and a grade.

score = input("Enter a Score between 0.0 and 1.0: ")
try:
    grade = float(score)
except: 
    print ('Please enter a valid number')
    grade = None
if grade is not None and grade > 1.0:
    print('Please enter a number between 0.0 and 1.0')
    score = input("Enter a Score between 0.0 and 1.0: ")
    try:
        grade = float(score)
    except: 
        print ('Please enter a valid number')
        grade = None
else:
    if grade is None:
        print('No grade entered')
    elif grade >= 0.9:
        print('A')
    elif grade >= 0.8:
        print('B')
    elif grade >= 0.7:
        print('C')
    elif grade >= 0.6:
        print('D')
    else:
        print('F')
