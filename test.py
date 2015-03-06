__author__ = 'Aadil_2'
import cv
import numpy as np
import cv2

image = cv2.imread('mona.jpg')
startPixelsToProcess=100
endpixelsToProcess=300


cols,rows,d = image.shape
print rows,cols
print image.item(215,229,0)

#for i in range(rows-1):
#    for j in range(cols):
#        print i,j
