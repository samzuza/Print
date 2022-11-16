lst = [4, 5, 6, 7, 8, 9]
temp = lst[0] # keeps the first element

# shift elements left
for i in range(1, len(lst)):
    lst[i - 1] = lst[i]

# move the first element to fill in the last position
lst[len(lst) - 1] = temp

# [5, 6, 7, 8, 9, 4]
print(lst)


# it can also be written as
lst = lst[1: len(lst)] + lst[0: 1]

# shifts the new lst
# [6, 7, 8, 9, 4, 5]
print(lst)

