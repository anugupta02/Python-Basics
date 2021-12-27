#Generators
def sample():
	a = 1
	print("This is Printed first")
	yield a#return pause
	a+=1#a = 2
	print("This is Second Page")
	yield a#return pause
	a+=1
	print("This is Last print")
	yield a

#print(sample())
a = sample()
print(a.__next__())
print(a.__next__())