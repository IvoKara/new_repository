import turtle 

ninja = turtle.Turtle()

ninja.speed(100)
ninja.color('red')
for i in range(360):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)
    
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    
    ninja.right(1)
    
turtle.done()
