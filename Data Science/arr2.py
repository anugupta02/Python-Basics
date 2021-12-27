import numpy as np

a=np.array([1,2,3])
#print(type(a))
#print(a.shape)
b=np.array([[1,2],[2,3]])
#print(b.shape)
#print(a[0],a[1],a[2])
a[0]=5
#print(a)


a=np.array([[1,2,3],[2,3,4],[3,4,5]])
#print(a)
b=a[1:3,1:3]
#print(b)
b[1,1]=30
#print(b)
#print(a)
