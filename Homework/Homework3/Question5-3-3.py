x = float(input("Enter the x-coordinate of the point: "))
y = float(input("Enter the y-coordinate of the point: "))

point = "is in"

if (x > -2.5) and (x < 2.5) and (y > -5) and (y < 5):
    print("Point (", x, ", ", y, ") is in the rectangle")
else:
    print("Point (", x, ", ", y, ") is not in the rectangle")

