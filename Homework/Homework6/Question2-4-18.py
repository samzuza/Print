def futureInvestmentValue(invest, monthlyInterestRate, years):
    print("Years\tFuture Value")
    # range of 1 - years
    for i in range(1, years + 1):
        futureValue = invest * ((1 + monthlyInterestRate) ** (12 * i))

        print(i, "\t\t\t\t", round(futureValue, 2))


invest = float(input("The amount invested: "))

interest = float(input("Annual interest rate: "))

year = 30

futureInvestmentValue(invest, interest / 1200, year)
