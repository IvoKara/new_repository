from tkinter import *

tk = Tk()
x = Canvas(tk, height=400, width=400)
x.pack()
pic = PhotoImage(file='C:\Users\user\Desktop\skrillex.jpg')
x.create_image(0, 0, anchor=NW, image=pic)
