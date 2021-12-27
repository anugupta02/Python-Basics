class ABCD:
	def add(self):
		self.a = int(input("Enter First Number: "))
		self.b = int(input("Enter Second Number: "))
	def display(self):
		print('sum : ',self.a+self.b)

obj=ABCD()
obj1=ABCD()
obj.add()
obj1.add()
obj.display()		
obj1.display()		