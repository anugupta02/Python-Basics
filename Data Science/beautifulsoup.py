import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.hubertiming.com/results/2017GPTR10K"
html = urlopen(url)

soup = BeautifulSoup(html, 'html.parser')
type(soup)

title = soup.title
print(title)

#Print out the text
text = soup.get_text()
print(text)

soup.find_all('a')

all_links = soup.find_all("a")
for linl in all_links:
    print(link.get("href"))


#Print the first 10 rows for sanity check
rows = soup.find_all('tr')
print(rows[:10])


for row in rows:
    row_td = row.find_all('td')
    print(row_td)	
#type(row_td)
#anaconda install kar lo again

str_cells = str(row_td)
cleantext = BeautifulSoup(str_cells, "html.parser").get_text()
print(cleantext)

'''
import re
list_rows = []
for row in rows:
    cells = row.find_all('td')
	str_cells = str(cells)
	clean = re.compile('.</?\w*>')
	clean2 = (re.sub(clean, '',str_cells))
	#print(clean2)
	list_rows.append(clean2)
#print(clean2)
print(list_rows)
#type(clean2)
'''

df = pd.DataFrame(list_rows)
df.head(10)

#Data Manipulation and Cleaning and split into 10 columns
df1 = df[10].str.split(',', expand=True)
df1.head(10)

#Character [] removing by strip method : Unwanted Data Cleaning and Processing
df1[0] = df1[0].str.strip('[')
df1[0] = df1[0].str.strip(']')

df1[1] = df1[1].str.strip(']')
df1[13] = df1[13].str.strip(']')
df1.head(20)

#In data we want heading for different words:
col_labels = soup.find_all('th')
print(col_labels)

#Converting data in Data Frame:
all_header = []
col_str = str(col_labels)
cleantext2 = BeautifulSoup(col_str, "html.parser").get_text()
all_header.append(cleantext2)
df2 = pd.DataFrame(all_header)
print(df2)

df3 = df2[0].str.split(',', expand=True)
print(df3)

frames= [df3, df1]
df4 = pd.concat(frames)
df4.head()

df4 = df4.rename(columns=df4.iloc[0])
df5.head()

df6 = df5.dropna(axis=0)
print(df6)


df7.df6.drop(df6.index[0])
df7.head(20)

df8 = df7[0].str.split(',', expand=True)
print(df8)

