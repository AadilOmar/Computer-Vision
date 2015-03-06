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

thresh=120
cols,rows,d = image.shape
print ("ASDFASDF",cols,rows)
#1=black 2=white 2=green
smallMatrix = [[0 for i in xrange(rows/2)] for i in xrange(cols/2)]
matrix = [[0 for i in xrange(rows)] for i in xrange(cols)]

row = 0
col = 0

smallMatrix[cols/2-1][rows/2-1]=0
#x,y are numbers(enumerate)  x=rows   [cols][rows]
for x,i in enumerate(range(rows-1)):
    row+=1
    col=0
    for y,j in enumerate(range(cols-1)):
        if((y%2==0 and x%2==0) or (y%2==1 and x%2==1)):
            smallMatrix[col][row] = matrix[x][y]
            print matrix[x][y]
            col+=1
        else:
            smallMatrix[col][row]=0

for (x,y), value in np.ndenumerate(matrix):
    #if odd row and off column
    row+=1
    if((y%2==0 and x%2==0) or (y%2==1 and x%2==1)):
        smallMatrix[row][col] = matrix[y][x]
        print (x,y)
        col+=1
    else:
        smallMatrix[row][col]=0
print smallMatrix
