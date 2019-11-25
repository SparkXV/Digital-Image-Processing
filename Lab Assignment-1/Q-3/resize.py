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

Fx = float(input("input scaling factor Fx = :"))
Fy = float(input("input scaling factor Fy = :"))

resizeimage = cv2.resize(img_cp,None,fx=Fx,fy=Fy)

# show an image 
cv2.imshow('resized image',resizeimage)
cv2.waitKey(0)
cv2.destroyAllWindows()
