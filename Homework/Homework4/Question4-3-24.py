ISBN = input("Enter the first 9 digits of an ISBN as a string: ")

digit = len(str(ISBN))
intISBN = int(ISBN)

if digit != 9:
    print("Incorrect input. It must have exact 9 digits")
else:
    first = int((intISBN % 1000000000) / 100000000)
    second = int((intISBN % 100000000) / 10000000)
    third = int((intISBN % 10000000) / 1000000)
    fourth = int((intISBN % 1000000) / 100000)
    fifth = int((intISBN % 100000) / 10000)
    sixth = int((intISBN % 10000) / 1000)
    seventh = int((intISBN % 1000) / 100)
    eighth = int((intISBN % 100) / 10)
    ninth = int(intISBN % 10)
    checksum: int = ((first * 1 + second * 2 + third * 3 + fourth * 4 + fifth * 5
            + sixth * 6 + seventh * 7 + eighth * 8 + ninth * 9) % 11)
    if checksum == 10:
            checksum = 'X'
            print("The ISBN-10 number is", ISBN, checksum)
    else:
            print("The ISBN-10 number is", ISBN, checksum)
