sum = 0

count = 0
i = 0.01

while count < 100:
    sum += i
    i = i + 0.01
    count += 1

print("The sum is", sum)

sum = 0
number = 0
while number < 20:
    number += 1
    sum += number
    if sum >= 100:
        break

print("The number is", number)
print("The sum is", sum)

sum = 0
number = 0
while number < 20:
    number += 1
    if number == 10 or number == 11:
        continue #skips next line if continue conditions are met
    sum += number

print("The sum is", sum)
print("The number is", number)