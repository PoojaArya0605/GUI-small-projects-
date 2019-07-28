import tkinter as tk
from tkinter import ttk
#here we adding scolledtext widgets it is much larger then simple text vidgets
from tkinter import scrolledtext
from tkinter import Menu
win=tk.Tk()
win.title("python gui")
"""ttk.Label(win,text='my gui first page').grid(column=0,row=0)"""

#win resizable(0,0)
aLabel=ttk.Label(win,text='A Label')
aLabel.grid(column=0,row=0)

#notifying button click function
def clickMe():
    action.configure(text="hi "+ name.get()+" !! This is your window "+" "+ numberChosen.get()) #"""to add number in you outut"""
ttk.Label(win,text="Enter name :").grid(column=0,row=1)

#adding textbook entry widget
name=tk.StringVar()
nameEntered=ttk.Entry(win,width=12,textvariable=name)
nameEntered.grid(column=1,row=1)

    
action=ttk.Button(win,text="click me ",command=clickMe)
action.grid(column=0,row=3)



ttk.Label(win,text="Chose the number:").grid(column=0,row=0)
number=tk.StringVar()
numberChosen=ttk.Combobox(win,width=12,textvariable=number, state="readonly")
numberChosen['values']=[1,2,3,4,64]
numberChosen.grid(column=1,row=0)
numberChosen.current(0)
#action.configure(state="disabeled")

#action.configure(state="disabeled")
chVarDis=tk.IntVar()
check1=tk.Checkbutton(win,text="Disabled",variable=chVarDis,state='disabled')
check1.select()
check1.grid(column=0,row=4,sticky=tk.W)

chVarUn=tk.IntVar()
check2=tk.Checkbutton(win,text="unChecked",variable=chVarUn)
check2.deselect()
check2.grid(column=1,row=4,sticky=tk.W )#means the widget will be aligned to west side

chVarEn=tk.IntVar()
check3=tk.Checkbutton(win,text="Enabled",variable=chVarEn)
check3.select()
check3.grid(column=2,row=4,sticky=tk.W,columnspan=3)
COLOR1='Blue'
COLOR2='Red'
COLOR3='Green'

def radCall():
    radSel=radVar.get()
    if   radSel == 1: win.configure(background=COLOR1)
    elif radSel == 2: win.configure(background=COLOR2)
    elif radSel == 3: win.configure(background=COLOR3)
    #create three radiobutton using one variable
radVar=tk.IntVar()
rad1=tk.Radiobutton(win,text=COLOR1,variable=radVar,value=1,command=radCall)
rad1.grid(column=0,row=5,sticky=tk.W,columnspan=3)
rad2=tk.Radiobutton(win,text=COLOR2,variable=radVar,value=2,command=radCall)
rad2.grid(column=1,row=5,sticky=tk.W,columnspan=3)

rad3=tk.Radiobutton(win,text=COLOR3,variable=radVar,value=3,command=radCall)
rad3.grid(column=2,row=5,sticky=tk.W,columnspan=3)
#using a scolled text context
scrolW=50# definig scroll text height and width
scrolH=2
src=scrolledtext.ScrolledText(win,width=scrolW,height=scrolH,wrap=tk.WORD)#wrap=tk.word by sending a wrap property totk.word 
src.grid(column=0,columnspan=3)

menuBar=Menu(win)
win.config(menu=menuBar)
fileMenu=Menu(menuBar,tearoff=0)

fileMenu.add_command(label="start")
#  fileMenu.add_command(label="Exit")
#fileMenu.add_separator()
fileMenu.add_cascade(label="file",menu=fileMenu)
nameEntered.focus()
#place cursor into name entry
#src.focus()
#action.configure(state="disabeled")
win.mainloop()
