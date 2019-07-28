from tkinter import*
win=Tk()
win.geometry('500x500')

win.title('my calculator')
c=Canvas(win,bg='red',height=500,width=500,cursor='pencil')
c.pack()
id1=c.create_line(90,98,150,10,215,120,width=4,fill='black')
id2=c.create_oval(90,60,210,190,width=4,fill='green',activefill='red',outline='black')
id1=c.create_line(150,140,150,120,width=4,fill='black')
id=c.create_oval(110,95,110,95,width=4,fill='green',activefill='red',outline='black')
id=c.create_oval(190,100,190,100,width=4,fill='green',activefill='red',outline='black')
#id=c.create.dot(90,100,width=3,fill='black')
win.mainloop()
