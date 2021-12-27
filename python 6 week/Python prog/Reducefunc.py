'''
# python code to demonstrate working of reduce() 

# importing functools for reduce() 
import functools 

# initializing list 
lis = [ 1 , 3, 5, 6, 2, ] 

# using reduce to compute sum of list 
print ("The sum of the list elements is : ",end="") 
print (functools.reduce(lambda a,b : a+b,lis)) 

# using reduce to compute maximum element from list 
print ("The maximum element of the list is : ",end="") 
print (functools.reduce(lambda a,b : a if a > b else b,lis)) 
'''
'''
# python code to demonstrate working of reduce() 
# using operator functions 
  
# importing functools for reduce()
import functools 
  
# importing operator for operator functions 
import operator 
  
# initializing list 
lis = [ 1 , 3, 5, 6, 2, ] 
  
# using reduce to compute sum of list 
# using operator functions 
print ("The sum of the list elements is : ",end="") 
print (functools.reduce(operator.add,lis)) 
  
# using reduce to compute product 
# using operator functions 
print ("The product of list elements is : ",end="") 
print (functools.reduce(operator.mul,lis)) 
  
# using reduce to concatenate string 
print ("The concatenated product is : ",end="") 
print (functools.reduce(operator.add,["Anu"," ","Gupta"])) 


Difference between Reduce and Accumulate :-
reduce() is defined in “functools” module, accumulate() in “itertools” module.
reduce() stores the intermediate result and only returns the final summation value. Whereas, accumulate() returns a list containing the intermediate results. The last number of the list returned is summation value of the list.
reduce(fun,seq) takes function as 1st and sequence as 2nd argument. In contrast accumulate(seq,fun) takes sequence as 1st argument and function as 2nd argument.
'''

# python code to demonstrate summation 
# using reduce() and accumulate() 

# importing itertools for accumulate() 
import itertools 

# importing functools for reduce() 
import functools 

# initializing list 
lis = [ 1, 3, 4, 10, 4 ] 

# priting summation using accumulate() 
print ("The summation of list using accumulate is :",end="") 
print (list(itertools.accumulate(lis,lambda x,y : x+y))) 

# priting summation using reduce() 
print ("The summation of list using reduce is :",end="") 
print (functools.reduce(lambda x,y:x+y,lis)) 

