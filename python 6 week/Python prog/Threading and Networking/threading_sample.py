import smtplib
import socket
ser = smtplib.SMTP('smtp.gmail.com',587)
ser.starttls()
ser.login('hbaghelducat@gmail.com','root@123')
msg = "Hello World"
ser.sendmail('hbaghelducat@gmail.com','satyamrajawat1994@gmail.com',msg)
print("Sent")
ser.close() 