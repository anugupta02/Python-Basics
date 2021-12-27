import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error,r2_score

#Load the diabetes dataset
diabetes=datasets.load_diabetes()
print(diabetes.keys())
print(diabetes.DESCR)
#Use only one feature
print(np.newaxis)
diabetes_X=diabetes.data[:,np.newaxis,2]
 #data se sara row lele aur newaxis se
 
 print(diabetes_X)
 
 #Split the data into training/testing sets
 diabetes_X_train = diabetes_X[:-20]
 diabetes_X_test = diabetes_X[-20:]
 #Create Linear regression object
 regr = linear_model.LinearRegression()
 #Train the model using the training sets
 regr.fit(diabetes_X_train,diabetes_y_train)
 #Make predictions using the testing set
 diabetes_y_pred = regr.predict(diabetes_X_test)
 #The coefficients
 print('Coefficients: \n', regr.coef_)
 #The mean squared error
 #print('Intercept: \n',regr)
 
 print("Mean squared error: %.2f")