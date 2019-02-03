import turtle
shape = turtle.Turtle()

def draw_star(color, turtle_color, size):
    shape.up()
    shape.color(turtle_color)
    shape.fillcolor(color)
    shape.down()
    shape.begin_fill()
    for i in range(5):
        shape.forward(size)
        shape.left(144)
        shape.forward(size)
    shape.end_fill()

draw_star("green", "orange", 20)
