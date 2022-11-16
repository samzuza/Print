subtotal = float(input("Enter subtotal: "))

gratuity = float(input("Enter the gratuity rate: "))

gratuity = float(round(subtotal * (gratuity/100), 2))

total = subtotal + gratuity

print("The gratuity is ", gratuity, "and the total is ", total)
