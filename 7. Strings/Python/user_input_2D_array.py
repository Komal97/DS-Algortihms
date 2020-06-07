'''
how to take 2-D array as user input
'''
import numpy as np 

def print_matrix(matrix, r, c):
    print(matrix)
    for i in range(r):
        for j in range(c):
            print(matrix[i][j], end = " ")
        print()

r = int(input())
c = int(input())

# method 1
matrix = []
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)
print_matrix(matrix, r, c)

# method 2
matrix = [[int(input()) for x in range (c)] for y in range(r)]
print_matrix(matrix, r, c)

# method 3
entries = list(map(int, input().split()))
matrix = np.array(entries).reshape(r, c)
print_matrix(matrix, r, c)

# method 4
data = map(int, input().split())
matrix = [*map(list, zip(*[data] * c))]
return matrix