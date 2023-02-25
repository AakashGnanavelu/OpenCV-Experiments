# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 15:20:18 2021

@author: Aakash
"""

import cv2

img = cv2.imread('rimuru.png')
print(img.shape)

imgResize = cv2.resize(img,(600,300))
imgCropped = img[0:250, 0:300]

cv2.imshow('Image', img)
cv2.imshow('Resized Image', imgResize)