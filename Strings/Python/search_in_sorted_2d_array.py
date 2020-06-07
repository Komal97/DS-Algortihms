'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example:
Consider the following matrix:
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Given target = 5, return true.
Given target = 20, return false.
'''

import numpy as np
def readMatrix(matrix, r, c):
    entries = list(map(int, input().split()))
    matrix = np.array(entries).reshape(r, c)
    return matrix
    
def search(matrix, r, c, key):
    i = 0
    j = c-1
    
    while(i<r and j>=0):
        if matrix[i][j] == key:
            return 1
        elif matrix[i][j] > key:
            j -= 1
        else:
            i += 1
    return 0
    
    
def main():
    t = int(input())
    while(t):
        r, c = input().split()
        r, c = int(r), int(c)
        matrix = []
        matrix = readMatrix(matrix, r, c)
        key = int(input())
        print(search(matrix, r, c, key))
        t -= 1
    
main()