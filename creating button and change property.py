#notresizable
import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title("python gui")
"""ttk.Label(win,text='my gui first page').grid(column=0,row=0)"""
aLabel=ttk.Label(win,text='my gui first page')
aLabel.grid(column=0,row=0)
def clickMe():
    action.configure(text="**i have clicked**")
    aLabel.configure(foreground='red')
    aLabel.configure(text='A red label')
    
action=ttk.Button(win,text="click Me ",command=clickMe)
action.grid(column=1,row=0)
win.mainloop()
