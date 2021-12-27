import cv2
img=cv2.imread('data/a.jpg')
MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
gender_list = ['Male', 'Female']

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faceDetect=cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
faces = faceDetect.detectMultiScale(gray)
for (x,y,w,h) in faces:
	cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
       
	#Get Face 
	face_img = img[y:y+h, h:h+w].copy()
	blob = cv2.dnn.blobFromImage(face_img, 1, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
		
	gender_net = cv2.dnn.readNetFromCaffe('data/deploy_gender.prototxt','data/gender_net.caffemodel')
    
    #Predict Gender
	gender_net.setInput(blob)
	gender_preds = gender_net.forward()
	gender = gender_list[gender_preds[0].argmax()]

	cv2.putText(img,gender,(x,y-5),0,.5, (255,255,255),1, cv2.LINE_AA)

cv2.imshow("Faces",img)
cv2.waitKey(0)
cv2.destroyAllWindows()