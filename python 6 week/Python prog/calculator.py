'''
a= int(input("Enter First Number:"))
b= int(input("Enter Second Number:"))
print("Press + for add:")
print("Press + for sub:")
print("Press + for mul:")
print("Press + for Div:")
c=input("Enter Choice: ")
if c=="+":
    print(a,'+',b,'=',a+b)
elif c=="-":
    print(a,'-',b,'=',a-b)
elif c=="*":
    print(a,'*',b,'=',a*b)
elif c=="/":
    print(a,'/',b,'=',a/b)
else:
    print("Wrong Choice")
'''

'''
Loops
for
while


Syntax:
for object in iterable_object/seq_of_element:
      lines of code
      lines of code

range()-->seq_of_int
range(start,stop,step)
range(stop) start=0 step=1
range(start,stop) step = 1

int
stop excluded
'''

'''
for i in range(10):
    print(i,"Hello World")
'''
'''
a=int(input("Enter Any Numer:"))
for i in range(a,a*10+1,a):
    print(i)
'''
'''
a=int(input("Enter Any Number: "))
#(1,23)
#(2,22)
f=0
for i in range(2,a):
    if a%i==0:
        f=1
if f==0:
    print("Prime")
else:
    print("Not Prime")
'''
'''
a=int(input ("Enter Any Number:  "))
f = 1#f = 1
for i in range(1,a+1):#(1,6) i=1,2,3,4,5
    f*=i#f = 1*2*3*4*5
print(f)
'''

'''
#febonacci Series: 0 1 1 2 3 5 8 13 21 34 55 89 144..........
a=0
b=1
sum=a+b#initialization
num=int(input("Enter the Last Term Range :  "))#initialization
print(a,"\t",b,end="\t")
while(sum<=num):#condition
	print(sum,end="\t")
	a=b		#updation
	b=sum	#updation
	sum=a+b	#updation
'''

'''
a = int(input("Enter Any Number : "))
f = 0
for i in range(2,int(a**.3)+1):
    if a%i==0:
        f = 1
        break
if f==0:
    print("Prime")
else:
    print("Not Prime")
#5463458053
'''

'''
While Loop:

while expression:
       lines of code:
       lines of code
'''
'''
a=1
while a<10:
    print(a,"Hello World")
    a+=1
else:
'''

'''
a= int(input ())
f = 1
while a>0:
  f*=a
  a-=1
print(f)
'''


start = 1
end = 1000000
  
for val in range(start, end + 1):  
   if val > 1:
       for n in range(2,int(val**.3)+1):
       #for n in range(2, val): 
           if (val % n) == 0: 
               break
       else: 
           print(val)

'''
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
'''
'''
for num in range(1,101):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       print (num)
'''
