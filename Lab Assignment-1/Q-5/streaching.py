# Required libraries

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read an image
img = cv2.imread('lena.jpg',0)

# Display original image 
cv2.imshow('Original Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Coping the original image
img_cp = img.copy()

minI=img.min()
maxI=img.max()
minO=100
maxO=200

for i in range(0,len(img)):
    for j in range (0,len(img[0])):
        img_cp[i][j]=((img_cp[i][j]-minI)/(maxI-minI))*255
        img_cp[i][j]=((img_cp[i][j]-minI)*(maxO-minO)/(maxI-minI))+minO

# Display constrast streached image 
cv2.imshow('Contrast Image',img_cp)
cv2.waitKey(0)
cv2.destroyAllWindows()    
#iI-minI)*(((maxO-minO)/(maxI-minI))+minO)
