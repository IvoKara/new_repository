import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_arc(10, 10, 60, 60, extent=359, style=ARC, fill='black')
for x in range(0, 100):
    canvas.move(1, 2, 0)
    canvas.create_line(x+2,35,x+22,35)
    tk.update()
    time.sleep(0.0001)
    
for x in range(0, 10):
    canvas.move(1, 0, 2)
    tk.update()
    time.sleep(0.0001)
    
for x in range(0, 20):
    canvas.move(1, -2, 2)
    tk.update()
    time.sleep(0.0001)

def move(event):
    if event.keysym == 'Right':
        canvas.move(1,9,0)
    elif event.keysym == 'Up':
        canvas.move(1,0,-9)
    elif event.keysym == 'Down':
        canvas.move(1,0,9)
    else:
        canvas.move(1,-9,0)
canvas.bind_all('<KeyPress-Up>', move)
canvas.bind_all('<KeyPress-Down>', move)
canvas.bind_all('<KeyPress-Left>', move)
canvas.bind_all('<KeyPress-Right>', move)
