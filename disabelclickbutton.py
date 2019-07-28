import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title("python gui")
"""ttk.Label(win,text='my gui first page').grid(column=0,row=0)"""
#win resizable(0,0)
aLabel=ttk.Label(win,text='A Label')
aLabel.grid(column=0,row=0)
#notifying button click function
def clickMe():
    action.configure(text="hi"+name.get())
ttk.Label(win,text="Enter name :").grid(column=0,row=0)
#adding textbook entry widget
name=tk.StringVar()
nameEntered=ttk.Entry(win,width=12,textvariable=name)
nameEntered.grid(column=0,row=1)
    
action=ttk.Button(win,text="click me ",command=clickMe)
action.grid(column=1,row=1)
action.configure(state="disabeled")
nameEntered.focus()#place cursor into name entry
win.mainloop()
