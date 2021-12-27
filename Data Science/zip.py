'''
notepad prog
login/register prog
overload_prog
generator prog
'''

'''
Zip Funcrion in python:

li = ['Ram','Shyam','Mohan','Anu']
l2=[22,23,45]
for x,y in zip(*(li,l2)):
    print(x,y)
'''

import pandas as pd
index = pd.MultiIndex.from_tuples(tuples,names=['first','second'])
index

df = pd.DataFrame(np.random.randn(8,2), index=index, 
                  columns['A','B'])
df

stacked = df2.stack()