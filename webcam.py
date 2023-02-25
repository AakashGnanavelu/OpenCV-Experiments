# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 10:52:30 2021

@author: Aakash
"""

import cv2

vid = cv2.VideoCapture('rtsp://admin:Radha1960@192.168.1.225:554/profile2/media.smp')
vid.set(3, 640)
vid.set(4, 480)

while(True):
    success, img = vid.read()

    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
