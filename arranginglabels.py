#LAYOUT MANAGMENTS
import tkinter as tk
from tkinter import ttk
#here we adding scolledtext widgets it is much larger then simple text vidgets
from tkinter import scrolledtext
from tkinter import Menu

import os,sys
win=tk.Tk()
win.title("python gui")
ttk.Label(win,text='my gui first page').grid(column=0,row=0)


#notifying button click function
def clickMe():
    action.configure(text=" hi "+ name.get()+" !! This is your window "+" "+ numberChosen.get()) #"""to add number in you outut"""
ttk.Label(win,text="Enter name :").grid(column=0,row=1)
#adding textbook entry widget
name=tk.StringVar()
nameEntered=ttk.Entry(win,width=12,textvariable=name)
nameEntered.grid(column=1,row=1)



#win resizable(0,0)
aLabel=ttk.Label(win,text=" HI this is your window   ")
aLabel.grid(column=1,row=0)
    
action=ttk.Button(win,text="click me ",command=clickMe)
action.grid(column=0,row=3)


ttk.Label(win,text=" Choose the number:").grid(column=0,row=2)


number=tk.StringVar()
numberChosen=ttk.Combobox(win,width=12,textvariable=number, state="readonly")
numberChosen['values']=[1,2,3,4,5]
numberChosen.grid(column=1,row=2)
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
check2.grid(column=1,row=4,sticky=tk.N )#means the widget will be aligned to west side

chVarEn=tk.IntVar()
check3=tk.Checkbutton(win,text="Enabled",variable=chVarEn)
check3.select()
check3.grid(column=2,row=4,sticky=tk.W,columnspan=3)
COLORs=['Blue','Red','Green','gray']

def radCall():
    radSel=radVar.get()
    if   radSel == 0: win.configure(background=COLORs[0])
    elif radSel == 1: win.configure(background=COLORs[1])
    elif radSel == 2: win.configure(background=COLORs[2])
    elif radSel == 3: win.configure(background=COLORs[3])
    #create three radiobutton using one variable
radVar=tk.IntVar()
radVar.set(99)
for COL in range(4):
    curRad='rad'+str(COL)
    curRad=tk.Radiobutton(win,text=COLORs[COL],variable=radVar,value=COL,command=radCall)
    curRad.grid(column=COL,row=7,sticky=tk.W)
    #create a container to hold labels
LabelsFrame=ttk.LabelFrame(win,text="Labels in a frame")
LabelsFrame.grid(column=0,row=9)
#place label into container element
ttk.Label(LabelsFrame,text="Label1").grid(column=0,row=8)
ttk.Label(LabelsFrame,text="Label2").grid(column=0,row=9)
ttk.Label(LabelsFrame,text="Label3").grid(column=0,row=10)
for child in LabelsFrame.winfo_children():
    child.grid_configure(padx=8,pady=1)
    #creating a function for exit use 
def _quit():
    win.quit()
    win.destroy()
    exit()

menuBar=Menu(win)
win.config(menu=menuBar)

   
fileMenu=Menu(menuBar,tearoff=0)
fileMenu.add_command(label='New')
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=_quit)
menuBar.add_cascade(label='file',menu=fileMenu)

windowMenu=Menu(menuBar,tearoff=0)
windowMenu.add_command(label='New')
windowMenu.add_separator()
windowMenu.add_command(label='Type')
windowMenu.add_separator()
windowMenu.add_command(label='Size')
windowMenu.add_separator()
windowMenu.add_command(label='Exit',command=_quit)
menuBar.add_cascade(label='Window',menu=windowMenu)


formatMenu=Menu(menuBar,tearoff=0)
formatMenu.add_command(label='indent region')
formatMenu.add_separator()
formatMenu.add_command(label='dedent region')
formatMenu.add_separator()
formatMenu.add_command(label='comment on region')
formatMenu.add_separator()
formatMenu.add_command(label='format paragraph')
formatMenu.add_separator()
formatMenu.add_command(label='Exit',command=_quit)
menuBar.add_cascade(label='Format',menu=formatMenu)



nameEntered.focus()
win.mainloop()
