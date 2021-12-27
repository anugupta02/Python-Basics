import cv2

img=cv2.imread('a.jpg',0)
rows,cols=img.shape

M-cv2.getRotationMatrix2D((rows/2,cols/2),60,1)
dst=cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()