import tkinter as tk
from random import choice
root = tk.Tk()
cl = [ '0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'] 
def change_color():
    r = choice(cl) + choice(cl)
    g = choice(cl) + choice(cl)
    b = choice(cl) + choice(cl)
    color = "#" +r+g+b
    print(color)
    root.config(bg=color)
button = tk.Button(root,text="Change Color", command=change_color)
button.pack()
root.wm_minsize(400,400)
root.mainloop()
