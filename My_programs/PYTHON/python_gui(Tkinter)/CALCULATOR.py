# -*- coding: utf-8 -*-
from Tkinter import *

def a():
    return 0




w=Tk()
w.title("calc")
#w.configure(background ="powder blue")
w.geometry("240x240")
self= Entry(w)
self.grid(row=0,column=0,columnspan=6,pady=10,ipadx=30,padx=10,ipady=5)
self.focus_set() #Sets focus on the input text area""

Button(w,text="=",width=8,command=a).grid(row=4, column=4,columnspan=2)
Button(w,text='AC',width=3,command=a).grid(row=1, column=4,pady=0,padx=0)
Button(w,text='C',width=3,command=a).grid(row=1, column=5,pady=0,padx=0)
Button(w,text="+",width=3,command=a).grid(row=4, column=3,pady=0,padx=0)
Button(w,text="x",width=3,command=a).grid(row=2, column=3,pady=0,padx=0)
Button(w,text="-",width=3,command=a).grid(row=3, column=3,pady=0,padx=0)
Button(w,text="÷",width=3,command=a).grid(row=1, column=3,pady=0,padx=0) 
Button(w,text="%",width=3,command=a).grid(row=4, column=2,pady=0,padx=0)
Button(w,text="7",width=3,command=a).grid(row=1, column=0,pady=0,padx=0)
Button(w,text="8",width=3,command=a).grid(row=1, column=1,pady=0,padx=0)
Button(w,text="9",width=3,command=a).grid(row=1, column=2,pady=0,padx=0)
Button(w,text="4",width=3,command=a).grid(row=2, column=0,pady=0,padx=0)
Button(w,text="5",width=3,command=a).grid(row=2, column=1,pady=0,padx=0)
Button(w,text="6",width=3,command=a).grid(row=2, column=2,pady=0,padx=0)
Button(w,text="1",width=3,command=a).grid(row=3, column=0,pady=0,padx=0)
Button(w,text="2",width=3,command=a).grid(row=3, column=1,pady=0,padx=0)
Button(w,text="3",width=3,command=a).grid(row=3, column=2,pady=0,padx=0)
Button(w,text="0",width=3,command=a).grid(row=4, column=0,pady=0,padx=0)
Button(w,text=".",width=3,command=a).grid(row=4, column=1,pady=0,padx=0)
Button(w,text="(",width=3,command=a).grid(row=2, column=4,pady=0,padx=0)
Button(w,text=")",width=3,command=a).grid(row=2, column=5,pady=0,padx=0)
Button(w,text="√",width=3,command=a).grid(row=3, column=4,pady=0,padx=0)
Button(w,text="x²",width=3,command=a).grid(row=3, column=5,pady=0,padx=0)

w.mainloop()
