import pandas as pd

data = pd.read_csv("C:\\Users\\anugu\\Book1.csv")

print(data.head())

x=data.iloc[:,0:1]
print(x,iloc[0])
print(len(x))
print(data.iloc[0,2])


for i in range(len(x)):
    if x,iloc[i]%2==0:
	   data.iloc[i,2]='Even'
	else:
	   data.iloc[i,2]='Odd'
print(data.head())

'''
data.to_csv('C:/Users/anugu/Book1final.csv')

l1=[]
l2=[]
for x in range(len(data)):
    if data.iloc[x,2]=='Odd':
        l1.append(data.iloc[x,0:3])
    else:
        l2.append(data.iloc[x,0:3])

	   
l1=pd.DataFrame(l1)
l2=pd.DataFrame(l2)

l1.to_csv('odd.csv')
l2.to_csv('even.csv')


df.head()
type(d1)


form bs4 import BeautifulSoup
'''