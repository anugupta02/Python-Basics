import pandas as pd
features = pd.read_csv('C:\\Users\\anugu\\temps.csv')
features.head(5)

print('The shape of our features is: ',features.shape)

print(features.describe())#One-hot encode the data using pandas get_dumies
features=pd.get_dummies(features)
#Dummies work: Convert categorical variable into dummy/indicator variables
#Display the first 5 rows of the last 12 columns
features.iloc[:,5:].head(5)

import numpy as np
labels=np.array(features['actual'])
#Remove the labels from the features
#axis 1 refers to the columns
features=features.drop('actual',axis=1)
#Saving feature names for later use
feature_list=list(features.columns)
#Convert to numpy array
features = np.array(features)

#Using Skicit-learn to split data into training and testing sets
from sklearn.model_selection import train_test_split
#Split the data into training and testing sets
train_features, test_features,train_labels,test_labels=train_test_split(
features,labels,test_size=0.25,random_State=42)

#random_state means ek position le lia jha se data uthana start karega.

print('Training Features Shape:',train_features.shape)
print('Training Labels Shape:',train_labels.shape)
print('Testing Features Shape:',test_features.shape)
print('Testing Labels Shape:',test_labels.shape)


#The baseline predictions are the historical averages
baseline_preds = test_features[:,feature_list.index('average')]
#Baseline errors, and display average baseline error
baseline_errors=abs(baseline_preds - test_labels)
print('Average baseline error: ',round(np.mean(baseline_errors),2))
#round means what precision would u like to show in decimals

#Import the model we are using
from sklearn.ensemble import RandomForestRegressor
#Instantiate model with 1000 decision trees
rf=RandomForestRegressor(n_estimators=1000,random_state=42)
#Train the model on training data
rt.fit(train_features,train_labels)

#Use the forest's predict method on the test data 
predictions=rf.predict(test_features)
print(predictions)
#Calculate the absolute errors
errors = abs(predictions - test_labels)

#Print out the mean absolute percentage error(MAPE)
mape=100*(errors/test_labels)
#Calculate and display accuracy
accuracy=100-np.mean(mape)
print('Accuracy: ',round(accuracy,2),'%.')




