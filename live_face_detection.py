# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 15:31:27 2021

@author: Aakash
"""

import cv2
import time

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
faceCascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.5, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + y, y + h), (255, 0, 0), 2)
    cv2.imshow("frame", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()