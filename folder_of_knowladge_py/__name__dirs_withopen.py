print("__name__ is ", __name__)
#import it(don't run it directly)

import os
print(os.getcwd())
for i in os.listdir("."):
    print(i)

with open("classes.py","r") as f:
    print(f.readline())

import tkinter as tk
window = tk.Tk()
tk.mainloop()
print("Anybody home?")
