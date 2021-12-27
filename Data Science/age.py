import numpy as np
from matplotlib import pyplot as plt


age = [22,55,62,45,21,22,34,42,15,19,20,42,102,95,85,55,110,108,70,65,55,109,101,80,32,65,54,44,43,42,48]
bins = [10,20,30,40,50,60,70,80,90,100,110]
plt.hist(age,bins,histtype='bar',rwidth=.5)
plt.xlabel('age groups')
plt.xlabel('Number of people')
plt.title('Histogram')
print(plt.show())

#256 types of graphs in total in matplotlib