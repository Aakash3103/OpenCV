# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 23:41:29 2021

@author: aakas
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 16:26:38 2021

@author: aakash
"""

import numpy as np
import cv2

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x,y,0]
        green = img[x,y,1]
        red= img[x,y,2]
        cv2.circle(img, (x,y), 3,(0,0,255),-1)
        mycolorimage=np.zeros((512,512,3),np.uint8)   
        mycolorimage[:]=[blue,green,red]
        cv2.imshow('lion color',mycolorimage)
    
    
img=cv2.imread('lion.jpg')   
cv2.imshow('lion',img)
cv2.setMouseCallback('lion',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()