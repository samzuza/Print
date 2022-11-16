NUMBER_OF_ELEMENTS = 3
numbers = []
sum = 0

for i in range(NUMBER_OF_ELEMENTS):
    value = float(input("Enter a new number: "))
    numbers.append(value)
    sum += value

average = sum / NUMBER_OF_ELEMENTS

count = 0
for i in range(NUMBER_OF_ELEMENTS):
    if numbers[i] > average:
        count += 1

print("Average is", average)
print("Number of elements above the average is", count)
