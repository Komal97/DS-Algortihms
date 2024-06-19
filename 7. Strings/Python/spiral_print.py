'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
'''

# variation - 1
'''
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


# variation - 2
'''
Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output: [1,4,7,8,9,6,3,5]
'''
row, col = 5, 7
arr = [[11, 12, 13, 14, 15, 16, 17], [21, 22, 23, 24, 25, 26, 27], [31, 32, 33, 34, 35, 36, 37], [41, 42, 43, 44, 45, 46, 47], [51, 52, 53, 54, 55, 56, 57]]

s_row = 0
e_row = row-1
s_col = 0
e_col = col-1

while(s_row <= e_row and s_col <= e_col):
    for i in range(s_row, e_row+1):
        print(arr[i][s_col])
    s_col +=1 

    for i in range(s_col, e_col+1):
        print(arr[e_row][i])
    e_row -=1 

    if s_col <= e_col:
        for i in range(e_row, s_row-1, -1):
            print(arr[i][e_col])
        e_col -=1

    if s_row <= e_row:
        for i in range(e_col, s_col-1, -1):
            print(arr[s_row][i])
        s_row +=1         