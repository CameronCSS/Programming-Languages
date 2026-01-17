# A program that takes input from the user for the length and width of a rectangle
# and then prints the rectangle perimter. 

# Middle of the rectingle is empty.

# User picks symbol used to draw the rectangle.

print("--------------------------------")
print("Rectangle Perimeter Calculator")
print("--------------------------------")

width = int(input("Enter the width: ")) 
length = int(input("Enter the length: "))
symbol = input("Enter the symbol: ")

for i in range(width):
    if i == 0 or i == width - 1:
        print(symbol * length)
    else:
        print(symbol + " " * (length - 2) + symbol)
