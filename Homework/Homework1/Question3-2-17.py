integer = int(input("Enter a 4 digit integer: "))

firstInteger = int((integer % 10000) / 10 / 10 / 10)
newFirst = firstInteger

secondInteger = int((integer % 1000) / 10 / 10)
newSecond = secondInteger

thirdInteger = int((integer % 100) / 10)

fourthInteger = int(integer % 10)

firstInteger = fourthInteger
secondInteger = thirdInteger
thirdInteger = newSecond
fourthInteger = newFirst

print(firstInteger)
print(secondInteger)
print(thirdInteger)
print(fourthInteger)