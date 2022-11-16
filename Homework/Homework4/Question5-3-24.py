import string

hexDigit = input("Enter a hex digit: ")

result = string.hexdigits

if hexDigit == 0:
    print("The binary value is 0000")
elif hexDigit == 1:
    print("The binary value is 0001")
elif hexDigit == 2:
    print("The binary value is 0010")
elif hexDigit == 3:
    print("The binary value is 0011")
elif hexDigit == 4:
    print("The binary value is 0100")
elif hexDigit == 5:
    print("The binary value is 0101")
elif hexDigit == 6:
    print("The binary value is 0110")
elif hexDigit == 7:
    print("The binary value is 0111")
elif hexDigit == 8:
    print("The binary value is 1000")
elif hexDigit == 9:
    print("The binary value is 1001")
elif hexDigit == 'a' or hexDigit == 'A':
    print("The binary value is 1010")
elif hexDigit == 'b' or hexDigit == 'B':
    print("The binary value is 1011")
elif hexDigit == 'c' or hexDigit == 'C':
    print("The binary value is 1100")
elif hexDigit == 'd' or hexDigit == 'D':
    print("The binary value is 1011")
elif hexDigit == 'e' or hexDigit == 'E':
    print("The binary value is 1110")
elif hexDigit == 'f' or hexDigit == 'F':
    print("The binary value is 1111")
else:
    print("Invalid input")