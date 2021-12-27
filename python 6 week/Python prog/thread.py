import time,threading
def sample():
    for x in range(1,10):
	    print(x,"Hello World")
	    time.sleep(1)
	
def example():
    for x in range(1,10):
	    print(x,"Hello Python")
	    time.sleep(1)

th1=threading.Thread(target=sample)
th2=threading.Thread(target=example)

th1.start()
th2.start()