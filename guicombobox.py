from tkinter import *
win=Tk()
win.title("python gui")
"""ttk.Label(win,text='my gui first page').grid(column=0,row=0)"""

#win resizable(0,0)
aLabel=Label(win,text='A Label')
aLabel.grid(column=0,row=0)

#notifying button click function
def clickMe():
    action.configure(text="hi "+ name.get()+" !! This is your window "+" "+ numberChosen.get()) #"""to add number in you outut"""
Label(win,text="Enter name :").grid(column=0,row=1)


#adding textbook entry widget
name=tkinter.StringVar()
nameEntered=Entry(win,width=12,textvariable=name)
nameEntered.grid(column=1,row=1)

    
action=Button(win,text="click me ",command=clickMe)
action.grid(column=0,row=3)


Label(win,text="Chose the number:").grid(column=0,row=0)
number=tkinter.StringVar()
numberChosen=Combobox(win,width=12,textvariable=number, state="readonly")
numberChosen['values']=[1,2,3,4,64]
numberChosen.grid(column=1,row=0)
numberChosen.current(0)
action.configure(state="disabeled")
nameEntered.focus()#place cursor into name entry
#action.configure(state="disabeled")
win.mainloop()
