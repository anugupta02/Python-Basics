import numpy as np
import cv2
cap=cv2.VideoCapture('http://100.91.152.2:8080/video')
#Define the kodac and create videowriter object
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('abc.avi',fourcc,20,(640,480))
while(cap.isOpened()):
    ind,frame=cap.read()
    
    
    #write the flipped frame
    out.write(frame)
    
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    else:
        break
     
    
#Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()