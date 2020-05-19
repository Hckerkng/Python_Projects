#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[ ]:


import tkinter as tk
from tkinter.ttk import *
from tkinter.messagebox import * 
r=tk.Tk()

frame=tk.Frame(r)
frame.config(bg="red")
frame.pack(expand=tk.YES,fill=tk.X)

counter=1000
records=dict()
v1=""
v2=""
o=tk.StringVar()
i=tk.StringVar()

def log():
    k=tk.StringVar()
    l=tk.StringVar()
    nw=tk.Toplevel(r)
    q=tk.Label(nw,text="Account",font=("Times",25,"bold"))
    q.config(bg="blue")
    q.pack(anchor=tk.NW,expand=tk.YES)
    
    a=tk.Entry(nw,textvariable=k)
    a.pack(anchor=tk.NW,expand=tk.YES)
    a.focus()
    
    
    o=tk.Label(nw,text="Password ",font=("Times",25,"bold"))
    o.config(bg="blue")
    o.pack(anchor=tk.W,expand=tk.YES)
    
  
    p=tk.Entry(nw,textvariable=l)
    p.pack(anchor=tk.W,expand=tk.YES)
    
    i=tk.Button(nw,text="submit",command=sub)
    i.pack(anchor=tk.S,expand=tk.YES)
    
    global v1
    v1=k.get()
    print(v1)
    global v2
    v2=l.get()
    print(v2)    
    
def sub():
    print(v1,v2)
    if v1 in records.keys():
            if records[v1]['password']==v2:
                n=tk.Toplevel(nw)
                w=tk.Label(n,text="Login Succesfull",font=("Times",25,"bold"))
                w.config(bg="blue")
                w.pack(anchor=tk.NW,expand=tk.YES)
    
                e=tk.Button(n,text="Credit",command=lambda :cred(v3))
                e.config(bg="white")
                e.pack()
                
                s=tk.Entry(n,textvariable=v3)
                s.pack(anchor=tk.NW,expand=tk.YES)
                s.focus()
    
                t=tk.Button(n,text="Dedit",command=lambda: deb(v4))
                t.config(bg="white")
                t.pack()
                
                d=tk.Entry(n,textvariable=v4)
                d.pack(anchor=tk.NW,expand=tk.YES)

                y=tk.Button(n,text="Check balance",command=chck)
                y.config(bg="white")
                y.pack()

                u=tk.Button(n,text="Logout",command=r.quit())
                u.config(bg="white")
                u.pack()
                
            else:
                showerror("Sorry","password does not match")
    else:
        showerror("Sorry","account not found")
    print(v1,v2)

def cred(v3):
        balance=(records[v1]["balance"])+v3
        records[v1]['balance']=balance
        showerror("Amount succesfully credited",balance)
        
def deb(v4):
    balance=0
    if records[v1]["balance"]>=d:
        balance=(records[v1]["balance"])-d
        records[v1]["balance"]=balance
        showerror("Amount succesfully debited",balance)
    else:
        showerror("insufficient balance",balance)
def check():
    showerror("balance is",records[v1]["balance"])
def sig():
    global v1,o,i
    v1=o.get()
    global v2
    v2=i.get()
    v4=tk.StringVar()
    global counter
    ac_no=counter
    counter=counter+1
    global records
    records.update({ac_no:{"name":v1,"password":v2,"balance":v4}})
    
    nw=tk.Toplevel(r)
    q=tk.Label(nw,text="Name",font=("Times",25,"bold"))
    q.config(bg="blue")
    q.pack(anchor=tk.NW,expand=tk.YES)
    
    a=tk.Entry(nw,textvariable=o)
    a.pack(anchor=tk.NW,expand=tk.YES)
    a.focus()
    
    
    o=tk.Label(nw,text="Password ",font=("Times",25,"bold"))
    o.config(bg="blue")
    o.pack(anchor=tk.W,expand=tk.YES)
    
  
    p=tk.Entry(nw,textvariable=i)
    p.pack(anchor=tk.W,expand=tk.YES)
    
    z=tk.Label(nw,text="initial balance ",font=("Times",25,"bold"))
    z.config(bg="blue")
    z.pack(anchor=tk.W,expand=tk.YES)
    
  
    x=tk.Entry(nw,textvariable=v4)
    x.pack(anchor=tk.W,expand=tk.YES)
    
    c=tk.Button(nw,text="submit",command=nw.destroy)
    c.pack(anchor=tk.S,expand=tk.YES)
    
    print(records)
    

    

l=tk.Label(frame,text="WELCOME TO MY BANK APPPLICATION ",font=("Times",25,"bold"))
l.config(bg="blue")
l.pack(expand=tk.YES,fill=tk.X)

b=tk.Button(frame,text="LOGIN",command=log)
b.config(bg="white")
b.pack()

b1=tk.Button(frame,text="SIGNUP",command=sig)
b1.config(bg="white")
b1.pack()

b2=tk.Button(frame,text="EXIT",command=r.quit())
b2.config(bg="white")
b2.pack()



r.mainloop()


# In[14]:





# In[ ]:




