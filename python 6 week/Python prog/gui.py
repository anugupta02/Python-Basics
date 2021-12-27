from tkinter import *
root=Tk()
root.title("Hello")
root.geometry("500*500")
root.configure(bg="red")

l1 = Label(text ="Demo TEXT",font=('bold',20))
#l1.pack(side="bottom")
#l1.pack(anchor="se")

#l1.grid(row=0,column=5)   #it is used to make gui responsive

l1.place(x=500,y=300)
'''
pack --> side
grid --> row,column
place --> axiz
'''
root.mainloop()