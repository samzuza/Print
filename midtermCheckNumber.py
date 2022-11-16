x = int(input("Enter an integer: "))

if (x % 5 == 0) and (x % 6 == 0):
    print("Is", x, "divisible by 5 and 6? True")
else:
    print("Is", x, "divisible by 5 and 6? False")

    if (x % 5 == 0) or (x % 6 == 0):
        print("Is", x, "divisible by 5 or 6? True")
    else:
        print("Is", x, "divisible by 5 or 6? False")

        if ((x % 5 == 0) or (x % 6 == 0)) and not ((x % 5 == 0) and (x % 6 == 0)):
            print("Is", x, "divisible by 5 or 6, but not both? True")
        else:
            print("Is", x, "divisible by 5 or 6, but not both? False")

