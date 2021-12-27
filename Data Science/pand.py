

#Regression:--> Pandas Full Form is Panel Data

import pandas as pd

#s=pd.Series(data,index,copy,dtype)

#s=pd.Series([11,22,33,45],index=['a','b','c','d'])

s=pd.Series(5,index=[1,2,3,4,5],dtype=np.float16)
#print(s)

student=[('Ram',23),('Mohan',34),('Sohan',31)]
df=pd.DataFrame(student,columns=['Name','Age']
#print(df)

#data=pd.read_csv('ddata.csv',names=['Name','Age','Salary'])
#print(data)
#print(data.head())
#print(data.head(3))
#print(data.tail())

#data=pd.read_excel('demod.xlsx',names=['Name','Age','Salary'])
#print(data.head())

data=pd.read_excel('ddata.tsv',names=['Name','Age','Salary'],sep='\t')
print(data.head())
print(data['Name'])
print(data[['Name','age']])
print(data.iloc[2:5,1:3])



