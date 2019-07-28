import tkinter as tk
from tkinter import ttk
#here we adding scolledtext widgets it is much larger then simple text vidgets
from tkinter import scrolledtext
from tkinter import Menu
win=tk.Tk()
win.title("python gui")
"""ttk.Label(win,text='my gui first page').grid(column=0,row=0)"""
tabControl=ttk.Notebook(win)
tab1=ttk.Frame(tabControl)
tabControl.add(tab1,text='Tab1')
tab2=ttk.Frame(tabControl)
tabControl.add(tab2,text='Tab2')
tabControl.pack(expand=1,fill='both')
#~~Tab control introduced here
pooja =ttk.LabelFrame(tab1,text='pooja python')
pooja.grid(column=0,row=0,padx=8,pady=4)
ttk.Label(pooja,text="Enter the name :").grid(column=0,row=0,sticky='W')


#win resizable(0,0)
aLabel=ttk.Label(tab1,text="    ")
aLabel.grid(column=0,row=0)

#notifying button click function
def clickMe():
    action.configure(text="hi "+ name.get()+" !! This is your window "+" "+ numberChosen.get()) #"""to add number in you outut"""
ttk.Label(win,text="Enter name :").grid(column=0,row=1)

#adding textbook entry widget
name=tk.StringVar()
nameEntered=ttk.Entry(tab1,width=12,textvariable=name)
nameEntered.grid(column=1,row=1)

    
action=ttk.Button(tab1,text="click me ",command=clickMe)
action.grid(column=0,row=3)



ttk.Label(tab2,text="Chose the number:").grid(column=0,row=0)
number=tk.StringVar()
numberChosen=ttk.Combobox(tab2,width=12,textvariable=number, state="readonly")
numberChosen['values']=[1,2,3,4,64]
numberChosen.grid(column=1,row=0)
numberChosen.current(0)

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
