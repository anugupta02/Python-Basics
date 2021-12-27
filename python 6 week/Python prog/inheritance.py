class Sample:
    
	def add(self):
	   self.x = int(input("Enter 1st No.: "))
	   self.y = int(input("Enter 2nd No.: "))
		
class Example(Sample):
     
	 def display(self):
	     print("Total : ",self.x+self.y)
obj = Example()
obj.add()
obj.display()