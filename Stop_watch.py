import tkinter as tk
r = tk.Tk()
running = False
hh = mm = ss = "00"
def counter(label):
    def count():
        global hh,mm,ss
        hh = int(hh) 
        mm = int(mm)
        ss = int(ss)
        if running:
            label['text'] = f'{str(hh).zfill(2)}:{str(mm).zfill(2)}:{str(ss).zfill(2)}'
            label.after(1000,count)
            ss+=1
            if ss == 60:
                mm+=1
                if mm == 60:
                    hh+=1 
    count()         
def sta_t(label):
    global running
    running = True
    counter(label)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'
def st_p():
    global running 
    running = False
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
def res_t(label):
    global running,hh,mm,ss
    hh = mm = ss = "00"
    label['text'] = f"{hh}:{mm}:{ss}"
    if running == False:
        start['state'] = 'normal'
        stop['state'] = 'disabled'
        reset['state'] = 'disabled'
    else:
        running = False
        start['state'] = 'normal'
        stop['state'] = 'disabled'
        reset['state'] ='disabled'
        
label = tk.Label(r,text=f'{hh}:{mm}:{ss}',bg="white",fg ="black", font=('times',30,'bold'))
label.pack(side=tk.TOP,padx=10,pady=20)

start = tk.Button(r,text="START",width=5,fg="white",bg="black",font=('times',15,'bold'),command=lambda:sta_t(label))
start.pack(side=tk.TOP,padx=10,pady=10,ipadx=2,ipady=2)

stop = tk.Button(r,text="STOP",width=5,fg="white",bg="black",state="disabled",font=('times',15,'bold'),command=st_p)
stop.pack(side=tk.TOP,padx=10,pady=10,ipadx=2,ipady=2)

reset = tk.Button(r,text="RESET",width=5,fg="white",bg="black",state="disabled",font=('times',15,'bold'),command=lambda:res_t(label))
reset.pack(side=tk.TOP,padx=10,pady=10,ipadx=2,ipady=2)
r.config(bg="white")
r.wm_minsize(400,300)
r.wm_maxsize(400,300)
r.iconbitmap('stop_watch.ico')
r.title('STOP-WATCH')
r.mainloop()
