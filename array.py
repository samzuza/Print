s = "Welcome"
# 'W'
print(s[0])
# "e'
print(s[1])


# splitting a string into a list
items = "Jane John Peter Susan".split()
# ['Jane', 'John', 'Peter', 'Susan']
print(items)

items1 = "09/20/2012".split("/")
# ['09', '20', '2012']
print(items1)

s1 = "welcome".split('o')
# ['welc', 'me']
print(s1)

s2 = "hi im sam".split()
# ['hi', 'im', 'sam']
print(s2)

s3 = "a$b$c$d".split('$')
# ['a', 'b', 'c', 'd']
print(s3)

# prints 10 numbers vertically in a column
array1 = []
print("Enter 10 numbers, one number per line: ")
for i in range(10):
    array1.append(float(input()))


t = input("Enter 10 numbers separated by spaces on one line: ")
items = t.split() # extracts items from the string
print(items)
array2 = [float(x) for x in items] # convert items to numbers
print(array2)


ourList = [1, 5, 5, 5, 5, 1]
max = ourList[0]
indexMax = 0
for i in range(1, len(ourList)):
    if ourList[i] > max:
        max = ourList[i]
        indexMax = i
# 1
print(indexMax)


yourList = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    yourList[i - 1] = yourList[i]

for i in range(0, 6):
    # 2 3 4 5 6 6
    print(yourList[i], end=" ")

# create a list with 100 boolean false values
    # lst = 100 * [False]
# assign the value 5.5 to the last element in the list
    # lst.append(5.5)
# display the sum of the first two elements
    # print(lst[0] + lst[1])
# compute the sum of the first five elements in the list
    # total = sum(lst[0:5])
# find the minimum element in the list
    # minimum = min(lst)
# randomly generate an index and display the element of this index in the list
    # print(list[random.randint(0, len(lst) - 1)])

# append(x) adds an element to the end of the list
# count(x) returns the number of times element x appears in the list
# extend(antherList) appends all the elements in anotherList to the list
# index(x) returns the index of the first occurrence of element x in the list
# insert(index, x) inserts an element at the given index
# pop(index) = removes the element at the given index and return it
# list.pop() removes and returns the last element in the list
# remove(x) removes the first occurrence of element x from the list
# ['09', '20', '2012']
print()

set1 = [1, 2]
set2 = [3, 4]

# [1, 2, 3, 4]
set3 = set1 + set2
print(set3)

# [1, 2, 1, 2, 1, 2]
set4 = 3 * set1
print(set4)


myList = [1, 2, 3, 4, 5, 6, 7]

# 1 2 3 4 5 6 7 counted with entered spaces
for u in myList:
    print(u)

# 1 3 5 7 counted with entered spaces
for i in range(0, len(myList), 2):
    print(myList[i])

lst = [1, 2, 3, 4, 5, 6]

# [1, 1, 1, 1, 1, 1]
for i in range(1, 6):
    lst[i] = lst[i - 1]

print(lst)


#list1 = ["green", "red", "blue"]
#list2 = ["red", "blue", "green"]
list1 = [30, 1, 2, 1, 0]
list2 = [1, 21, 13]

# false / false
print(list2 == list1)
# true / true
print(list2 != list1)
# true looks for if r is greater than g
# false looks for if 1 is greater than 30
print(list2 > list1)
# true / false
print(list2 >= list1)
# false looks for if r is less than g
# true looks for if 1 is less than 30
print(list2 < list1)
# false / true
print(list2 <= list1)
# [30, 1, 2, 1, 0, 1, 21, 13]
print(list1 + list2)
# [1, 21, 13, 1, 21, 13]
print(2 * list2)
# 1, 21, 13, 1, 21, 13]
print(list2 * 2)
# [1, 2]
print(list1[1: 3])
# 1
print(list1[3])
# [30, 2]
print([x for x in list1 if x > 1])
# [0, 2, 4, 6, 8]
print([x for x in range(0, 10, 2)])
# [10, 8, 6, 4, 2]
print([x for x in range(10, 0, -2)])


list3 = [x for x in range(5)]
# [0, 1, 2, 3, 4]
print(list3)

list4 = [0.5 * x for x in list3]
# [0.0, 0.5, 1.0, 1.5, 2.0]
print(list4)

list5 = [x for x in list4 if x < 1.5]
# [0.0, 0.5, 1.0]
print(list5)