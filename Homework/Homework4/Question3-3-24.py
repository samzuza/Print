year = int(input("Enter a year: "))

month = input("Enter a month: ")

isLeapYear = (year % 4 == 0 and year % 100 != 0) or \
             (year % 400 == 0)

day = 1

if month == 'Jan':
    day = 31
    print(month, year, "has", day, "days")
elif month == 'Feb' and isLeapYear:
    day = 29
    print(month, year, "has", day, "days")
elif month == 'Feb':
    day = 28
    print(month, year, "has", day, "days")
elif month == 'Mar':
    day = 31
    print(month, year, "has", day, "days")
elif month == 'Apr':
    day = 30
    print(month, year, "has", day, "days")
elif month == 'May':
    day = 31
    print(month, year, "has", day, "days")
elif month == 'June':
    day = 30
    print(month, year, "has", day, "days")
elif month == 'July':
    day = 31
    print(month, year, "has", day, "days")
elif month == 'Aug':
    day = 31
    print(month, year, "has", day, "days")
elif month == 'Sep':
    day = 30
    print(month, year, "has", day, "days")
elif month == 'Oct':
    day = 31
    print(month, year, "has", day, "days")
elif month == 'Nov':
    day = 30
    print(month, year, "has", day, "days")
elif month == 'Dec':
    day = 31
    print(month, year, "has", day, "days")
else:
    print(month, "is not a correct month name")