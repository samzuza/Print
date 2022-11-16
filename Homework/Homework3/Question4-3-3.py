y = int(input("Enter year: (e.g., 2008): "))
m = int(input("Enter month: 1-12: "))
q = int(input("Enter the day of the month: 1-31: "))

j = y // 100
k = y % 100

h = ((q + ((26 * (m + 1)) // 10) + k + (k // 4) + (j // 4) + (5 * j)) % 7)

if h == 0:
    h = "Saturday"
elif h == 1:
    h = "Sunday"
elif h == 2:
    h = "Monday"
elif h == 3:
    h = "Tuesday"
elif h == 4:
    h = "Wednesday"
elif h == 5:
    h = "Thursday"
else:
    h = "Friday"

print("Day of the week is", h)
