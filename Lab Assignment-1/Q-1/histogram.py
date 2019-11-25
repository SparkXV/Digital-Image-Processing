# importing required libraries of opencv 
import cv2 
import numpy as np 
from matplotlib import pyplot as plt

# reads an input image 
img = cv2.imread('lena.jpg',0) 

hist=np.zeros([256,1])

# find frequency of pixels in range 0-255 
# histr = cv2.calcHist([img],[0],None,[256],[0,256]) 

# find frequency of pixels in range 0-255
for i in range (0,256):
     for j in range (0,256):
        hist[img[i][j]+1]=hist[img[i][j]+1]+1

# show the plotting graph of an image 
plt.plot(hist)
plt.show()
