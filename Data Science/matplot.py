#pip install matplotlib

#Seaborn
#ggplot
#Bokeh
#tablute
#Plotly
#Pygal is an open source program that allows you to create vector graphics for your website.
'''Is Seaborn better than Matplotlib?
It is used to create more attractive and informative statistical 
graphics. While seaborn is a different package, it can also be used to 
develop the attractiveness of matplotlib graphics. While matplotlib is 
great, we always want to do better.
'''

#from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

x=[5,13,26,45,78]
y=[14,25,40,70,100]
x1=[8,19,30,50,100]
y1=[25,50,90,150,210]
#plt.plot(x,y)

plt.xlabel('Person')
plt.ylabel('Production')
plt.title('Production Table')
#plt.legend()  #When multiple lines in graph then we use legend in that case
plt.plot(x,y,'r',labels='Less',linewidth=4)
plt.plot(x1,y1,'g',labels='increase',linewidth=5)
plt.legend()
#plt.savefig('name.jpg')
print(plt.show())



