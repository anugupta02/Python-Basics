from tkinter import *
from tkinter import messagebox as ms
r = Tk()
q = TK()
r.title("Hello")
r.geometry("500*500")

def sample():
    #print("in sample")
    name = e1.get()
    print("Hello",name)
    ms.showinfo("Welcome","Hello " +name)
l1 = Label(r,text ="Registration Form",font=('bold',20))
l2 = Label(q,text ="Enter Your Name",font=('bold',20))
e1=Entry(r,font=('bold',15))
b1=Button(text="Enter Here",font=(bold,15),width=10,bg="red",command=sample)
l1.place(x=140,y=50)
l2.place(x=100,y=80)
e1.place(x=270,y=150)
b1.place(x=230,y=155)
r.mainloop()