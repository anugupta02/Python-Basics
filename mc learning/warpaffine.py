import cv2
import numpy as np
img=cv2.imread('a.jpg',0)
rows,cols=img.shape
M=np.float32([[1,0,40],[0,1,50]])
dst=cv2.warpAffine(img,M,(cols,rows))
'''
warpAffine to implement simple remapping routines. Use the 
OpenCV function getRotationMatrix2D to obtain a rotation matrix
'''
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
