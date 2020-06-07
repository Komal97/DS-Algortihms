'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output: [1,2,3,6,9,8,7,4,5]
'''
import numpy as np
def readMatrix(matrix, r, c):
    entries = list(map(int, input().split()))
    matrix = np.array(entries).reshape(r, c)
    matrix = list(matrix)
    return matrix 

def print_spriral(matrix, r, c):
    start_row = 0
    start_col = 0
    end_row = r - 1
    end_col = c - 1
    
    while(start_row <= end_row and start_col <= end_col):
        for i in range(start_col, end_col+1):
            print(matrix[start_row][i], end = " ")
        start_row += 1
        
        for i in range(start_row, end_row+1):
            print(matrix[i][end_col], end = " ")
        end_col -= 1
        
        if start_row <= end_row:
            for i in range(end_col, start_col-1, -1):
                print(matrix[end_row][i], end = " ")
            end_row -= 1
        
        if start_col <= end_col:
            for i in range(end_row, start_row-1, -1):
                print(matrix[i][start_col], end = " ")
            start_col += 1

def main():
    t = int(input())
    while(t):
        r, c = input().split()
        r, c = int(r), int(c)
        matrix = []
        matrix = readMatrix(matrix, r, c)
        print_spriral(matrix, r, c)
        print()
        t -= 1

main()