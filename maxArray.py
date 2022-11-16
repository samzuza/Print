import random

list1 = [2, 3, 4, 1, 32]
list2 = [2, 3, 5, 7, 9, 1]

#5
print(len(list1))

# 32
print(max(list1))

# 1
print(min(list1))

# 42
print(sum(list1))

# 32
print(list1[-1])

# 4
print(list1[-3])

# 3 is in the 1 position
print(list1.index(1))

# 1 is the first in the list
print(list1.count(1))

# prints 5, 7 because it starts at index 2 up until 4th index - 1 (so 3rd index)
print(list2[2: 4])

# prints 2, 5, 9 because it starts at index 0 up until 5th index - 1 (so 4th index)
# but the 2 skips every other index
print(list2[0: 5: 2])

# prints 2, 3, starts at 0 until index 2 - 1 (which is 1)
print(list2[: 2])

# prints 7, 9, 1, starts at 3 - 1 (which is 1) and goes until the last index
print(list2[3:])

# prints 3, 5 because -3 + 6 = 3, prints index 3 - 1 (which is 2)
print(list2[1: -3])

# prints 5, 7 because -4 + 6 = 2 and -2 + 6 = 4, prints index 2 to 4 - 1 (which is 3)
print(list2[-4: -2])

random.shuffle(list1)
print(list1)

for i in range(len(list1)):
    list1[i] = i
    print(list1)

