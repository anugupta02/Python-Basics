def swap(x,y):#3,4
    temp=x#t=3
    x=y#x=4
    y=temp#y=3
	return x,y
print("Enter the Two Numbers : ")
a=int(input())
b=int(input())
print("Before Calling Swap function a = ",a," and b = ",b)
a,b=swap(a,b)
print("After Calling Swap function a = ",a," and b = ",b)