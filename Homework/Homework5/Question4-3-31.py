loanAmount = int(input("Loan Amount: "))
years = int(input("Number of Years: "))

print("Interest Rate\tMonthly Payment\tTotal Payment")

percentRate = 5.000
interestRate = percentRate / 1200

for i in range(5, 30):
    monthlyPay = loanAmount * interestRate / (1 - 1 / (1 + interestRate) ** (years * 12))
    totalPay = monthlyPay * years * 12
    monthlyPay = "{:.2f}".format(monthlyPay)
    totalPay = "{:.2f}".format(totalPay)
    print(percentRate, "%\t\t\t", monthlyPay, "\t\t", totalPay)
    interestRate = interestRate + (0.00125/12)
    percentRate = percentRate + 0.125
