from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

digits=load_digits()
#print(digits.data)
#print(digits.target)
X_train,X_test,y_train,y_test=train_test_split(digits.data,digits.target,test_size=0.2,random_state=2)
print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(X_test.shape)

import numpy as np
para_grid={'C':5.** np.arange(-3,3),'gamma':5.** np.arange(-5,0)}
#** means power 5 ka square in python

grid_search=GridSearchCV(SVC(),para_grid,cv=5)
grid_search.fit(X_train,y_train)
grid_search.predict(X_test)
grid_search.score(X_test,y_test)
grid_search.best_params_

