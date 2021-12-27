class Sample:
    def __init__(self,x=0):
        self.x=x
    def display(self):
        print(self.x)
    def __sub__(self,other):
        obj=Sample()
        obj.x=self.x + other.x
        return obj
obj1=Sample(30)
obj2=Sample(20)
obj3=obj1-obj2
obj3.display()