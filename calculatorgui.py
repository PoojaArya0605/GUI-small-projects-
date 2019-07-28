from tkinter import*
from flask import Flask
app=Flask(__name__)
win=Tk()
expression=''
win.title(" SIMPLE CALCULATOR")
win.geometry('400x300')
@app.route('/abc/')
def e1(event):
    global expression
    s1=e.get()
    s1=str(s1)
    expression=s1
    equalpress()
@app.route('/abc/')    
def click(n):
    global expression
    expression=expression+str(n)
    s.set(expression)
@app.route('/abc/')    
def equalpress():
    try:
        global expression
        total=str(eval(expression))
        s.set(total)
        expression=''
    except:
        s.set("Error")
s=StringVar()
e=Entry(win,textvariable=s)
e.bind('<Return>',e1)
e.grid(rowspan=2,columnspan=4,ipadx=137)
e.focus()
b1=Button(win,text='1',fg='black',bg='blue'
          ,width=13,height=4,command=lambda: click(1)).grid(row=2,column=0)
b2=Button(win,text='2',fg="black", bg="blue",width=13,height=4,command=lambda: click(2)).grid(row=2,column=1)
b3=Button(win,text='3',fg="black", bg="blue",width=13,height=4,command=lambda: click(3)).grid(row=2,column=2)
b4=Button(win,text='4',fg="black", bg="blue",width=13,height=4,command=lambda: click(4)).grid(row=3,column=0)
b5=Button(win,text='5',fg='black',bg='blue',width=13,height=4,command=lambda: click(5)).grid(row=3,column=1)
b6=Button(win,text='6',fg='black',bg='blue',width=13,height=4,command=lambda: click(6)).grid(row=3,column=2)
b7=Button(win,text='7',fg='black',bg='blue',width=13,height=4,command=lambda: click(7)).grid(row=4,column=0)
b8=Button(win,text='8',fg='black',bg='blue',width=13,height=4,command=lambda: click(8)).grid(row=4,column=1)
b9=Button(win,text='9',fg='black',bg='blue',width=13,height=4,command=lambda: click(9)).grid(row=4,column=2)
b0=Button(win,text='0',fg='black',bg='blue',width=13,height=4,command=lambda: click(0)).grid(row=5,column=1)
plus=Button(win,text='+',fg="black", bg="green",width=13,height=4,command=lambda:click('+')).grid(row=2,column=3)
minus=Button(win,text='-',fg="black", bg="green",width=13,height=4,command=lambda:click('-')).grid(row=3,column=3)
plus=Button(win,text='*',fg="black", bg="green",width=13,height=4,command=lambda:click('*')).grid(row=4,column=3)
divide=Button(win,text='/',fg="black", bg="green",width=13,height=4,command=lambda:click('/')).grid(row=5,column=2)
point=Button(win,text='.',fg="black", bg="green",width=13,height=4,command=lambda:click('.')).grid(row=5,column=0)
equal=Button(win,text='=',fg="black", bg="green",width=13,height=4,command=equalpress).grid(row=5,column=3)
#backspace=button(win,text='<-',command=lambda:click(<-)).grid(row=4,column=3)
if __name__=="__main__":
    app.run(debug=True)
win.mainloop()
