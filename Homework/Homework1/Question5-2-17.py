investment = float(input("Enter investment amount: "))

annualInterestRate = float(input("Enter annual interest rate: "))
annualInterestRate = annualInterestRate / 100
monthlyInterestRate = annualInterestRate / 12 #12 months in a year

years = float(input("Enter number of years: "))
months = years * 12 #12 months in a year

accumulatedValue = float(round(investment * ((1 + monthlyInterestRate) ** months), 2))

print("Accumulated value is ", accumulatedValue)