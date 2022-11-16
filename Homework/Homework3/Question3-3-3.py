month = int(input("Enter a month in the year (e.g., 1 for Jan): "))

year = int(input("Enter a year: "))

isLeapYear = (year % 4 == 0 and year % 100 != 0) or \
             (year % 400 == 0)

day = 1

if month == 1:
    day = 31
    month = "January"
elif month == 2 and isLeapYear:
    day = 29
    month = "February"
elif month == 2:
    day = 28
    month = "February"
elif month == 3:
    day = 31
    month = "March"
elif month == 4:
    day = 30
    month = "April"
elif month == 5:
    day = 31
    month = "May"
elif month == 6:
    day = 30
    month = "June"
elif month == 7:
    day = 31
    month = "July"
elif month == 8:
    day = 31
    month = "August"
elif month == 9:
    day = 30
    month = "September"
elif month == 10:
    day = 31
    month = "October"
elif month == 11:
    day = 30
    month = "November"
else:
    day = 31
    month = "December"

print(month, year, "has", day, "days")