'''
Write a code which inputs two numbers m and n and creates a matrix of size m x n (m rows and n columns) in which every elements is either X or 0. 
The Xs and 0s must be filled alternatively, the matrix should have outermost rectangle of Xs, then a rectangle of 0s, then a rectangle of Xs, and so on.

Examples:

Input: m = 3, n = 3
Output: Following matrix 
X X X
X 0 X
X X X
'''

def print_matrix(matrix, r, c):
    for i in range(r):
        for j in range(c):
            print(matrix[i][j], end = " ")
        print()
        
def print_pattern(r, c):
    matrix = [["" for _ in range(c)] for _ in range(r)]
    start_row = 0
    start_col = 0
    end_row = r - 1 
    end_col = c - 1
	temp = 'X'
    
    while(start_row <= end_row and start_col <= end_col):
            
        for i in range(start_col, end_col + 1):
            matrix[start_row][i] = temp
        start_row += 1 
        
        for i in range(start_row, end_row + 1):
            matrix[i][end_col] = temp
        end_col -= 1
        
        if start_col <= end_col:
            for i in range(end_col, start_col-1, -1):
                matrix[end_row][i] = temp
            end_row -= 1
        
        if start_row <= end_row:
            for i in range(end_row, start_row-1, -1):
                matrix[i][start_col] = temp
            start_col += 1
        
        temp = 'X' if temp == '0' else '0'
    print_matrix(matrix, r, c)
        
        
def main():
    n = int(input())
    r, c = n, n
    print_pattern(r, c)

main()