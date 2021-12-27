import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


#data1=pd.read_excel('C:/Users/anugu//iris.csv',header=None)


x=np.arange(0,3 * np.pi,0.1)
y_sin = np.sin(x)
y_cos=np.cos(x)
print(x)
print(y_sin)
plt.plot(x,y_sin,'r')
plt.plot(x,y_cos,'*')
print(plt.show())



