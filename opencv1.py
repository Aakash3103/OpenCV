# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 10:14:04 2021

@author: aakas
"""

import cv2

img = cv2.imread('aakash.jpeg',-1)
cv2.imshow('image',img)
k = cv2.waitKey(10000)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('aakash_copy.png',img)
    cv2.destroyAllWindows()
