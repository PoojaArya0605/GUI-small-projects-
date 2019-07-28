#notresizable
import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title("python gui")
ttk.Label(win,text='my gui first page').grid(column=0,row=0)

win.mainloop()
