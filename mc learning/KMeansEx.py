#yolo : it is used to detect the object.

#KMeans: Kmeans ka object banaya aur usme data ki value fit kr di

#uint means unsigned integer main image save krna hai
'''
Matplot main subplot:
1 row ko multipkle rows main divide krta hai
'''
#size print krne ke liye os.stat

from sklearn.cluster import KMeans
import numpy as np
from PTL import Image
import matplotlib.image as mping
import matplotlib.pyplot as plt

img=Image.open('bird.png')
img_np=np.asarray(img)
#print(img_np)
img_np.shape

pixels=img_np.reshape(img_np.shape[0]*img_np.shape[1])