def binaryToHex(binaryValue):
    # formats binaryValue with base 2
    # and X tells it to include hexadecimal
    # or else it would print just the base 10 value
    hexadecimal = f"{int(binaryValue, 2) :X}"
    print("The hex value is", hexadecimal)
    return


binaryValue = input("Enter a binary number: ")

binaryToHex(binaryValue)

