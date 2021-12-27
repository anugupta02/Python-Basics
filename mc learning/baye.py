#Question on Naive Baye's Algorithm:
#For the given dataset,Apply Naive-Baye's Algorithm and Predict
#the outcome for a Car={Red,Domestic,SUV}
#To find out the Probability in ML, there were 2 methods:
#1. Gaussian MV
#2. Multinomial  Naive-Baye
#Python 
#Data Science
#Deep learning
#Machine Learning
#Django
#load the iris dataset
'''
Data ko regression format main kaise krna hai
'''
from sklearn.datasets import load_iris
iris=load_iris()

#store the feature matrix(X) and response vector (y)
#X is data and y is Target

X=iris.data
y=iris.target

#print(y)
#splitting X and y into training and testing sets
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=1)

#training the model on training set
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X_train,y_train)
import pandas as pd
test=[[4.6,3.4,1.4,0.3]]
testdata=pd.DataFrame(test)
#making predictions on the testing set
y_pred=gnb.predict(X_test)
print(y_pred)
myp=gnb.predict(testdata) #myp is make ur predictions
print('Test',myp)
#comparing actual response value (y_test) with predicted response values(y_pred)
from sklearn import metrics
print("Gaussian Naive Bayes model accuracy(in %): ",metrics.accuracy_score(y_test, y_pred))

#load the iris dataset
df=pd.read_csv('C:\\Users\\anugu\\iris.csv',names=['SL','SW','PL','PW','C'])
#store the feature matrix (X) and response vector (y)
X=df.iloc[:,0:4]
y=df['C']
print(y)
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=1)


