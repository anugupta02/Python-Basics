import cv2
image =cv2.imread("tet.jpg",1)
cv2.imshow("Image",image)
cv2.waitKey(0)

#convert the image to grayscale
#gray = cv2.cvtColor(image,cv2.COLOR_BGR2Lab)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray)
#print(gray)
cv2.waitKey(0)

#applying edge detection we can find the outlines of object in images
edged=cv2.Canny(gray,0,155)
cv2.imshow("Edged",edged)
cv2.waitKey(0)

#pip install --upgrade imutils
from imutils import contours
import imutils
import numpy
import cv2
#threshold the image by setting all pixel values less than 225
#(white;foreground) and all pixel values
#>= 225 to 255
#(black;background),thereby segmenting the image

thresh = cv2.threshold(gray,225,255,cv2.THRESH_BINARY_INV)[1]
#to grab 1st index of image
cv2.imshow("Thresh",thresh)
cv2.waitKey(0)
#find contours (i.e; outlines) of the foreground objects in the 
#thresholded image

cnts=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#print('value',cnts)
output=image.copy()


#loops over the contours

for c in cnts:
	#draw each contour on the output image with a 3px thick pure
	#outline, then display the output contours one at a time
	#ctr = numpy.array(c).reshape((-1,1,2)).astype(numpy.int32)
	#print(len(c))
	ctr.imutils.grab_contours(cnts)
	#cv2.drawContours(output,[ctr],-1,(0,255,0),3)
	cv2.imshow("Contours", output)
	cv2.waitKey(0)
#draw the total number of contours found in purple

#text














