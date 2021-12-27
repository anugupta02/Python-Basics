import  pandas as pd
import numpy as np

dates=pd.date_range('20190924',periods=6) #yymmdd
#print(dates)


df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
#print(df)

#Classification => Categorical Datatype means char
df2=pd.DataFrame({'A' : 1.,'B' : pd.Timestamp('20190521'),
'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
'D' : np.array([3] * 4,dtype='int32'),
'E' : pd.Categorical(["test","train","test","train"]),
'F' : -1})

#print(df2)
#print(df2.dtypes)
#print(df2.index)
#print(df.index)
#print(df.columns)
#print(df.values)
#print(df.quantile()) #It brings 3 4th of the Dataframe
#print(df.T)
#print(df.sort_index(axis=1,ascending=False))
#(df.sort_index(axis=0,ascending=True))

dff=pd.DataFrame([[13,12,3],[2,3,4],[4,1,5]])
#print(dff)
#print(dff.sort_index(axis=1,ascending=False))
#print(dff.sort_index(axis=0,ascending=False))
#print(dff.sort_index(axis=0,ascending=True))

#df.at[dates[0],'A']=0
#df.at[dates[0],'B']=1
#df.at[dates[2],'C']=5
#df.iat[0,3]=7
#print(df)
#df.to_csv('C:/Users/anugu//sss.csv')

df.loc[:,'B'] = np.array([3]*len(df))
#print(df)

df2=df.copy()
#print(df2)

