import pandas as pd
import sqlalchemy
import numpy as np
import pymysql
con=sqlalchemy.create_engine('mysql+pymysql://root:Mysql@4321@localhost/wsp')
data=pd.read_csv('C://Users/Aman/Employee.csv',sep=',',encoding='latin-1',usecols=['Name','Designation','Salary'])
data.to_sql('ducat',con=con,if_exists='append',index=False,chunksize=1)
# index=False means it will not display index as it display index in csv file
#chunksize=1 means it will one item at a time
#encoding='latin-1' is used for csv file .It is charater set for writing data  
#it is like utf-8
#use