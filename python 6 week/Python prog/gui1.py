from tkinter import *
r = Tk()
q = TK()
r.title("Hello")
r.geometry("500*500")
r.configure(bg="red")

l1 = Label(r,text ="Demo TEXT",font=('bold',20))
l2 = Label(q,text ="Label TEXT",font=('bold',20))
#l1.pack(anchor="se")
l1.place(x=300,y=300)
l2.place(x=0,y=0)
r.mainloop()