lst = [1, 2, 3, 5, 4, 5]
lst1 = lst.copy()

lst1.sort()

if lst1 == lst:
    print(lst1, lst)
    print("yes")
else:
    print(lst1, lst)
    print("no")