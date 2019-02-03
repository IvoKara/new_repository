import turtle
circle = turtle.Turtle()
circle.speed(100)
for rounding in range(360):
    circle.forward(1)
    circle.left(1)

for rounding in range(360):
    circle.forward(2)
    circle.left(1)
turtle.done()
