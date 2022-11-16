#there are 31,536,000 seconds in a year
birth = 31536000/7
death = 31536000/13
immigrant = 31536000/45


year1 = round((birth - death + immigrant))
year2 = year1 + round((birth - death + immigrant))
year3 = year2 + round((birth - death + immigrant))
year4 = year3 + round((birth - death + immigrant))
year5 = year4 + round((birth - death + immigrant))

print("The projected population for year 1 is", year1)
print("The projected population for year 2 is", year2)
print("The projected population for year 3 is", year3)
print("The projected population for year 4 is", year4)
print("The projected population for year 5 is", year5)