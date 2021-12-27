import  pandas as pd
#data=pd.read_csv('iris.csv',names=['sepal length','sepal width','petal length','petal width','spacies'])
#print(data.head())

#print(data.groupby('spacies').count())
#print(data.groupby('spacies').sum())

#Describe function is used to descibe data of the table in file
#data.describe()
#data.mean()
#data.spd()

#Simple describe gives whole data that is contains in the file
#data.describe
#data[['sepal length','petal width']]
#data.info()
#data.describe(include='all')
#Nan means not a number
#frequency means 0 or 1
#data.isna()

df=pd.read_csv('C:/Users/anugu//test.csv')#,header=None,skiprows=1)

#print(df.head())
#print(df.isna().count())
#print(df.isna().sum())
#df.ffill(inplace=True) #ffill means First Fill joh bhi blank data hai uske phele vale data ki value se fill krdo
#df.dropna(thresh=2,inplace=True)

#print(df.head())
#print(df.isna())
# 3 Types of functions for drop
#1. drop
#2. dropna
#3. drop_duplicates

#df.dropna(inplace=True)
#print(df.head(10))

#print(df.drop_duplicates())
#print(df.Name)

# 2 methods:
# a) loc means data ki value name se denge jabki iloc index ke according value denge data ki
#loc gets rows (or columns) with particular labels from the index.
# b)iloc means index location and first : means all rows
#iloc gets rows (or columns) at particular positions in the index (so it only takes integers).It usually tries to behave like loc but falls back to behaving like iloc if a label is not present in the index.
#print(df.iloc[:,1:3])
print(df.loc[:,'Age'])
