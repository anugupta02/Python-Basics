import pandas as pd
data=pd.read_csv('iris.csv',names=['sepal length','sepal width','petal length', 'peatl width','species'])
print(data.head())