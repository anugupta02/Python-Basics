# decorators : self study
'''
Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class.
Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.
'''
'''
def sample(f): #f = demo
    def example():
        print("in example")
        f()
    return example

def demo():
    print("in demo")

q=sample(demo)
q()

'''
def sample(f): #f = demo
    def example():
        print("in example")
        f()
    return example

@sample #demo = sample(demo)
def demo():
    print("in demo")
print(demo)
demo()

