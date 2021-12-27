import socket
import threading
server=socket.socket()
host = "localhost"
port = 12345
server.connect((host,port))
#data = server.recv(1024)
#print(data)
#ser.send(f"My Name is {name}".encode())

def send():
     while True:
	    msg = input()
		if msg:
		 c.send(msg.encode())
			  
th1 = threading.Thread(target=send)
th1.start()

while True:
     data = server.recv(1024)
	 print(data)
	 
server.close()