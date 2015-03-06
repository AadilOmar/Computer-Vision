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

#1=black 2=white 2=green
matrix = [[0 for i in xrange(rows)] for i in xrange(cols)]

#creates matrix and puts contrasting pixel data (black edges and white background)
x=1;
for j in range(1,rows-1):
    for i in range(1,cols-1):
        #print i,j
        pt = image.item(i-1,j,0)+image.item(i-1,j,1)+image.item(i-1,j,2)
        pb = image.item(i+1,j,0)+image.item(i+1,j,1)+image.item(i+1,j,2)
        pl = image.item(i,j-1,0)+image.item(i,j-1,1)+image.item(i,j-1,2)
        pr = image.item(i,j+1,0)+image.item(i,j+1,1)+image.item(i,j+1,2)
        ptl=image.item(i-1,j-1,0)+image.item(i-1,j-1,1)+image.item(i-1,j-1,2)
        ptr=image.item(i-1,j+1,0)+image.item(i-1,j+1,1)+image.item(i-1,j+1,2)
        pbl=image.item(i+1,j-1,0)+image.item(i+1,j-1,1)+image.item(i+1,j-1,2)
        pbr=image.item(i+1,j+1,0)+image.item(i+1,j+1,1)+image.item(i+1,j+1,2)
        list = [pt,pb,pl,pr,ptl,ptr,pbl,pbr]
        darkest=pt
        lightest=pt
        for q,w in enumerate(list):
            if list[q] >lightest:
                lightest=list[q]
            if list[q]<darkest:
                darkest = list[q]
        #print lightest-darkest," THIS IS THE DARK_LIGHT",i,j,rows,cols
        if lightest-darkest>thresh:
            matrix[i][j]='1'
        else:
            matrix[i][j]='0'

#goes through matrix and sets the actual pic to black and white
for j in range(1,rows-1):
    for i in range(1,cols-1):

        #print "OKOK"
        if matrix[i][j]=='1':
            image.itemset((i,j,0),0)
            image.itemset((i,j,1),0)
            image.itemset((i,j,2),0)
        else:
            image.itemset((i,j,0),255)
            image.itemset((i,j,1),255)
            image.itemset((i,j,2),255)




#looks for green and paints green pixels where line is going 45 degrees
def findEdge(row,col):
    if matrix[row][col]=='0':
        #print "YEAYEAYEA"
        if matrix[row-1][col-1]=='0': #if tl is also white
            if matrix[row+1][col]=='1' and matrix[row+1][col+1]=='1' and matrix[row][col+1]=='1': #if bottom right corner is black
                print "ZZZZZZZZZZZZZZZZ"
                matrix[row][col]='2'
                image.itemset((i,j,0),0)
                image.itemset((i,j,1),255)
                image.itemset((i,j,2),0)
    else:
        image.itemset((i,j,0),255)
        image.itemset((i,j,1),255)
        image.itemset((i,j,2),255)


for j in range(1,rows-1):
    for i in range(1,cols-1):
        pass
        #print "PPPPPPPPQPQPQPPQ"
        #findEdge(i,j)
np.savetxt("textFile.txt", matrix, fmt='%s', delimiter='', newline='\n', header='', footer='', comments='# ')


cv2.imshow("asdf",image)
cv2.waitKey(0)
print "ok"

