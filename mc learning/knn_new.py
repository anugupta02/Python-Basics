#Importing libraries
import pandas as pd
import numpy as np
import math 
import operator

names=['sepal_length','sepal_width','petal_length','petal_width','species']
data=pd.read_csv("C:\Users\anugu\iris.csv",names=names)
#data.head()
print(data.shape)


def ed(data1,data2,length):

    distance=0
	for x in range(length):
		distance += np.square(data1[x] - data2[x])
	return np.sqrt(distance)
	
#Defining our KNN model
def knn(trainset,testset,k):
    distances = {}
	sort = {}
	length=testset.shape[1] 
	#in shape[] either passed parameter is 0 means key and 1 means value
	
	for x in range(len(trainset)): 
		dist = ed(testset,trainset.iloc[x],length)
		distances[x]=dist[0]
		
	sorted_d = sorted(distances.items(),key=operator.itemgetter(1))
	neighbors = []
    
    # Extracting top k neighbors
    for x in range(k):
        neighbors.append(sorted_d[x][0])
    #### End of STEP 3.3
    classVotes = {}
    # Calculating the most freq class in the neighbors
    for x in range(len(neighbors)):
        response = trainset.iloc[neighbors[x]][-1]
 
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(),
    key=operator.itemgetter(1), reverse=True)
    return(sortedVotes[0][0], neighbors)

	
#Creating a dummy testset
testSet = [[5.1,3.8,1.5,0.3]]
test = pd.DataFrame(testSet)
k=7
result,neigh=knn(data,test,k)
print(result)
print(neigh)


