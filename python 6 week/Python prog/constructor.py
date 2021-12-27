
class Sample:
    
	def __init__(self):
	
	    print("in init")
	def demo(self):
	    print("in demo", self)
		
	def __del__(self):
	    print("in del")
		
obj1 = Sample()
obj1.demo()
del obj1