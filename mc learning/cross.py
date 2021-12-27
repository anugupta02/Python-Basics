#cross validation
#OverFit if greater than 50
#UnderFit if lessthan 50 
import pandas as pd

pd.read_csv('C:\Users\anugu\gender1.csv',names=['gender','weight','height'])
data.head()

#x=data.iloc[:,1:3]
#y=data.drop(1:3,axis=1)


y=data[['gender']]
x=data.drop('gender',axis=1)

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2,random_state=2)
#when we change random_state then it will effect score number not final result


print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)


from sklearn.neighbors import KNeighborsClassifier

kobj=KNeighborsClassifier(n_neighbors=7)
#Train the System
kobj.fit(x_train,y_train)

pred=kobj.predict(x_test)
print(pred)

testdata=[[76,178]]
test=pd.DataFrame(testdata)
#Result is male

testdata=[[53,167.64]]
test=pd.DataFrame(testdata)
#Result is female

print(kobj.predict(test))

from sklearn.metrics.import accuracy_score

print(accuracy_score(pred,y_test))

from tkinter import *
from tkinter import messagebox as msg 

class Knn(Frame):
    def __init__(self,master):
	    super().__init__(master)
		self.l1=Label(self,text='Weight',font('algerian',12),bd=8,fg='lightblue')
		self.l1=Label(self,text='Height',font('algerian',12),bd=8,fg='lightblue',command=self.show)
		#bd : border , fg : foreground
		self.rowconfigure(index=0,pad=10)
		self.rowconfigure(index=1,pad=10)
		self.columnconfigure(index=0,pad=10)
		self.columnconfigure(index=1,pad=10)
		
		
	    self.l1.grid(row=1,column=0)
	    self.t1.grid(row=1,column=1)
		
		self.l2.grid(row=2,column=0)
	    self.t2.grid(row=2,column=1)
		
		self.b1.grid(columnspan=2)
		self.pack()
		
	def show(self):
	    w=float(self.t1.get())
	    h=float(self.t2.get())
		tdata=[[w,h]]
		test=pd.DataFrame(tdata)
		output=kobj.predict(test)
		msg.showinfo('Prediction',output)

root=Tk()
ob=Knn(root)
root.geometry('350*250')
root.mainloop()


		
		
		
		
		
		