'''
nCr = n!/(r! * (n-r)!)
use pascal triangle to create a recursive case
'''

def nCr(n, r):
    if r==0 or r==n:
        return 1
    
    return nCr(n-1, r-1) + nCr(n-1, r)

print(nCr(4, 2))