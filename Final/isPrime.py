# show printout if input = 9
# i is 4
# 9 is not prime

number = eval(input("Enter an integer: "))

isPrime = True

i = 2
while i < number and isPrime:
    if number % i == 0:
        isPrime = False
    i += 1

print("i is", i)

if isPrime:
    print(number, "is prime")
else:
    print(number, "is not prime")