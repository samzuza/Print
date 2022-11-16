distance = float(input("Enter the driving distance: "))
mpg = float(input("Enter miles per gallon: "))
ppg = float(input("Enter price per gallon: "))

cost = distance / mpg * ppg

print("The cost of driving is $", cost)