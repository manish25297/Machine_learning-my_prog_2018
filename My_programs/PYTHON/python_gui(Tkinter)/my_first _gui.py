from Tkinter import *
window = Tk()

window.title("Calculator")
window.geometry('360x480')
window.configure(background = 'blue')

enterPrompt=Label(window, text="enter 1st value")
enterPrompt.grid(column=0, row=0)

rollLablel = Entry(window,width=5)
rollLablel.grid(column=1,row=0)
rollLablel.focus()

enterPrompt1=Label(window, text="enter 2nd value")
enterPrompt1.grid(column=0, row=25)

rollLablel2 = Entry(window,width=5)
rollLablel2.grid(column=1,row=25)
rollLablel2.focus()

show=Label(window,text='')
show.grid(column=361, row=360)

def clicked():
    rollNumber = rollLablel.get()
    rollNumber=int(rollNumber)

    rollNumber2 = rollLablel2.get()
    rollNumber2=int(rollNumber2)
    c=rollNumber+rollNumber2
    c=str(c)

    show.configure(text=c)

    window.configure(background = 'red')
    window.title("calculated")
    #also change other attributes
    #h.sw calculator like windows

    
btn = Button(window, text="Enter", bg = "#2196F3", command=clicked)
btn.grid(column=36, row=360)



window.mainloop()
