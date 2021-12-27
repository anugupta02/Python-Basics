import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree


balance_data = pd.read_csv('iris2.csv', header = None) 
print("Dataset Length:: ", len(balance_data))
print("Dataset Shape:: ", balance_data.shape)

print("Dataset:: ")
balance_data.head()

X=balance_data.values[:,1:5]
Y=balance_data.values[:,0]
X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=100)
print(X_train.shape)

clf_gini=DecisionTreeClassifier(criterion="gini",max_depth=3,min_samples_leaf=5)
clf_gini.fit(X_train,y_train)

clf_entropy=DecisionTreeClassifier(criterion="entropy",max_depth=3,min_samples_leaf=5)
clf_entropy.fit(X_train,y_train)

clf_gini.predict([[4,4,3,3]])
clf_entropy.predict([[4,4,3,3]])

y_pred=clf_gini.predict(X_test)
print(y_pred)

y_pred_en=clf_entropy.predict(X_test)
print(y_pred_en)

print("Accuray is",accuracy_score(y_test,y_pred))
print("Accuray is",accuracy_score(y_test,y_pred_en))
