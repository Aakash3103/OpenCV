# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 09:41:47 2021

@author: aakas
"""

import cv2
import datetime

cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(3,3000)
cap.set(4,3000)
print(cap.get(3))
print(cap.get(4))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'width :'+str(cap.get(3)) + 'height: '+str(cap.get(3))
        datem = str(datetime.datetime.now())
        frame = cv2.putText(frame,datem,(10,40),font,1,(0,255,255),2,cv2.LINE_AA)
        cv2.imshow('frame',frame)
        
        
        if cv2.waitKey(1) &0xff == ord('q'):
            break
    else:
        break
    
cap.release()
cv2.destroyAllWindows()