
class Sample:
    
	def __init__(self):
	    self.x = int(input("Enter 1st No.: "))
	    self.y = int(input("Enter 2nd No.: "))
		
	def display(self):
	    print("Total: ", self.x + self.y)
		
obj1 = Sample()
obj1.display()

'''
setattr(onj1, 'a',3)
setattr(obj1, 'b', 45)

obj1.__dict__
{'x' : 5,'y' : 9,'z' : 25}
obj2.__dic__
{'x' : 15,'y' : 29,'z' : 35}

getattr(obj2, 'x')
getattr(obj1, 'y')

delattr(obj2 , 'x')
'''