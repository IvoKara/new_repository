from tkinter import *

lol = Tk()
color_choose = colorchooser.askcolor()
color_choose2 = colorchooser.askcolor()
sir = Canvas(lol, width=600, height=600)
sir.pack()
sir.create_line(0,0,600,600, fill='orange')
sir.create_rectangle(200,40,400,60, fill=color_choose[1],outline=color_choose2[1])
sir.create_rectangle(0,0,200,200)
sir.create_arc(10, 10, 200, 100, extent=359, style=ARC)
sir.create_polygon(10, 400, 60, 400, 70, 450, 30, 500,
                   fill=color_choose[1], outline=color_choose2[1])
sir.create_text(450, 400, text='The brown fox jumped over the dog',fill='blue',
                font=('Lucida Handwriting', 10))

