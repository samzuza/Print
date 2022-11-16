def isSorted(lst):
    lst1 = lst.copy()

    lst1.sort()

    if lst1 == lst:
        print("The list is already sorted")
    else:
        print("The list is not sorted")


numbers = input("Enter list: ")

lst = numbers.split()

for i in range(0, len(lst)):
    lst[i] = int(lst[i])

isSorted(lst)
