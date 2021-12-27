class Sample:
    def __init__(self,x=0):
        self.x=x
    def __sub__(self,other):
        obj=self.x + other.x
        return obj    
    def __str__(self):
        return f"{self.x}"
    
obj1=Sample(30)
obj2=Sample(20)
print(obj1)
print(obj2)
