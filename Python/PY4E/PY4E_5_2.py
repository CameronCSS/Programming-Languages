largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        fval = int(num)
    except:
        print('Invalid input')
        continue
    if smallest is None : 
        smallest = fval
    elif fval < smallest :
        smallest = fval
    if largest is None : 
        largest = fval
    elif fval > largest :
        largest = fval
    

print("Maximum is", largest)
print("Minimum is", smallest)
