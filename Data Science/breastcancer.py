import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

nam=['Id','Clump Thickness','Uniformity of Cell Size',
     'Uniformity of Cell Shape','Marginal Adhesion',
     'Single Epithelial Cell Size','Bare Nuclei',
     'Bland Chromatin',
     'Normal Nucleoli','Mitoses','Class']
data=pd.read_csv('C:/Users/anugu/breast_cancer.csv',names=nam)
print(data.shape)
print(data.head())
#print(data['Class'])

data=data.replace('?','-999')

data.head(30)
y=data.Class
print(y)

X=data.drop('Class',axis=1)
#axis=1 is applied for each row for every coloumn labels.
#axis=0 is applied for every row labels
print(X)
X_train,X_test,y_train,y_test = train_test_split(X, y,test_size=0.2,
random_state=10)
'''
random_state as the name suggests, is used for initializing the internal 
random number generator, which will decide the splitting of data into train 
and test indices in your case. In the documentation, it is stated that: If 
random_state is None or np.random, then a randomly-initialized RandomState 
object is returned.

test_size=.2 means 20% or .3 means 30%
random_state means uss no. pr joh data usne fetch(uthaya) kiya humesha vhi se lega
'''

print("\nX_train:\n")
#print(X_train.head())
print(X_train.shape)
print("\nx_test:\n")
#print(X_test.head())
print(X_test.shape)
print(y_test.shape)
print(y_train.shape)


from sklearn.neighbours import KNeighborsClassifier
lf1=KNeighborsClassifier(n_neighbours=5)

lf1.fit(X_train,y_train)
#Euclidean Distance Formula
#KNN: Distance nikalke uski value se data predict krna

from sklearn.metrics import accuracy_score

y_pred=lf1.predict(X_test)
#print('clf1:',accuracy_score(y_pred))
print(y_pred)
print(lf1.score(X_train,y_train))
lf1.score(X_test,y_test)

np.where(y_pred!=y_test)

count_b=0 #Benign and Malignant; these are 2 types of breast cancer
count_m=0
mylist=data['Class']
for x in mylist:
    if x==2:
	    count_b+=1
	else:
	   count_m+=1
count_b=(count_b/699)*100
count_m=(count_m/699)*100

print('Benign',count_b)
print('Malignant',count_m)

print('Benign is a currable cancer and it has positive result count of',count_b)
print('Malignant is a non-currable cancer and it has positive result count of',count_m)

#DharamShila Cancer Hospital in Noida it is Large Hospital for Cancer Treatment

