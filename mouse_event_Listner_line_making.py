# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 16:26:38 2021

@author: aakash
"""

import numpy as np
import cv2

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 2,(0,0,255),-1)
        '''when you give -1 as thickness it fills yours circle or any closed shape'''
        point.append((x,y))
        if len(point)>=2:
            cv2.line(img, point[-1], point[-2], (255,255,255), 2)
        cv2.imshow('image',img)
    
img = np.zeros((512,512,4))   
cv2.imshow('image',img)
point=[]
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
