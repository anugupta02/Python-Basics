import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


#high-level interface for controlling the look of matplotlib fig
#matplotlib inline
#Define a simple plot function, to plot offset sin waves
def sinplot(f=1):
    x = np.linspace(0,8,100)
    for i in range(1,7):
	    plt.plot(x, np.sin(x + i * .5))

sns.set()
sns.set_style('dark')
print(sinplot())
sns.set_style('darkgrid')
print(tanplot())

'''
#sns.set_style('white')
#sns.set_style('whitegrid')

		
#yarn plot   ---> Self-Study


Seaborn figure styles
Seaborn

data = np.random.normal(size=(20, 6) + np.arrange(6)/6
#print(data)
sns.boxplot(data=data)

sns.set_style("white")
sinplot()

sns.set_style("ticks")
sinplot()

#Removing axes spines
#you can call despine function to remove them: despine()
sinplot()
sns.despine()

#f, ax =plt.subplots()
sns.violinplot(data=data)
sns.despine(offset=15,trim=False) #trim space ko hata dega
sns.despine(offset=15,trim=True)

df = sns.load_dataset('iris')
#Large bandwidth
#print(df.head(150))
sns.kdeplot(df['sepal_width'],shade=True,bw=.09,vertical=True,color="red")

#Narrower bandwidth
#sns.kdeplot(df['petal_width'],shade=True,bw=.08,vertical=True,color="green")



'''




