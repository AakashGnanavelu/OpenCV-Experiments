# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 09:08:00 2021

@author: Aakash
"""

import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
cv2.rectangle(img,(0,0), (250,350),(0,0,255))
cv2.circle(img,(400,50), 30, (255,255,0), 5)
cv2.putText(img, 'OpenCV Text', (250, 150), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (100, 150,100), 1)

cv2.imshow("Image", img)
cv2.waitKey(0)