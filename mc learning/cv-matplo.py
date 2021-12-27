#import numpy as np
import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
from matplotlib import pyplot as plt
img=cv2.imread('a.jpg',cv2.IMREAD_COLOR)
plt.imshow(img)
plt.xticks([]),plt.yticks([]) #to hide tick values on X and Y axis
print(plt.show())