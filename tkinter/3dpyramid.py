from tkinter import *

alf = Tk()
canvas = Canvas(alf, width=400, height=400)
canvas.pack()


canvas.create_rectangle(3,3, 397,397)
canvas.create_rectangle(6,6, 394,394)

x = 0
y = 400
while y >= 200 and x <= 200:
    y -= 3
    x += 3
    canvas.create_rectangle(x,x,y,y)
