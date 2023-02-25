# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 11:20:10 2021

@author: Aakash
"""

import cv2
import numpy as np

img = cv2.imread('rimuru.png')
kernal = np.ones((5,5), np.uint8)

imgBlur = cv2.GaussianBlur(img,(13,13),0)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgCanny = cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(img, kernal, iterations = 1)
imgErode = cv2.erode(img, kernal, iterations = 1)

cv2.imshow('Image',img)
cv2.imshow("Gray Image", imgGray)
cv2.imshow('Blur Image', imgBlur)
cv2.imshow('Canny Image', imgCanny)
cv2.imshow('Dialation Image', imgDialation)
cv2.imshow('Eroded Image', imgErode)
cv2.waitKey(0)