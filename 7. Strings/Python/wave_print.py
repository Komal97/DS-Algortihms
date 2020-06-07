'''
Input a 2D array and print it in wave form.
Input : r = 5, c = 4
		matrix = 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
Output : 1 2 3 4 
		 5 6 7 8 
		 9 10 11 12 
		13 14 15 16 
		17 18 19 20 
		wave print = 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19 20 16 12 8 4 
'''
import numpy as np 

def print_matrix(matrix, r, c):
    for i in range(r):
        for j in range(c):
            print(matrix[i][j], end = " ")
        print()

def read_matrix(matrix, r, c):
    entries = list(map(int, input().split()))
    matrix = np.array(entries).reshape(r, c)
    return matrix 

def wave_print(matrix, r, c):
	for i in range(c):
		if i%2 == 0:
			for j in range(0, r):
				print(matrix[j][i], end = " ")
		else:
			for j in range(r-1, -1, -1):
				print(matrix[j][i], end = " ")
				
def main():
    r, c = input().split()
    r, c = int(r), int(c)
    
    matrix = []
    matrix = read_matrix(matrix, r, c)
    print_matrix(matrix, r, c)
    wave_print(matrix, r, c)
	
main()