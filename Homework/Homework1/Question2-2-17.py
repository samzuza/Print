minutes = int(input("Enter the number of minutes: "))
remainingMinutes = minutes

years = remainingMinutes//525600
remainingMinutes = remainingMinutes % 525600

days = remainingMinutes//1440
remainingMinutes = remainingMinutes % 1440

print(minutes, " minutes is approximately ", years,
      "years and ", days, "days")