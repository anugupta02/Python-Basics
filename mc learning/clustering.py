from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt

X,y=make_blobs(n_samples=300, centers=6,clusters_std=0.80,random_state=0)
print(X)
plt.scatter(X[:, 0],X[:, 1], s=50)



#k-means algorithm
from sklearn.cluster import KMeans
km=KMeans(n_clusters=6)
km.fit(X)

pred=km.predict(X)
print(pred)

plt.scatter(X[:,0],X[:,1],c=pred,cmap='winter')
centers = km.cluster_centers_plt.scatter(centers[:,0],centers[:,1], 
                                     c='black',s=300,alpha=0.5)
									 
'''
K-Means Algorithm Works:

1. Choose the number of k clusters
2. Select at random k points, the centroids
3. Assign each data points to closet centroid
4. Compute and place the new centroid of each cluster
5. Reassign each data point to the new closet centroid

If any Reassignment took place, go to step4
otherwise ur model is ready
'''

#Finding optimal number of clusters
#Elbow method:

cluster_range = range(1,15)
cluster_errors=[]

for k in cluster_range:
	km=KMeans(k)
	km.fit(X)
	cluster_errors.append(km.inertia_)
	#inertia returns the error and that is added in our list

import pandas as pd
df=pd.DataFrame({'num_clusters':cluster_range,
                 'cluster_error':cluster_errors})
print(df)

#WCSS --> With-in Cluster Sum of Squared error
plt.plot(cluster_range,cluster_errors,marker='o')
plt.xlabel('No. of clusters')
plt.ylabel('WCSS error')
plt.show()