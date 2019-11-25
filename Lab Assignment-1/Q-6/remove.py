# Required libraries

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read an image
img = cv2.imread('img8.tif',0)

# Display original image 
cv2.imshow('Original Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_cp=img.copy()

for row in range(1,len(img)-1):
    for col in range (1,len(img[0])-1):
    
        if img[row][col] == 0 or img[row][col] == 255:         
            img_cp[row][col] = (img[row - 1][col] + 
                             img[row - 1][col - 1] + 
                             img[row - 1][col + 1] + 
                             img[row][col - 1] + 
                             img[row][col + 1] + 
                             img[row + 1][col + 1] + 
                             img[row + 1][col] + 
                             img[row + 1][col - 1]) / 8
       
# Display constrast streached image 
cv2.imshow('Clear Image',img_cp)
cv2.waitKey(0)
cv2.destroyAllWindows()
