# Required libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read an image
img = cv2.imread('lena.jpg',0)

numrows=len(img)      # number of rows  
numcols=len(img[0])   # number of columns

# show an image 
cv2.imshow('Original image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Coping image to rotate
img_cp = img.copy()

angle = int(input("input rotating angle :"))
scale = 1.0
center = (numrows/2,numcols/2)

rot = cv2.getRotationMatrix2D(center,angle,scale)
rotate=cv2.warpAffine(img_cp,rot,(numcols,numrows))

# show an image 
cv2.imshow('rotated image',rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()
