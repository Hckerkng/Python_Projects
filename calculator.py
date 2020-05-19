from tkinter import * 
from tkinter.ttk import *
class PressButton(Button):
    def __init__(self,master,value):
        self.value = value
        super().__init__(master)
        self['text'] = value
        self['command'] = self.add
    def add(self):
        d = var.get()
        v = d+str(self.value)
        var.set(v)       
root = Tk()

var = StringVar()
e = Entry(root,textvariable=var,width=45,font=('Times',20,'bold'))
e.grid(row=0,column=0,rowspan=2,columnspan=4,ipadx=10,ipady=10,padx=15,pady=15)

ob = Button(root,text="(",command = lambda : var.set(var.get()+"("))
ob.grid(row=0,column=4,ipadx=5,ipady=5,pady=5)

cl = Button(root,text=")",command = lambda :var.set(var.get()+")"))
cl.grid(row=1,column=4,ipadx=5,ipady=5)

b = ['1','2','3','+','4','5','6','-','7','8','9','*','00','0','.','/']
for row in range(2,6):
    col=0
    for col in range(0,4):
        button = PressButton(root,b[col])
        button.config(width=20)
        button.grid(row=row,column=col,ipadx=10,ipady=10,padx=5,pady=5)
    b = b[4:]

def clear():
    var.set('')
def back_space():
    var.set(var.get()[:-1])
def equal():
    var.set(var.get()+"="+str(round(eval(var.get()),2)))
clr=Button(root,text="Clear",command=clear)
clr.grid(row=2,column=4,padx=10,pady=10,ipadx=5,ipady=5)
back= Button(root,text="X",command=back_space)
back.grid(row=3,column=4,padx=10,pady=10,ipadx=5,ipady=5)
eq = Button(root,text="=",command=equal)
eq.grid(row=4,column=4,padx=10,pady=10,ipadx=5,ipady=5)
quit = Button(root,text="Exit",command=root.destroy)
quit.grid(row=5,column=4,padx=10,pady=10,ipadx=10,ipady=10)

root.wm_minsize(780,320)
root.wm_maxsize(780,320)
root.iconbitmap("cal.ico")
root.title("Calculator")
root.mainloop()
