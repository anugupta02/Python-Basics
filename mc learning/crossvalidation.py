from sklearn.datasets import load_iris
iris=load_iris()
X=iris.data
y=iris.target

from sklearn.model_selection import cross_val_score
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn import linear_model
from sklearn.neighbors import KNeighborsClassifier

print(cross_val_score(LinearSVC(),X,y,cv=5))
print(cross_val_score(DecisionTreeClassifier(),X,y,cv=5))
print(cross_val_score(KNeighborsClassifier(),X,y,cv=5))
print(cross_val_score(linear_model.LinearRegression(),X,y,cv=5))

print(cross_val_score(LinearSVC(),X,y,cv=5,scoring="f1_macro"))

#restricted to the binary classification task or multilabel classify

print(cross_val_score(LinearSVC(),X,y%2,cv=5,scoring="roc_auc"))

