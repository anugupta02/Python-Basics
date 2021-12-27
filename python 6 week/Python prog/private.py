class Sample:
    a = 10
    def __init__(self,x,y):
        self.x = x#Public
        self.__y = y#Private
		self.__display()
		
    def display(self):
        print("A  : ",self.a)
        print("X  : ",self.x)
        print("Y  : ",self.__y)

obj = Sample(5,2)
#obj.display()        
print("in main : ",obj.x)
#print(obj.__y)