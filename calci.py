from tkinter import *
import tkinter
import tkinter.messagebox

def proces():
    t1=Entry.get(E1)
    t2=Entry.get(E2)
    op=Entry.get(E3)
    if op=="-":
        ans=int(t1)-int(t2)
        tkinter.messagebox.showinfo( "Answer", ans)
    if op=="+":
        ans=int(t1)-int(t2)
        tkinter.messagebox.showinfo("Answer", ans)
    if op=="/":
        ans=int(t1)/int(t2)
        tkinter.messagebox.showinfo("Answer", ans)
    if op=="*":
        ans=int(t1)*int(t2)
        tkinter.messagebox.showinfo("Answer", ans)
    

top = tkinter.Tk()
top.title("Calulator")
L2 = Label(top, text="Value1",).grid(row=1,column=1)
E1 = Entry(top, bd =5)
E1.grid(row=2,column=1)
L3 = Label(top, text="value2",).grid(row=3,column=1)
E2 = Entry(top, bd =5)
E2.grid(row=4,column=1)
L4 = Label(top, text="operator",).grid(row=5,column=1)
E3 = Entry(top, bd =5)
E3.grid(row=6,column=1)
B=Button(top, text ="Submit",command = proces).grid(row=7,column=1,)

top.mainloop()