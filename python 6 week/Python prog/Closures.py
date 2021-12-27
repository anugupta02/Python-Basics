'''
import sys as s
a = [1,465,1321,0,0,15375,"Hello", 5+2j]
for x in a:
    try:
        r=1/int(x)
    except:
        print(s.exc_info()[1])
'''
#raise : self study
'''
Closure functions:
def sample():
    print("in sample")
    
a=sample
a()
'''
'''
a = 0
def sample():
    a = 5
    def example():
        a = 10
        print("in example : ",a)
    print("in sample",a)
    example()

sample()
print("in main : ",a)
''' 
'''
Non-Local:
a = 0
def sample():
    a = 10
    
    def example():
        nonlocal a
        a = 5
        print("in example : ",a)
    example()
    print("in sample",a)
    
sample()
print("in main : ",a)
'''
'''
a = 0
def sample():
    a = 5
    def example():
        nonlocal a
        a = 10
        print("in example : ",a)
    example()
    print("in sample",a)

sample()
print("in main : ",a)
'''
'''
def sample(a):#a=5
    def example(b):#b=6
        return a*b#5*6
    return example

q=sample(5)#q=example
print(q(6))#example(6) 30
'''

