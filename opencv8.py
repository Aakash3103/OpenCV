# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 14:03:01 2021

@author: aakas
"""

import numpy as np
import cv2

def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, " ",y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strxy= str(x) + ' ,' +str(y)
        cv2.putText(img,strxy,(x,y),font,.5,(255,255,0),2)
        cv2.imshow('image',img)
        
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,2]
        red = img[y,x,3]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strbgr= str(blue) + ' ,' +str(green)+','+str(red)
        cv2.putText(img,strbgr ,(x,y),font,.5,(0,255,255),2)
        cv2.imshow('image',img)
    
    
    
    
img = np.zeros((512,512,3),np.uint8)
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()