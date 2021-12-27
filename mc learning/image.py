'''
How does Haar Cascade work?
It is a machine learning based approach where a cascade function is 
trained from a lot of positive and negative images. It is then used 
to detect objects in other images. The algorithm has four stages: 
Haar Feature Selection.


What is Haar feature selection?
Haar-like feature. From Wikipedia, the free encyclopedia. 
Haar-like features are digital image features used in object 
recognition. They owe their name to their intuitive similarity 
with Haar wavelets and were used in the first real-time face detector.


What is Haar cascade classifier?
A Haar Cascade is basically a classifier which is used to detect the 
object for which it has been trained for, from the source. 
The Haar Cascade is trained by superimposing the positive image 
over a set of negative images. The training is generally done on 
a server and on various stages.
'''


import cv2

#img=cv2.imread('img1.jpg',cv2.IMREAD_COLOR)
img=cv2.imread('img1.jpg',cv2.IMREAD_GRAYSCALE)
#img=cv2.imread('img1.jpg',cv2.IMREAD_REDUCED_COLOR)

#print(img)
#print(img.shape)

#cv2.imshow("Photo",img)
#cv2.waitKey(1)    #jab tak waitkey nhi daloge image load nhi hogi
#waitKey(1) it means image ko show mat karo

cv2.rectangle(img,(50,100),25,(0,150,0),-1)
cv2.rectangle(img,(50,100),(200,350),(0,150,0),5) #start x position, start y position,color,thickness
#cv2.putText(img,'Anu',(20,30),cv2.FONT_HERSHEY_DUPLEX,0.5,(0,0,255),1) #textfont,size,color,thickness
#cv2.line(img,(20,40),(300,40),(0,255,0),4)
#cv2.cirlce(img,(40,100),25,(25,60,100),-1) #image,(x,y),radius,color,line thickness
cv2.imshow("Photo",img)
cv2.waitKey(1)

#cv2.destroyAllWindows()



