# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 13:49:26 2021

@author: Aakash
"""

import cv2
import os
import numpy as np

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)

            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
 
            if objCor ==3: 
                objectType ="Tri"
            elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio >0.98 and aspRatio <1.03: 
                    objectType= "Square"
                else:
                    objectType="Rectangle"
            elif objCor>4: 
                objectType= "Circles"
            else:
                objectType="None"
 
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContour,objectType,
                        (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,
                        (0,0,0),2)

        
os.chdir(r'C:\Users\Aakash\Desktop\AAKASH\Coding Stuff\Python\Project\opencv project')

img = cv2.imread('shapes.png')
imgContour = img.copy()

imgCanny = cv2.Canny(img, 50, 50)
getContours(imgCanny)

cv2.imshow('Original', img)
cv2.imshow('Canny', imgCanny)
cv2.imshow('Contour', imgContour)
cv2.waitKey(0)
