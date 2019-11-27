# Required libraries 
import cv2
import numpy as np

img = cv2.imread('3.2.jpg',0)      # reading an image

row=len(img)
col=len(img[0])

lmebp = [8,((row-2)*(col-2))]
temp1 = []
temp2 = []
out   = np.copy(img)
    
for i in range(1, row-1):
    for j in range(1, col-1):
        center= img[i][j]
        count1=0
        count2=0
        for k in range (i-1, i+2):
            for l in range (j-1, j+2):
                if k == i and l == j:
                    continue
                else:
                    if img[k][l] <= center:
                        temp1[count1] = img[k][l]-center
                        count1 = count1+1
                    else:
                        temp2[count2] = img[k][l]-center
                        count2 = count2+1
        break
    break
#temp.sort()
print('\nOriginal Image :\n')
print(img)       
       
print('\nLocal Maximum Edge Binary Pattern : \n')
print(temp1)
print(temp2)

print('\nout\n')
print(out)

cv2.imshow('image',out)
cv2.waitKey(0)
cv2.destroyAllWindows()
