# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 23:56:58 2021

@author: aakas
"""


import cv2

rap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

print(rap.isOpened())

while(rap.isOpened()):
    
    ret, frame = rap.read()
    
    if ret == True:
    
        print(rap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(rap.get(cv2.CAP_PROP_FRAME_WIDTH))
        
        out.write(frame)        
        cv2.imshow('video_mode',frame)
        
        if cv2.waitKey(1) &0xff == ord('q'):
            break
    else:
        break
    
rap.release()
out.release()
cv2.destroyAllWindows()
