#KNN: k-nearest neighbors (KNN) algorithm is a simple,
#supervised machine learning algorithm that can be used to solve 
#both classification and regression problems.

'''

Manhanton
Equlidean Distance
Hamilton Distance
'''

'''
Python Algorithm Steps for Execution:
1. Import Libraries
2. Divide Data by trained test split
3. Create object of algorithm
4. Trained to machine
5. Predict the outcome
6. Print the score

'''

import pandas as pd

data=pd.read_csv('C:\Users\anugu\fruit.csv',names=['I','S','C','T'])
data.head()

x=data.iloc[:,1:3]
y=data['T']

#Point to be noted while writing program:
#a) test_size : by default 80:20 ke ratio main leta hai
#b) random_state agar define ya assign nhi karoge toh at random khi se bhi data fetch kar lega

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=1)
knn.fit(x,y)
tdata=[[6,4]]
test=pd.DataFrame(tdata)
knn.predict(test)

