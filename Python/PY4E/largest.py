largest_so_far = 0

print('Before', largest_so_far)
for num in [9, 41, 12, 3, 74, 15]:
    if num > largest_so_far:
        largest_so_far = num
    print(largest_so_far, num)

print('After', largest_so_far)