import numpy as np

arr=np.array([1,2,3,4,5,6])

arr1=np.array({1,2,3,4,5,6})

arr1=np.array({1:'Ram',2:'Shyam'})
arr[1]
#print(arr)
#print(arr1)

dt=np.dtype(np.int64)
dt1=np.dtype('i4')
student=np.dtype([('name','S20'),('age','i1'),('marks','f4')])
#print(type(student))
s1=np.array([('Ramandeep singh gurjewala',21,67)],dtype=student)
#print(s1)

a1=np.arange(1,13,1)
#print(a1)
#Reshaping of array:--
m1=a1.reshape(4,3)

#Slicing of data :--
m1[2,2]
#print(m1[2,2])

m1[1:3,1:3]
#print(m1[1:3,1:3])

for x in range(1,3):
    for y in range(1,3):
	    print(m1[x],[y],end=' ')
#print()

#print(m1.T)
#print(m1.mean())
#Zeroth array:--
#print(np.zeros([3,3]))
#Once array:--
#print(np.ones([3,3]))

#Identity Array:--
#print(np.eye(3,3))

m1=np.arange(1,10,1).reshape(3,3)
m2=np.arange(2,20,2).reshape(3,3)
#print(m1)
#print(m2)

#Product of 2 matrices:--
m3=np.dot(m1,m2)
print('\n')
#print(m3)

#print(np.add(m1,m2))

#print(np.subtract(m2,m1))

#print(np.multiply(m1,m2))

#print(np.divide(m1,m2))

#Without using function matrice make 3 by 3:--

m4=np.array([[1,2,3],[3,2,4],[4,5,6]])
#print(m4)
#print(m4.size)#

m5=np.array([[1,2,3,4],[4,5,6,7],[9,5,8,6],[8,9,6,3]])
#print(m5)
#Used by arange:--
#print([m5[1,1],m5[1,2],m5[1,3]])
#print([m5[2,1],m5[2,2],m5[2,3]])
#print([m5[3,1],m5[3,2],m5[3,3]])

#Used by Slicing:--
a=np.arange(1,17,1).reshape(4,4)
#print(a)
#print(a[1:4,1:4])
#print(a[1,2])
#print(a[1:2,2:4])

mat = np.arange(1,17).reshape(4,4)
print(mat)
#print(np.hsplit(mat,2))
#print(np.vsplit(mat,2))

#csv - comma separated
#tsv - tab saparated ex: name age salary
#excel disadvantage is that it only takes 99 records in a file
#in machine learning data stored in pentabyte so thats why we save the data by using csv and tsv 



