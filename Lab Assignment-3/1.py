'''

Q-1 Apply Difference of Gaussian edge detection technique on the given image ‘3.jpg’with Laplacian kernels as given below. Get the results for sigma = 1, 3 . Compare the outcomes and write your observations. Don’t use the gaussian filter from python library.

'''

import cv2
import numpy as np
import math

img0 = cv2.imread('3.jpg')
img = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)

out = np.copy(img)

#print(img)

G=[ [1,1,1],
    [1,-8,1],
    [1,1,1]]
                    
sigma = 1
r = len(img)
c = len(img[0]) 
'''
for i in range (0,3):
    for j in range (0,3):
        G[i][j]=(1/(2*math.pi*sigma*sigma))*(math.exp((i*i+j*j)/(2*sigma*sigma)))      
print(G)'''

for i in range (1,r-1):
    for j in range (1,c-1):
        m=0
        result=0
        for k in range (i-1, i+2):
            n=0
            for l in range (j-1, j+2):
                result+=img[k][l]*G[m][n]
                n=n+1
            m=m+1
        
        out[i][j]=result
#print(out)
cv2.imshow('result',out)
cv2.waitKey(0)
cv2.destroyAllWindows()
