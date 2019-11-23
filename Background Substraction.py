# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 08:47:54 2019

@author: Dell
"""

import cv2
import numpy as np
import os,sys,PIL
from PIL import Image

def listdirectory():
    files=os.listdir(os.getcwd())
    imlist=[]
    for f in files:
        if f[-4:] in [".jpg",".jpeg"]:
            imlist.append(f)
    return imlist

def saveindirectory(mean,i,k):
    if(k=="Mean"):
        cv2.imwrite(r'C:\Users\Dell\.spyder-py3\et\Mean\{}.jpg'.format(i),mean) 
    elif(k=="Median"):
        cv2.imwrite(r'C:\Users\Dell\.spyder-py3\et\Median\{}.jpg'.format(i),mean) 
    else:
        cv2.imwrite(r'C:\Users\Dell\.spyder-py3\et\{}.jpg'.format(i),mean) 
        

def getaverage(files):
    N=len(files)
    img=cv2.imread(files[0])
    w=len(img[0])
    h=len(img)
    arr=np.zeros((h,w),np.float)
    for f in files:
        img=cv2.imread(f,0)
        img=np.array(img,dtype=np.float)
        arr=arr+img
    arr=arr/N
    arr=np.array(np.round(arr),dtype=np.uint8)           # Rounding the pixel
    return arr                               

def bgsubmeanthresholding(files,mean):
    k=1
    for f in files:
        im=cv2.imread(f,0)
        img=abs(im-mean)
        cnt=0
        su=0
        for i in range(0,len(img)):
            for j in range(0,len(img[0])):
                su=su+img[i][j]
                cnt=cnt+1
        su=su/cnt
        ret,th=cv2.threshold(img,su,255,cv2.THRESH_BINARY)
        saveindirectory(th,str(k),"Mean")
        k=k+1

def bgsubmedianthresholding(files,mean):
    k=1
    for f in files:
        im=cv2.imread(f,0)
        img=abs(im-mean)
        res=img.flatten()
        res=sorted(res)
        N=len(res)
        if(N%2!=0):
            med=res[int((N-1)/2)]
        else:
            p=int(N/2)
            med=int((res[p]+res[p-1])/2)
        ret,th=cv2.threshold(img,med,255,cv2.THRESH_BINARY)
        saveindirectory(th,str(k),"Median")
        k=k+1
         
          
if __name__=="__main__":
    files=listdirectory()
    mean=getaverage(files)
    saveindirectory(mean,"Mean","m")
    bgsubmeanthresholding(files,mean)
    bgsubmedianthresholding(files,mean)
    
    
    
