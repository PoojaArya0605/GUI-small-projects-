from tkinter import*
win=Tk()
win.title("mini calc")
L1=Label(win,text="Number(kg)")
L1.grid(row=0,column=0)
L2=Label(win,text="(ounces)")
L2.grid(row=1,column=0)
L3=Label(win,text="(grams)")
L3.grid(row=3,column=0)
L4=Label(win,text="(pounds)")
L4.grid(row=4,column=0)

number=IntVar()
e1=Entry(win,textvariable=number)
e1.grid(row=0,column=1)
t1=Text(win,height=1,width=20)
t1.grid(row=1,column=1)
t2=Text(win,height=1,width=20)
t2.grid(row=3,column=1)
t3=Text(win,height=1,width=20)
t3.grid(row=4,column=1)
def calculate():
    try:
        print(number.get())
        ounces = float(number.get())*35.274
        t1.insert(END,ounces)
        
        grams=(number.get())*1000
        t2.insert(END,grams)
        print(grams)
        pounds=(number.get())*2.20462
        t3.insert(END,pounds)
        print(pounds)
    except AttributeError:
        print("insert mistake")
b1=Button(win,text="Enter",command=calculate)
b1.grid(row=5,column=0)
win.mainloop()
