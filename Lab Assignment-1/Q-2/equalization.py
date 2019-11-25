# importing required libraries of opencv 
import cv2 
import numpy as np 
from matplotlib import pyplot as plt

# reads an input image 
img = cv2.imread('lena.jpg',0) 

numrows = len(img)    # number of rows
numcols = len(img[0]) # number of columns

n = numrows*numcols

hist=np.zeros([256,1])
pdf =np.zeros([256,1])
cdf =np.zeros([256,1])
out =np.zeros([256,1]) 

# Finding the PDF
for i in range (0,256):
     for j in range (0,256):
        hist[img[i][j]+1]=hist[img[i][j]+1]+1
        pdf[img[i][j]+1]= hist[img[i][j]+1]/n

# Finding the CDF
s=0
l=255        
for i in range (1,256):
        cdf[i]=cdf[i-1]+pdf[i]
        out[i]=int(cdf[i]*l)
            
# show the plotting graph of an image 
plt.plot(out)
plt.show()
