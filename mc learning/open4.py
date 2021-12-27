import cv2
import numpy as np
import math
fd=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)
while True: #jab tak terminate nhi kr dete tabh tak chalta rahe
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.IMREAD_GRAYSCALE)
    faces=fd.detectMultiScale(gray,1.3,5)
    #color,scale,thickness of line
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.imshow('Faces',img)
    if(cv2.waitKey(1)==ord('q')):
        break

cam.release()
cv2.destroyAllWindows()