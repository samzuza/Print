year = int(input("Enter a year: "))

isLeapYear = (year % 4 == 0 and year % 100 != 0) or \
             (year % 400 == 0)

print(year, "is a leap yaer?", isLeapYear)