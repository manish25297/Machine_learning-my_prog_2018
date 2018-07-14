

from Tkinter import *                        #importing Tkinter lib
w1 = Tk()                                     # making object w1 for making window


w1.title("Calculator")                            #giving a title to out window
w1.geometry('360x480')                          #specifying the size of the window
w1.configure(background = 'blue')                #  choosing the window background color,we can also use "bg" shortform instead of background

line_print=Label(w1, text="enter 1st value")      
line_print.grid(column=0, row=0)

line_input= Entry(w1,width=25)                           #w1 = specifying window (optional)no need to specify when single window, text = giving output (optional)
line_input.grid(column=1,row=0)
line_input.focus()                                      #automatically brings the pointer to the textbox,input box at start

line_print1=Label(w1, text="enter 2nd value")               #w1 = specifying window (optional), text = giving output or print data (optional)
line_print1.grid(column=0, row=2)

line_input2 = Entry(w1,width=25)
line_input2.grid(column=1,row=2)
#line_input2.focus()

line_print3=Label(w1,text='result',width=10)        #w1 = specifying window (optional), text = giving output(optional), width= setting width(optional)
line_print3.grid(column=0, row=360)

line_print4=Label(w1,text='',width=25)
line_print4.grid(column=1, row=360)

def sum1():                                           #this function is called when the button named sum is clicked 
    rollNumber = line_input.get()
    rollNumber=int(rollNumber)

    rollNumber2 = line_input2.get()
    rollNumber2=int(rollNumber2)
    c=rollNumber+rollNumber2
    c=str(c)

    line_print4.configure(text= c)                           # text= print data, giving output
    
    line_print.configure(background = 'red')
    line_print1.configure(background = 'red')
    w1.configure(background = 'red')
    w1.title("calculated")
    #also change other attributes
    #h.sw calculator like windows
def sub():
    rollNumber = line_input.get()
    rollNumber=int(rollNumber)

    rollNumber2 = line_input2.get()
    rollNumber2=int(rollNumber2)
    c=rollNumber-rollNumber2
    c=str(c)

    line_print4.configure(text=c)
    
    line_print.configure(background = 'red')
    line_print1.configure(background = 'red')
    w1.configure(background = 'red')
    w1.title("calculated")
def mul():
    rollNumber = line_input.get()
    rollNumber=int(rollNumber)

    rollNumber2 = line_input2.get()
    rollNumber2=int(rollNumber2)
    c=rollNumber*rollNumber2
    c=str(c)

    line_print4.configure(text=c)
    line_print.configure(background = 'red')
    line_print1.configure(background = 'red')
    w1.configure(background = 'red')
    w1.title("calculated")
def div():
    rollNumber = line_input.get()
    rollNumber=int(rollNumber)

    rollNumber2 = line_input2.get()
    rollNumber2=int(rollNumber2)
    c=rollNumber/rollNumber2
    c=str(c)

    line_print4.configure(text=c)
    
    line_print.configure(background = 'red')
    line_print1.configure(background = 'red')
    w1.configure(background = 'red')
    w1.title("calculated")
    
btn = Button(w1, text="sum", bg = "silver", command=sum1,width=10)      #creating button w1=window(optionL),text= replacement of print(optionL),
btn.grid(column=0, row=4)                                                #bg=backgroud color(optional),command= calling function (optianL.),width=optional

btn = Button(w1, text="sub", bg = "silver", command=sub,width=10)
btn.grid(column=3, row=4)

btn = Button(w1, text="mul", bg = "silver", command=mul,width=10)
btn.grid(column=0, row=6)

btn = Button(w1, text="div", bg = "silver", command=div,width=10)
btn.grid(column=3, row=6)



line_print.configure(bg = 'blue')
line_print1.configure(bg = 'blue')

w1.mainloop()                                                            #for iterative or repetetive operation so, that the window appears static
