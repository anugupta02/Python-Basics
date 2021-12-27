'''
Lambda Function:
a) A simple 1-Line function
b) Don't use def or return keywords.
These are implicit
'''

'''
Example:
c = lambda x: 2*x
print(c(90))

d = lambda x,y:x+y
print(d(90,100))
'''
'''
mx = lambda x,y: x if x>y else y
print(mx(8,5))
'''

'''
Map Function:
a) Apply same function to each element of a sequence
b) Return the modified list

List, [m,n,p]
Function, f()----> MAP ----> Mew list, [f(m),f(n),f(p)]
'''
'''
n=[10,9,8,7,6,5,4,3,2,1]
#print(list(map(lambda x:x **2,n)))

List comprehension soluion:
print([x**2 for x in n])
'''

'''
Filter Function:
a) Filter items out of sequence.
b) Return filtered list

List, [m,n,p]

