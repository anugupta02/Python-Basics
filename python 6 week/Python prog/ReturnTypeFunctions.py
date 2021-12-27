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
