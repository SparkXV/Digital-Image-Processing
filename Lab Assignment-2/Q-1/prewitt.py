import numpy as np      # Required Libraries
import cv2

img = cv2.imread('image1.jpg',0)    # Readong image
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#img_gaussian = cv2.GaussianBlur(gray,(3,3),0)

Gx=np.array([[1,1,1],[0,0,0],[-1,-1,-1]])     # Gx
Gy=np.array([[-1,0,1],[-1,0,1],[-1,0,1]])     # Gy

r = len(img)
c = len(img[0])

pre_imgx=img.copy()
pre_imgy=img.copy()

#img_prewittx = cv2.filter2D(img_gaussian, -1, Gx)
#img_prewitty = cv2.filter2D(img_gaussian, -1, Gy)

for i in range (1,r-1):
    for j in range (1,c-1):
        m=0
        result=0
        for k in range (i-1, i+2):
            n=0
            for l in range (j-1, j+2):
                result+=img[k][l]*Gx[m][n]
                n=n+1
            m=m+1
        
        pre_imgx[i][j]=result

for i in range (1,r-1):
    for j in range (1,c-1):
        m=0
        result=0
        for k in range (i-1, i+2):
            n=0
            for l in range (j-1, j+2):
                result+=img[k][l]*Gy[m][n]
                n=n+1
            m=m+1
        
        pre_imgy[i][j]=result


cv2.imshow("Prewitt X", pre_imgx)
cv2.imshow("Prewitt Y", pre_imgy)
cv2.imshow("Prewitt", pre_imgx + pre_imgy)

cv2.waitKey(0)
cv2.destroyAllWindows()
