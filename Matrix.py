__author__ = 'Aadil_2'



f = open('textFile.txt','r')
#print file.readlines()

num_lines = sum(1 for line in f)
num_cols = sum(1 for char in range(num_lines))
f.close()
matrix = [[0 for i in xrange(num_cols+1)] for i in xrange(num_lines+1)]
f = open('textFile.txt','r')
for i in range(num_lines):
    line = f.readline()
    for j in range(len(line)):
        matrix[i][j]=line[j]

print matrix
