#from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import numpy as np


labels=['Python','C++','Ruby','Java','R']
sizes=np.array([250,130,200,210,100])
colors=['yellow','yellowgreen','pink','blue','red']
exp=[0,0,0,0,.1]

def calc(val):
    a  = np.round(val/100*sizes.sum())
    return a
#radius=10
print(plt.pie(sizes,explode=exp,labels=labels,colors=colors,startangle=90,
        shadow=True,autopct=calc))
plt.legend()
print(plt.show())

