sec = 20
def hello():
    sec= sec - 1
    label["text"]=str(sec)
    if sec>0 and stop!=1:
        label.after(1000, hello)
    else:
        btn["state"]="disabled"
        label["fg"]="red"

def stop():
    return 1
    
from tkinter import *

tk = Tk()
tk.title("Some button")
label=Label(tk)
label["text"]=str(sec)
label.pack()
label.after(1000, hello)
btn = Button(tk)
btn["text"]='Click to stop'
btn["height"]=1
btn["width"]=10
btn["command"]=stop
btn["bg"]="white"
btn["activebackground"]="#cdc9c9"
btn["activeforeground"]="red"
btn["relief"]="ridge"
btn.pack()


