sum = 0
positive = 0
negative = 0
count = 0
number = 1

number = int(input("Enter an integer, the input ends if it is 0: "))

sum = sum + number

if number == 0:
    print("No numbers are entered except 0")
elif number > 0:
    positive += 1
else:
    negative += 1

while number != 0:
    number = int(input("Enter an integer, the input ends if it is 0: "))
    sum = sum + number
    count+=1
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        average = sum / count
        print("The number of positives is", positive)
        print("The number of negatives is", negative)
        print("The total is", sum)
        print("The average is", average)