# Required libraries 
import cv2
import numpy as np

img = cv2.imread('img2.jpg')      # reading an image
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

lbp = [[0,0,0],[0,0,0],[0,0,0]]
out= np.copy(img)

row=len(img)
col=len(img[0])

for i in range(1, row-1):
    for j in range(1, col-1):
        center= img[i][j]
        m=0
        for k in range (i-1, i+2):
            n=0
            for l in range (j-1, j+2):
                if (img[k][l] > center):
                    lbp[m][n] = 1
                else:
                    lbp[m][n] = 0
                n=n+1
            m=m+1
        out[i][j] = (lbp[0][0]*1) + (lbp[0][1]*2) + (lbp[0][2]*4) + (lbp[1][2]*8) + (lbp[2][2]*16) + (lbp[2][1]*32) + (lbp[2][0]*64)+(lbp[1][0]*128)

print('\nOriginal Image :\n')
print(img)       
       
print('\nLocal Binary Pattern : \n')
print(lbp)

print('\nout\n')
print(out)

cv2.imshow('image',out)
cv2.waitKey(0)
cv2.destroyAllWindows()
