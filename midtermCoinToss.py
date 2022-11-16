import random

coin = random.randint(0, 1)

print("Guess head or tail?")
guess = int(input("Enter 0 for head and 1 for tail: "))

if (guess == 0) and (coin == 0):
    print("Correct, it is a head")
elif (guess == 1) and (coin == 1):
    print("Correct, it is a tail")
elif (guess == 0) and (coin == 1):
    print("Sorry, it is a tail")
elif (guess == 1) and (coin == 0):
    print("Sorry, it is a head")