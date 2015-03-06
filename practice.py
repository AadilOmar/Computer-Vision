from cv2.cv import CV_RETR_CCOMP, CV_CHAIN_APPROX_NONE

__author__ = 'Aadil_2'

import cv
import numpy as np
import cv2
from PIL import Image

image = cv2.imread('buzz.jpg')
startPixelsToProcess=100
endpixelsToProcess=300


#changes all pixels in image --changes all the reds to 0

needRow=20
needCol=30

#longer wide then tall
matrix = [[1 for i in xrange(needCol)] for i in xrange(needRow)]
smallMatrix = [[0 for i in xrange(needCol/2)] for i in xrange(needRow/2)]

print smallMatrix

row = 0
col = 0

#x,y are numbers(enumerate)  x=rows   [cols][rows]
for x,i in enumerate(range(needRow-1)):
    row+=1
    col=0
    for y,j in enumerate(range(needCol-1)):
        col+=1
print row,col


