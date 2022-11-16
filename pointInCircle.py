import turtle
x1 = float(input("Enter the center x-coordinate of a circle: "))
y1 = float(input("Enter the center y-coordinate of a circle: "))
radius = float(input("Enter the radius of the circle: "))
x2 = float(input("Enter a point x-coordinate: "))
y2 = float(input("Enter a point y-coordinate: "))

turtle.penup()
turtle.goto(x1, y1 - radius)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(x2,y2)
turtle.pendown()
turtle.dot(6, "red")

turtle.penup()
turtle.goto(x1 - 70, y1 - radius - 20)
turtle.pendown()

d = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
if d >= radius:
    turtle.write("The point is inside the circle.")
else:
    turtle.write("The point is outside the circle")

turtle.hideturtle()
turtle.done()