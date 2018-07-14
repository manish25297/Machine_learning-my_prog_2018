from Tkinter import *
from random import choice

colors = ["red","blue","purple","yellow","white","black"]

root = Tk()
root.configure(bg="#B3E5FC")
root.title("Divyam")
root.geometry("360x480")


name = Label(root, text="Enter your Name : ",bg="#E040FB",width=40)
name.grid(row=0,column=0)

entery = Entry(root,width=40)
entery.grid(row=1,column=0)
entery.focus()

display = Label(root, text="Your name is : ",bg="#E040FB",width=40)
display.grid(row=3,column=0)


def changename():
    n = entery.get()
    display.configure(text=n)
    root.configure(bg=choice(colors))



button = Button(text="Enter",bg="#CDDC39",command=changename)
button.grid(row=2,column=0)
root.mainloop()

