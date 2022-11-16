amount = float(input("Enter the amount as a decimal number: "))
remainingAmount = int(amount*100) #converts to cents

dollars = remainingAmount//100
remainingAmount = remainingAmount % 100

quarters = remainingAmount//25
remainingAmount = remainingAmount % 25

dimes = remainingAmount//10
remainingAmount = remainingAmount % 10

nickles = remainingAmount//5
remainingAmount = remainingAmount % 5

pennies = remainingAmount//1
remainingAmount = remainingAmount % 1

print(dollars, quarters, dimes, nickles, pennies, amount)