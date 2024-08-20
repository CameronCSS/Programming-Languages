# This is my answer for the Python for Everyone course Chapter 4.6
# The question asks:

# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. 
# Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. 
# The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number. 
# Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. 
# Do not name your variable sum or use the sum() function.



NOTE: *
"I have since come back to this after a year and decided to update my answer with better code."

# Original ANSWER:

def computepay(h, r):
    if h >= 40:
        rp = 40 * r
        ot = (h - 40) * r * 1.5
        pay = rp + ot
    else:
        pay = h * r
    return pay

while True:
    try:
        hrs = float(input("Enter Hours: "))
        if hrs > 100:
            raise ValueError("T")
        rate = float(input("Enter Rate of Pay: "))
        break # Break out of the loop if inputs are valid
    except ValueError as e:
        if str(e) == "T":
            print("Error: Are you sure you worked that much? Double check your hours and enter again.")
        else:
            print("Error: Invalid input. Please enter a number.")
    except:
        print("Error: Unknown error occurred.")

p = computepay(hrs, rate)
print("Pay", p)


#  NEW UPDATED ANSWER:

def computepay(h, r):
    if h > 40:
        ot = h - 40
        op = ot * (r * 1.5)
        h = 40
        p = (h * r) + op
    else:
        p = h * r
    return p

def get_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            value = float(user_input)
            return value
        except ValueError:
            print("Please enter a valid number.")


h = get_input("Enter Hours: ")
r = get_input("Enter Pay Rate: ")


pay = computepay(h, r)

print("Pay", pay)
