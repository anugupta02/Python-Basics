'''
Server--> Create Host(IP), Port
Client--> Connect Host(IP), Port
'''

import socket
import threading
server = socket.socket()
host = "localhost"
port = 12345
#name = input("Enter Name : ")
server.bind((host,port))
server.listen()
c,addr = server.accept()
#server.bind((host,port)) #1st bracket is for function and 2nd is for tupple#
#server.listen()
#c, addr = server.accept()
#c.send("Thanks for Connecting....".encode())

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