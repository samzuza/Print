def system(newList):
    for x in newList:
        print(x, end=' ')


list1 = input("Enter numbers: ")

numbers = list1.split()

for i in range(0, len(numbers)):
    numbers[i] = int(numbers[i])

list2 = set(numbers)

newList = (list(list2))
print("The distinct numbers are: ", end='')
system(newList)
