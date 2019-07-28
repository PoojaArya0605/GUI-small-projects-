import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
win=tk.Tk()
win.title("python firstGUI")
aLabel=ttk.Label(win,text="gui page")
aLabel.grid(column=0,row=0)
Label(Label,text="first").grid(row=0,sticky='s')
Label(Label,text="second").grid(row=1,sticky='e')
e1=Entry(Label)
e2=Entry(Label)
e1.grid(column=0,row=0)
e2.grid(column=1,row=0)
Label1.grid(sticky=E)
Label2.grid(sticky=E)
entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
checkbuttton.grid(columnspan=2,sticky='W')
image.grid(row=0,column=2,columnspan=2,rowspan=2,sticky=W+E+S+N,padx=5,pady=5)
butoon1.grid(row=2,column=2)
butoon2.grid(row=2,column=3)


win.mainloop()
