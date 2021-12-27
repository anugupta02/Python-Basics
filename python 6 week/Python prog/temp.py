class Sample:
    def __init__(self,x):
        self.x = x
        
    def __add__(self,other):#self
	   #print("in display : ",self.x)
       #print("in display : ",other.x)
        a = self.x*other.x
        return a
        
obj1 = Sample(5)
obj2 = Sample(10)
#obj1.display(obj2)
print(obj1 + obj2)
#print(dir(obj1))
