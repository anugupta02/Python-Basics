'''
Seaborn is a library for making statistical graphics in Python. 
It is built on top of matplotlib and closely integrated with pandas data 
structures. Here is some of the functionality that seaborn offers: 
A dataset-oriented API for examining relationships between multiple variables.
Seaborn is an advance version of matplotlib

Functionality:
Matplotlib: Matplotlib is mainly deployed for basic plotting. 
Visualization using Matplotlib generally consists of bars, pies, lines, scatter plot. 
Seaborn: Seaborn will provide a variety of visualization patterns. 
It will use less syntax and has easily interesting default themes.
'''

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

fig,ax = plt.subplots()
data = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")
ax.violinplot(data["tip"])
plt.xlabel('Tips')
plt.ylabel('Value')
#Show the plot
#print(plt.show())


#tips = sns.load_dataset("tips")
#tips = sns.load_dataset("iris")
#print(tips.head())
#sns.violinplot(x=tips, data=tips)
sns.violinplot(x=tips.sepal_length, data=tips)

tips = sns.load_dataset("tips")
sns.swarmplot(x="tip",y="smoker", data=tips)
g = sns.factorplot("class", "survived", "sex", data=titanic,kind="bar",
     palette="muted",legend=True)


titanic = sns.load_dataset("titanic")
print(titanic.head(20))


