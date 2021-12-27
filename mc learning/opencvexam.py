'''
Zero
One and 
File Name
'''
import cv2
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    ind, img = cap.read()
    if ind:
        gray= cv2.cvtColor(img,cv2.IMREAD_COLOR)
        cv2.imshow('frame', gray)
        #cv2.imwrite('cap1.jpg',gray)
    if cv2.waitKey(1) & 0xFF == ord('z'):
        break
		
cap.release()


cv2.destroyAllWindows()

			
			