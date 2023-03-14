# Data in Motion Python Challenge # 31

#### VERY EASY

# Write a function that takes the base and height of a triangle and return its area.

# The area of a triangle is: (base * height) / 2

# Example:

# tri_area(3, 2) ➞ 3

while True:
    try:
        b = float(input('Enter Base:'))
        h = float(input('Enter Height:'))

        tri_area = (b * h) / 2
        print(tri_area)
        break
    except ValueError: 
        print("Error: Invalid input. Please enter a valid number.")
        continue
        
        
        
######################################

# Data in Motion Python Challenge # 31

#### EASY

# Create a function that takes an integer and returns the factorial of that integer. That is, the integer multiplied by all positive lower integers.

# Example 
# factorial(13) ➞ 6227020800


while True:
    try:
        n = int(input('Enter an Integer:'))
        fact_of_n = math.factorial(n)
        print(fact_of_n)
        break
    except ValueError:
        print("Error: Invalid input. Please enter a valid Integer.")
        continue
        
######################################
        
# Data in Motion Python Challenge # 31

#### MEDIUM

# Create a function that takes three values:

# h hours
# m minutes
# s seconds

# Return the value that's the longest duration.

# Example 
# longest_time(15, 955, 59400) ➞ 59400

while True:
    try:
        hours = float(input('Enter hours'))
        h = (hours * 60) * 60
        minutes = float(input('Enter minutes'))
        m = minutes * 60
        seconds = (input('Enter seconds'))
        s = float(seconds)
        
        if h > m and h > s:
            print(hours)
        elif m > h and m > s:
            print(minutes)
        else:
            print(seconds)
        break
    except ValueError:
        print("Error: Invalid input. Please enter a valid Integer.")
        continue
        
        
######################################

# Data in Motion Python Challenge # 31

#### HARD

# Given a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.

# Example 
# pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }

def pluralize(words):
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    
    result = set()
    for word, freq in count.items():
        if freq > 1:
            result.add(word + "s")
        else:
            result.add(word)
    
    return result


words = ["cow", "pig", "cow", "cow"]
print(pluralize(words))

words = ["table", "table", "table"]
print(pluralize(words))

words = ["chair", "pencil", "arm"]
print(pluralize(words))

words = ["capybara", "capybara", "capybara"]
print(pluralize(words))

