'''
Exception Handling

try:-

except:-

finally:-
'''
'''
a = int(input("Enter 1st No. : "))
b = int(input("Enter 2nd No. : "))

try:
    print(a/b)
except:
    print("division by zero ")
'''
'''
try:
    a = int(input("Enter 1st No. : "))
    b = int(input("Enter 2nd No. : "))
    print(a/b)
except ZeroDivisionError as ze:
    print(ze)
'''
'''
try:
    a = int(input("Enter 1st No. : "))
    b = int(input("Enter 2nd No. : "))
    print(a/b)
except ZeroDivisionError as ze:
    print(ze)
except ValueError as v:
    print(v)
'''
'''
while True:
  try:
      a = int(input("Enter 1st No. : "))
      b = int(input("Enter 2nd No. : "))
      print(a/b)
except ZeroDivisionError as ze:
    print(ze)
except ValueError as v:
    print(v)
finally:
    print("Thank You")
'''



    
