from tkinter import *
from tkinter import messagebox as msg

class Knn(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.lbl1=Label(self,text='Wieght',font=('lucida 10 bold'))
        self.lbl1.grid(row=1,column=1)
        
        self.lbl2=Label(self,text='Height',font=('lucida 10 bold'))
        self.lbl2.grid(row=2,column=1)
        
        self.txt1=Entry(self,font=('arial 10 italic'))
        self.txt1.grid(row=1,column=2)
        
        self.txt1=Entry(self,font=('arial 10 italic'))
        self.txt1.grid(row=2,column=2)
        
        self.btn=Button(self,text='Predict',command=self.show)
        self.btn.grid(row=3,column=1,columnspan=2)
        self.pack()
    def show(self):
        weight=float(self.txt1.get())
        height=float(self.txt2.get())
        testdata=[[weight,height]]
        check=pd.DataFrame(testdata)
        dis=kobj.predict(check)
        msg.showinfo('The Human Is:-',dis)
        
root=Tk()
obj=Knn(root)
root.geometry('200x250')
root.mainloop()