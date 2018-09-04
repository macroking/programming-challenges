from __future__ import print_function
import os
import sys
import math
def rotate_matrix(mat):
    for x in range(0, int(math.ceil(N/2.0))):
        for y in range(x, N-x-1):
            temp = mat[x][y]                 #curr -> Temp
            mat[x][y] = mat[y][N-1-x]        #Right -> Top
            mat[y][N-1-x] = mat[N-1-x][N-1-y]#Bottom -> Right
            mat[N-1-x][N-1-y] = mat[N-1-y][x]#Left -> Bottom
            mat[N-1-y][x] = temp             #Temp -> Left
    return mat

# Function to pr the matrix
def displayMatrix( mat ):
    for i in range(0, N):
        for j in range(0, N):
            print (mat[i][j], end = ' ')
        print ("")

if __name__ == '__main__':
    mat = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]]
    N = len(mat)
    rotate_matrix(mat)
    displayMatrix(mat)