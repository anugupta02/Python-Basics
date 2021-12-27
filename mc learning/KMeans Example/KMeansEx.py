from sklearn.cluster import  KMeans
import numpy as np
from PIL import Image
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

img=Image.open('bird.png')
img_np=np.asarray(img)
#print(img_np)
img_np.shape

pixels=img_np.reshape(img_np.shape[0]* img_np.shape[1],img_np.shape[2])
print(pixels.shape)
model=KMeans(n_clusters=16)
model.fit(pixels)

pixels_centroids=model.labels_
cluster_centers=model.cluster_centers_
print(pixels_centroids)
print(cluster_centers)

final=np.zeros((pixels_centroids.shape[0],3))
print(final.shape)

for cluster_no in range(16):
    final[pixels_centroids==cluster_no]=cluster_centers[cluster_no]
print(final)

comp_image=final.reshape(img_np.shape[0],img_np.shape[1],3)
print(comp_image.shape)

comp_image=Image.fromarray(np.uint8(comp_image))
comp_image.save('newbird.png')

fname='bird.png'
fname1='newbird.png'
img1=mpimg.imread(fname,0)
img2=mpimg.imread(fname1,0)
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(20,20))
ax1.imshow(img1)
ax1.set_title('Orginal Image')
ax2.imshow(img2)
ax2.set_title('Compressed Image')
print(plt.show())

'''
import os

print('Size of Orginal Image',int(os.stat('bird.png').st_size/1024),'kB')
print('Size of Compressed Image',int(os.stat('newbird.png').st_size/1024),'kB')
'''