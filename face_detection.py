# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 15:14:56 2021

@author: Aakash
"""

import cv2
import os
os.chdir(r'C:\Users\Aakash\Desktop\AAKASH\Coding Stuff\Python\learning\Youtube and Webinars\Opencv Learning')

faceCascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
img = cv2.imread('rimuru.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w ,h) in faces:
    cv2.rectangle(img, (x, y), (x+y, y+h), (255, 0, 0), 2)

cv2.imshow('Result', img)
cv2.waitKey(0)