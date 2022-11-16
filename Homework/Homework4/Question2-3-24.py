letter = input("Enter a letter grade: ")

if letter.upper() == 'A':
    grade = 4
    print("The numeric value for grade", letter.upper(), "is", grade)

elif letter.upper() == 'B':
    grade = 3
    print("The numeric value for grade", letter.upper(), "is", grade)

elif letter.upper() == 'C':
    grade = 2
    print("The numeric value for grade", letter.upper(), "is", grade)

elif letter.upper() == 'D':
    grade = 1
    print("The numeric value for grade", letter.upper(), "is", grade)

elif letter.upper() == 'F':
    grade = 0
    print("The numeric value for grade", letter.upper(), "is", grade)

else:
    print(letter.upper(), "is an invalid grade")