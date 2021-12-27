'''
Functions:

def sample():
    print("in sample")

#print("in main")
sample()
'''

'''
def sample():
    ""
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    print("Total :",a+b)

help (sample)
'''

'''
Local --> with in functions
Global --> any where


a = 25  #Global
def func():
    b=50  #Local
    print(a,b)
func()
print(a)
print(b) #Error
'''

'''
a = 25  #Global
def func():
    global b
    a=10
    b=50  #Local
    print(a,b)
func()
print(a)
'''

'''
def add(a=6,b=7):
    
    print("Sum : ",a+b)


add()
'''
'''
def add(a=6,b=7):
    
    print("Sum : ",a+b)
    print("A : " , a)
    print("B : " , b)

add(b=6)
'''
'''
RETURN TYPE FUNCTIONS:

def add(*a):  #* means all arguments that we have passed in func
    
    print("A : " , a)

add(6,8,9,45,46,87)
'''
'''
def add(*a):
    print("A : ",sum(a))

add(6,8,9,45,46,87)
'''

'''
def mul(*a):
    print("A : ",sum(a))
    m=1
    for x in a:
        m*=x
    print(m)
mul(6,8,9,45,46,87)
'''
'''
def sample(**a):  #** means keywords that we have passed in func
    
    print(a)
sample(name="Anu",address="noida",phno=123456)
'''
'''
def sample(**kwargs):  #** means keywords that we have passed in func
    print(kwargs)
    
sample(name="Anu",address="noida",phno=123456)
'''
'''
def sample(*args):
    return sum(args),1234
    
q,w=sample(5,7,845,65,431,34,6)
print("in main : ",q)
print(w)
'''

'''
lambda expressions:-


add = lambda a,b:a+b
print(add(8,6))
'''
'''
add = lambda a:a**4  #** is Its a keyword
print(add(2)) ---- Its a keyword argument
'''
'''
a=[5,4,51,54,3,21,65]
add = lambda a:a%2==0

print(add(2))
'''

'''
a = [5,4,5,1,4,3,2,51,54,51,3,21,65,4,3,1,3,2,16,54,313,21,54,13,2,1,654,313]
add = lambda a:a%2==0
q = filter(add,a)
print(list(q))
'''
'''
map-->mapping
filter-->filter

filter(function, seq_of Element)
'''

'''
a = [5,4,5,1,4,3,2,51,54,51,3,21,65,4,3,1,3,2,16,54,313,21,54,13,2,1,654,313]
add = lambda a:a%2==0
q = filter(add,a)
print(list(q))
'''
'''
map-->mapping
filter-->filter

filter(function, seq_of Element)
'''

'''
a = [5,4,5,1,4,3,2,51,54,51,3,21,65,4,3,1,3,2,16,54,313,21,54,13,2,1,654,313]
add = list(lambda a:a%2==0,a)
print(add(q))
'''
'''
a = [5,4,5,1,4,3,2,51,54]
q = list(map(lambda a:a%2==0, a))

print(q)

map-->mapping
filter-->filter
reduce-->Self study
filter(function, seq_of Element)

'''

'''
Modules:-
Pre-define Modules
User-define Modules
'''

'''
import calendar
import time
#print(dir(calendar)
#help(calendar)
#print(calendar.month(2019,6))
#print(calendar.calendar(2019))
print(time.ctime())
'''
'''
import calendar as c
import time as t
print(c.calendar(5555))
'''
'''
import calendar as c
import time as t
print(c.isleap(2016))
'''
