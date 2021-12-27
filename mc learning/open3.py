import numpy as np
import cv2
cap=cv2.VideoCapture(0)
#Define the kodac and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('http://192.168.137.112:8080/video',fourcc,10,(140,80))
while(cap.isOpened()):
	ind,frame=cap.read()
	if ind==True:
		frame=cv2.flip(frame,0)#optional
		
		#write the flipped frame
		out.write(frame)
		cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0Xff == ord('z'):
			cv2.dest

		#Hexa code hai jiske corresponding 
			break
		else:
			break
		
#Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()