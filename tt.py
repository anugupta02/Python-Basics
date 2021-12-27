
import pandas as pd
import sqlalchemy
import numpy as np
import pymysql

con = sqlalchemy.create_engine('mysql+pymysql://root:020296@localhost/wsp')
#We give encoding=latin-1 coz database will accept this encoding type only
data = pd.read_csv('C:/Users/anugu//employee.csv',sep=',',encoding='latin-1',usecols=['Name','Designation','Salary'])
"""The parameter essentially means the number of rows to be read into a dataframe at any single time in order to fit into 
the local memory. Since the data consists of more than 70 millions of rows, I specified the chunksize as 1 million rows 
each time that broke the large data set into many smaller pieces."""
data.to_sql('MyServer',con=con,if_exists='append',index=False,chunksize=1)


