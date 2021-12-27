import cv2
image =cv2.imread("tet.jpg",1)
cv2.imshow("Image",image)
cv2.waitKey(0)

#convert the image to grayscale
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray)
#print(gray)
cv2.waitKey(0)


#applying edge aetection we can find the outline of object in image 
edged=cv2.Canny(gray,0,155)

cv2.imshow("Edge",edged)
cv2.waitKey(0)

from imutils import contours
import imutils
import numpy
import cv2

# threshold the image by setting all pixel value 
#less than 225
#(white; foreground) and all pixel value
#>=225 to 255
#(black; background),thereby segmenting the 
#image
thresh=cv2.threshold(gray,225,255,cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Thresh",thresh)
cv2.waitKey(0)
#find contours .,outlines) of the foreground objects in the image thresholded image
cnts=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#print('value',cnts)
output=image.copy()

# Loop over the contours
for c in cnts:
    #draw each contour on the output image with a 3px thicknpur 
    # outline ,then display the output contours one at a time 
    #ctr=numpy.array)(c).reshape((-1,1,2)).astype(numpy.int32)
    #print(Len(c))
    ctr=imutils.grab_contours(cntsS)
 
    cv2.drawContours(output,[ctr],-1,(0,255,0),3)
    cv2.imshow("Contours",output)
    cv2.waitKey(0)
