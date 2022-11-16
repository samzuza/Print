number = 25
isPrime = True
i = 2
while i < number and isPrime:
    if number % i == 0:
        isPrime = False

    i += 1

print("i is", i, "isPrime is", isPrime)
