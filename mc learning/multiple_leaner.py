import pandas as pd

stock = pd.read_csv('economi.csv',names=['Year','Month','Rate_int','Unemp_Rate','Stock_Price'])
df=pd.DataFrame(stock)
df.head()


from pandas import DataFrame
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
    
X = df[['Rate_int','Unemp_Rate']] 
Y = df['Stock_Price']
regr = LinearRegression()
regr.fit(X, Y)
print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)
# prediction with sklearn
New_Interest_Rate = 4.75
New_Unemployment_Rate = 7.2
print ('Predicted Stock Index Price: \n',
regr.predict([[New_Interest_Rate ,New_Unemployment_Rate]]))
# with statsmodels
X = sm.add_constant(X) # adding a constant
model = sm.OLS(Y, X).fit()
predictions = model.predict(X) 

print_model = model.summary()
print(print_model)
