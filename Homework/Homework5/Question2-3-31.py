initialTuition = 10000
increaseRate = 0.05
year = 0
yearsPaid = 0
newTuition = 0

while year < 10:
    initialTuition = initialTuition + (initialTuition * increaseRate)
    year += 1

print("In 10 years the tuition will be $", initialTuition)

newTuition = newTuition + initialTuition

while yearsPaid < 3:
    initialTuition = initialTuition + (initialTuition * increaseRate)
    newTuition = newTuition + initialTuition
    yearsPaid += 1

print("The total cost of 4 years' worth of tuition starting after the 10th year is $", newTuition)